(() => {
  const NAME_KEY = "aai-learner-name";

  const dogmaCopy = {
    dna: {
      title: "DNA",
      text: "Stable sequence information in a clone. Mutations and copy-number changes are heritable. Most cell-state changes do not rewrite DNA.",
    },
    transcription: {
      title: "Transcription",
      text: "RNA polymerases copy genes under the control of transcription factors, enhancers, and chromatin. This is the main gate between genome and program.",
    },
    rna: {
      title: "RNA",
      text: "mRNA is a high-throughput snapshot of recent transcription. Splicing, noncoding RNAs, and RNA stability all matter. Droplet scRNA-seq mostly counts 3′ ends of poly(A) transcripts.",
    },
    translation: {
      title: "Translation",
      text: "Ribosomes build polypeptides from mRNA. Protein output can diverge from mRNA because of translation rate, degradation, and localization.",
    },
    protein: {
      title: "Protein",
      text: "Function often depends on folding and post-translational modification. Phosphorylation can switch a pathway without any change in that protein’s mRNA.",
    },
    signaling: {
      title: "Signaling and transcription factors",
      text: "Ligands and receptors feed kinases and other messengers that regulate transcription factors. That is control of information flow, not reverse translation of protein sequence into DNA.",
    },
  };

  const hallmarkCopy = {
    proliferation: {
      title: "Sustaining proliferative signaling",
      text: "Clones keep mitogenic programs on — receptor tyrosine kinases, RAS, MYC, and others. In scRNA-seq this may look like a cycling or growth-factor program. That is state, not automatically a proven driver mutation.",
    },
    suppressors: {
      title: "Evading growth suppressors",
      text: "Tumor suppressors such as RB and TP53 restrain the cycle and DNA-damage responses. Loss is a genetic/epigenetic event; the RNA neighborhood is only a clue.",
    },
    death: {
      title: "Resisting cell death",
      text: "Apoptosis and other death programs can be blunted. Immune killing uses overlapping and distinct death routes — the next module.",
    },
    immortality: {
      title: "Enabling replicative immortality",
      text: "Telomere maintenance lets clones divide far beyond normal limits. This hallmark is easy to skip in RNA tutorials and still biologically real.",
    },
    angiogenesis: {
      title: "Inducing angiogenesis",
      text: "Tumors recruit vessels. Hypoxia programs in scRNA-seq are a state that may sit next to VEGF-family signaling, not a photograph of a vessel.",
    },
    invasion: {
      title: "Invasion and metastasis",
      text: "Epithelial programs can shift. Do not treat every EPCAM-low cluster as proven EMT. Space and protein still matter.",
    },
    metabolism: {
      title: "Reprogramming energy metabolism",
      text: "Aerobic glycolysis and other shifts support biomass and survival. Metabolites also shape immune cells in the niche.",
    },
    immunity: {
      title: "Avoiding immune destruction",
      text: "This is the bridge into Module 4: antigen presentation, checkpoints, exclusion, and myeloid programs. The hallmark names the phenotype; the cycle names the steps.",
    },
  };

  const cycleCopy = {
    antigen: {
      title: "1. Release of tumor antigens",
      text: "Dying or stressed tumor cells can release proteins that become peptide antigens. If a clone is poorly antigenic, later steps never start. scRNA-seq does not measure peptides; it can only hint at antigen-processing transcripts.",
    },
    presentation: {
      title: "2. Antigen presentation",
      text: "Dendritic cells and other APCs process antigen and provide costimulation. Failure here looks like ignorance, not exhausted T cells in the tumor.",
    },
    priming: {
      title: "3. Priming and activation",
      text: "T cells expand in lymphoid tissue. CTLA-4 is a teaching example of a brake at this end of the cycle.",
    },
    traffic: {
      title: "4. T-cell trafficking",
      text: "Chemokines and endothelium decide whether primed T cells reach the tumor bed. RNA from a dissociated biopsy cannot show the path they took.",
    },
    infiltrate: {
      title: "5. Infiltration into tumor",
      text: "Stroma can exclude T cells at a margin. That pattern is spatial. A UMAP with few T cells cannot by itself prove exclusion versus absence versus dropout.",
    },
    recognize: {
      title: "6. Recognition of cancer cells",
      text: "CD8 T cells see peptide–MHC I. Loss of MHC or antigen-processing genes is a classic escape. PD-1 ligands act after recognition is possible.",
    },
    kill: {
      title: "7. Killing and more antigen",
      text: "Effector function can fail even with infiltration — exhaustion programs, checkpoints, suppressive myeloid cells. Successful killing feeds antigen back into step 1.",
    },
  };

  const heatmapNotes = {
    genes: {
      EPCAM: "EPCAM is high in E1–E3 and in the suspicious X1 column. Epithelial-like program, not a proof of malignancy.",
      KRT8: "KRT8 tracks EPCAM here. Co-expression of epithelial genes is how you start a lineage hypothesis.",
      CD3D: "CD3D marks T-lineage barcodes T1–T3. X1 also has CD3D — that mixed program is why X1 is a doublet candidate.",
      CD8A: "CD8A splits the T-like cells: T1–T2 vs T3. Real data need more markers and still may stay “CD3+ CD8−”.",
      MS4A1: "MS4A1 (CD20) isolates B1. One marker is not a finished annotation, but it is enough for this toy matrix.",
      CD68: "CD68 isolates M1 as myeloid-like. Myeloid states in tumors are much finer than this cartoon.",
      MKI67: "MKI67 is a cycling program. X1 is high — cycling plus mixed lineage genes is still not a new cell type until doublets are ruled out.",
    },
    cells: {
      0: "E1: epithelial-like (EPCAM, KRT8).",
      1: "E2: epithelial-like.",
      2: "E3: epithelial-like.",
      3: "T1: CD8 T-like (CD3D, CD8A).",
      4: "T2: CD8 T-like.",
      5: "T3: T-like without CD8A. Leave it as CD3+ CD8− until more evidence exists.",
      6: "B1: B-cell-like (MS4A1).",
      7: "M1: myeloid-like (CD68).",
      8: "X1: epithelial + T + cycling genes together. Abstain. Check doublets and ambient RNA before naming a hybrid cell.",
    },
  };

  function learnerName() {
    return window.localStorage.getItem(NAME_KEY) || "";
  }

  function setLearnerName(name) {
    window.localStorage.setItem(NAME_KEY, name);
  }

  function fillLearnerForm() {
    const input = document.querySelector("#learnerName");
    if (input && learnerName()) {
      input.value = learnerName();
    }
  }

  async function markVisited(moduleId) {
    const name = learnerName();
    if (!name || !moduleId) {
      return;
    }
    try {
      await fetch("/api/progress", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ name, module_id: moduleId }),
      });
    } catch (_error) {
      // Progress is optional; the lesson should still work.
    }
  }

  function setPressed(buttons, active) {
    buttons.forEach((button) => {
      const on = button === active;
      button.classList.toggle("is-active", on);
      button.setAttribute("aria-pressed", on ? "true" : "false");
    });
  }

  function bindChoiceGroup(selector, copy, panelSelector, keyAttr) {
    const buttons = Array.from(document.querySelectorAll(selector));
    const panel = document.querySelector(panelSelector);
    if (!buttons.length || !panel) {
      return;
    }
    buttons.forEach((button) => {
      button.addEventListener("click", () => {
        setPressed(buttons, button);
        const key = button.getAttribute(keyAttr);
        const item = copy[key];
        if (item) {
          panel.innerHTML = `<h3>${item.title}</h3><p>${item.text}</p>`;
        }
      });
    });
  }

  function bindHeatmap() {
    const table = document.querySelector("#umiTable");
    const caption = document.querySelector("#heatmapCaption");
    if (!table || !caption) {
      return;
    }
    const geneButtons = table.querySelectorAll("button[data-gene]");
    const cellButtons = table.querySelectorAll("button[data-cell]");
    const rows = table.querySelectorAll("tbody tr");

    function clear() {
      table.querySelectorAll(".is-hot, .is-row, .is-col, .is-active").forEach((node) => {
        node.classList.remove("is-hot", "is-row", "is-col", "is-active");
      });
    }

    geneButtons.forEach((button) => {
      button.addEventListener("click", () => {
        clear();
        button.classList.add("is-active");
        const gene = button.getAttribute("data-gene");
        const row = table.querySelector(`tr[data-gene="${gene}"]`);
        if (row) {
          row.classList.add("is-row");
          row.querySelectorAll("td").forEach((cell) => {
            if (Number(cell.textContent) >= 6) {
              cell.classList.add("is-hot");
            }
          });
        }
        caption.textContent = heatmapNotes.genes[gene] || caption.textContent;
      });
    });

    cellButtons.forEach((button) => {
      button.addEventListener("click", () => {
        clear();
        button.classList.add("is-active");
        const index = Number(button.getAttribute("data-cell"));
        rows.forEach((row) => {
          const cell = row.querySelectorAll("td")[index];
          if (cell) {
            cell.classList.add("is-col");
            if (Number(cell.textContent) >= 6) {
              cell.classList.add("is-hot");
            }
          }
        });
        caption.textContent = heatmapNotes.cells[index] || caption.textContent;
      });
    });
  }

  function bindLearnerForm() {
    const form = document.querySelector("#learnerForm");
    if (!form) {
      return;
    }
    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      const name = String(new FormData(form).get("learnerName") || "").trim();
      const status = document.querySelector("#learnerStatus");
      if (!name) {
        return;
      }
      setLearnerName(name);
      if (status) {
        status.textContent = `Saved as ${name}. Progress will attach to this name.`;
      }
      try {
        await fetch("/api/progress", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({ name }),
        });
      } catch (_error) {
        if (status) {
          status.textContent = `Saved locally as ${name}. The server progress file was not reachable.`;
        }
      }
    });
  }

  function bindQuiz() {
    const form = document.querySelector("#quizForm");
    const article = document.querySelector(".quiz");
    if (!form || !article) {
      return;
    }
    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      const moduleId = article.getAttribute("data-module-id");
      const answers = {};
      new FormData(form).forEach((value, key) => {
        answers[key] = Number(value);
      });
      const response = await fetch("/api/quiz/grade", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          module_id: moduleId,
          answers,
          name: learnerName(),
        }),
      });
      const payload = await response.json();
      const summary = document.querySelector("#quizSummary");
      if (!response.ok) {
        if (summary) {
          summary.textContent = payload.error || "Scoring failed.";
        }
        return;
      }
      payload.results.forEach((result) => {
        const fieldset = form.querySelector(`[data-question-id="${result.id}"]`);
        if (!fieldset) {
          return;
        }
        fieldset.classList.toggle("is-right", result.correct);
        fieldset.classList.toggle("is-wrong", !result.correct);
        const feedback = fieldset.querySelector(".quiz-feedback");
        if (feedback) {
          feedback.hidden = false;
          const mark = result.correct ? "Correct." : "Not quite.";
          feedback.textContent = `${mark} ${result.explanation}`;
        }
      });
      if (summary) {
        summary.textContent = `Score: ${payload.correct} / ${payload.total}.`;
      }
    });
  }

  function bindTutor() {
    const form = document.querySelector("#tutorForm");
    const lesson = document.querySelector(".lesson");
    const log = document.querySelector("#tutorLog");
    if (!form || !lesson || !log) {
      return;
    }
    const history = [];
    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      const textarea = document.querySelector("#tutorMessage");
      const message = String(textarea.value || "").trim();
      if (!message) {
        return;
      }
      const userTurn = document.createElement("div");
      userTurn.className = "tutor-turn user";
      userTurn.innerHTML = `<p><strong>You</strong></p><p></p>`;
      userTurn.querySelectorAll("p")[1].textContent = message;
      log.append(userTurn);
      textarea.value = "";
      const pending = document.createElement("div");
      pending.className = "tutor-turn";
      pending.innerHTML = `<p><strong>Tutor</strong></p><p>Thinking…</p>`;
      log.append(pending);
      try {
        const response = await fetch("/api/tutor", {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            message,
            module_id: lesson.getAttribute("data-module-id"),
            history,
          }),
        });
        const payload = await response.json();
        if (!response.ok) {
          pending.querySelectorAll("p")[1].textContent = payload.error || "The tutor is unavailable.";
          return;
        }
        pending.querySelectorAll("p")[1].textContent = payload.reply;
        history.push({ role: "user", content: message });
        history.push({ role: "assistant", content: payload.reply });
      } catch (_error) {
        pending.querySelectorAll("p")[1].textContent = "Network error talking to the tutor.";
      }
    });
  }

  document.addEventListener("DOMContentLoaded", () => {
    fillLearnerForm();
    bindLearnerForm();
    bindQuiz();
    bindTutor();
    bindHeatmap();
    bindChoiceGroup(".dogma-node", dogmaCopy, "#dogmaPanel", "data-stage");
    bindChoiceGroup(".map-card", hallmarkCopy, "#hallmarkPanel", "data-hallmark");
    bindChoiceGroup(".cycle-step", cycleCopy, "#cyclePanel", "data-step");
    const lesson = document.querySelector(".lesson");
    if (lesson) {
      markVisited(lesson.getAttribute("data-module-id"));
    }
  });
})();
