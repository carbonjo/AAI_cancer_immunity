from app import app
from content.lessons import MODULES, get_module


def test_home_and_module_pages_ok():
    client = app.test_client()
    assert client.get("/").status_code == 200
    for module in MODULES:
        lesson = client.get(f"/learn/{module['id']}")
        quiz = client.get(f"/quiz/{module['id']}")
        assert lesson.status_code == 200, module["id"]
        assert quiz.status_code == 200, module["id"]
        assert module["title"].encode() in lesson.data
    missing = client.get("/learn/not-a-module")
    assert missing.status_code == 404


def test_health_without_key():
    client = app.test_client()
    payload = client.get("/api/health").get_json()
    assert payload["ok"] is True
    assert payload["tutor"] is False


def test_quiz_grades_without_openai():
    client = app.test_client()
    module = get_module("info-flow")
    answers = {item["id"]: item["answer_index"] for item in module["quiz"]}
    response = client.post(
        "/api/quiz/grade",
        json={"module_id": "info-flow", "answers": answers, "name": "Test Learner"},
    )
    payload = response.get_json()
    assert response.status_code == 200
    assert payload["correct"] == payload["total"] == len(module["quiz"])


def test_quiz_wrong_answers():
    client = app.test_client()
    module = get_module("immunity")
    answers = {item["id"]: (item["answer_index"] + 1) % 4 for item in module["quiz"]}
    payload = client.post(
        "/api/quiz/grade",
        json={"module_id": "immunity", "answers": answers},
    ).get_json()
    assert payload["correct"] == 0
    assert payload["total"] == 5


def test_tutor_off_without_key():
    client = app.test_client()
    response = client.post("/api/tutor", json={"message": "What is MHC?", "module_id": "immunity"})
    assert response.status_code == 503
