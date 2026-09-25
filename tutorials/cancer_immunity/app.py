from __future__ import annotations

import json
import os
from pathlib import Path
from threading import Lock

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from openai import APIError, OpenAI

from content.lessons import MODULES, get_module, module_summaries, public_module
from content.tutor import system_prompt

load_dotenv()

ROOT = Path(__file__).resolve().parent
DATA_DIR = Path(os.environ.get("DATA_DIR", ROOT / "data"))
PROGRESS_FILE = DATA_DIR / "progress.json"
PROGRESS_LOCK = Lock()

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "dev-only-change-me")

OPENAI_MODEL = os.environ.get("OPENAI_MODEL", "gpt-4o-mini")


def openai_configured() -> bool:
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    return bool(key) and key not in {"sk-your-key-here", "your-key-here"}


def openai_client() -> OpenAI:
    return OpenAI(api_key=os.environ["OPENAI_API_KEY"].strip())


def load_progress() -> dict:
    if not PROGRESS_FILE.exists():
        return {"learners": {}}
    try:
        return json.loads(PROGRESS_FILE.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"learners": {}}


def save_progress(payload: dict) -> None:
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    tmp = PROGRESS_FILE.with_suffix(".tmp")
    tmp.write_text(json.dumps(payload, indent=2), encoding="utf-8")
    tmp.replace(PROGRESS_FILE)


def empty_learner(name: str) -> dict:
    return {
        "name": name,
        "modules": {
            module["id"]: {"visited": False, "quiz_score": None, "quiz_length": len(module["quiz"])}
            for module in MODULES
        },
    }


@app.context_processor
def inject_globals():
    return {
        "modules": module_summaries(),
        "tutor_ready": openai_configured(),
        "team": {
            "students": ["David Graham", "Dominic Sciarrino"],
            "sme": "Dr. John Krolewski",
            "advisor": "Dr. Joaquin Carbonara",
        },
    }


@app.get("/")
def home():
    return render_template("home.html")


@app.get("/learn/<module_id>")
def learn(module_id: str):
    module = get_module(module_id)
    if module is None:
        return render_template("not_found.html"), 404
    idx = next(i for i, item in enumerate(MODULES) if item["id"] == module_id)
    previous_mod = MODULES[idx - 1] if idx > 0 else None
    next_mod = MODULES[idx + 1] if idx + 1 < len(MODULES) else None
    return render_template(
        "learn.html",
        module=public_module(module),
        previous_mod=previous_mod,
        next_mod=next_mod,
    )


@app.get("/quiz/<module_id>")
def quiz(module_id: str):
    module = get_module(module_id)
    if module is None:
        return render_template("not_found.html"), 404
    return render_template("quiz.html", module=public_module(module))


@app.get("/api/health")
def health():
    return jsonify(
        {
            "ok": True,
            "tutor": openai_configured(),
            "model": OPENAI_MODEL if openai_configured() else None,
        }
    )


@app.post("/api/progress")
def progress():
    body = request.get_json(silent=True) or {}
    name = str(body.get("name", "")).strip()[:80]
    module_id = str(body.get("module_id", "")).strip()
    if not name:
        return jsonify({"error": "Enter a name to save progress."}), 400
    with PROGRESS_LOCK:
        store = load_progress()
        learners = store.setdefault("learners", {})
        row = learners.setdefault(name, empty_learner(name))
        if module_id and module_id in row["modules"]:
            row["modules"][module_id]["visited"] = True
        save_progress(store)
    return jsonify(row)


@app.post("/api/quiz/grade")
def grade_quiz():
    body = request.get_json(silent=True) or {}
    module = get_module(str(body.get("module_id", "")))
    answers = body.get("answers") or {}
    name = str(body.get("name", "")).strip()[:80]
    if module is None:
        return jsonify({"error": "Unknown module."}), 404

    results = []
    correct = 0
    for item in module["quiz"]:
        selected = answers.get(item["id"])
        try:
            selected_index = int(selected)
        except (TypeError, ValueError):
            selected_index = -1
        is_correct = selected_index == item["answer_index"]
        if is_correct:
            correct += 1
        results.append(
            {
                "id": item["id"],
                "correct": is_correct,
                "answer_index": item["answer_index"],
                "explanation": item["explanation"],
            }
        )

    total = len(module["quiz"])
    if name:
        with PROGRESS_LOCK:
            store = load_progress()
            learners = store.setdefault("learners", {})
            row = learners.setdefault(name, empty_learner(name))
            row["modules"][module["id"]]["visited"] = True
            row["modules"][module["id"]]["quiz_score"] = correct
            row["modules"][module["id"]]["quiz_length"] = total
            save_progress(store)

    return jsonify({"correct": correct, "total": total, "results": results})


@app.post("/api/tutor")
def tutor():
    if not openai_configured():
        return jsonify(
            {
                "error": "Tutor is off until OPENAI_API_KEY is set in .env. Quizzes still work."
            }
        ), 503

    body = request.get_json(silent=True) or {}
    message = str(body.get("message", "")).strip()
    module_id = body.get("module_id") or None
    history = body.get("history") or []
    if not message:
        return jsonify({"error": "Type a question first."}), 400
    if len(message) > 4000:
        return jsonify({"error": "Please shorten the question."}), 400

    messages = [{"role": "system", "content": system_prompt(module_id)}]
    if isinstance(history, list):
        for turn in history[-8:]:
            role = turn.get("role")
            content = str(turn.get("content", "")).strip()
            if role in {"user", "assistant"} and content:
                messages.append({"role": role, "content": content[:4000]})
    messages.append({"role": "user", "content": message})

    try:
        response = openai_client().chat.completions.create(
            model=OPENAI_MODEL,
            messages=messages,
            temperature=0.3,
            max_tokens=500,
        )
    except APIError as exc:
        return jsonify({"error": f"The tutor could not reach OpenAI ({exc.__class__.__name__})."}), 502
    except Exception:
        return jsonify({"error": "The tutor failed unexpectedly. Try again."}), 502

    text = (response.choices[0].message.content or "").strip()
    if not text:
        return jsonify({"error": "The tutor returned an empty reply."}), 502
    return jsonify({"reply": text})


def create_app() -> Flask:
    return app


if __name__ == "__main__":
    port = int(os.environ.get("PORT", "5050"))
    debug = os.environ.get("FLASK_DEBUG", "0") == "1"
    app.run(host="0.0.0.0", port=port, debug=debug)
