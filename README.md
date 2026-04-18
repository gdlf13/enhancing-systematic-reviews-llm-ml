# Enhancing Systematic Reviews: LLM, Prompt Engineering & ML — R2 Reproducibility Update

**Manuscript:** RSM-2025-0110 — "Enhancing Systematic Reviews: Integrating LLM Prompt Engineering and Machine Learning Methods"

**DOI:** 10.5281/zenodo.15291559

This update adds the files and scripts needed to reproduce the analyses described in the Response to Reviewer 2 (R2 revision).

---

## Where files go in the GitHub repo

```
enhancing-systematic-reviews-llm-ml/
├── README.md
├── requirements.txt                                      ← updated
├── code/
│   ├── 01_compute_per_database_metrics.py                ← NEW: reproduces Table S1
│   ├── 02_inspect_model_pipeline.py                      ← NEW: verifies SMOTE pipeline
│   └── 03_reproduce_holdout_split.py                     ← NEW: reproduces class distribution & split
├── data/
│   ├── ml_training/
│   │   └── WoS_health_revised_MO.xlsx                    ← WoS training data (695 records)
│   ├── predictions/
│   │   ├── PubMed_predictions.xlsx                       ← NEW: MLM + Human Reviewer labels (N=146)
│   │   ├── Scopus_predictions.xlsx                       ← NEW: MLM + Human Reviewer labels (N=422)
│   │   ├── IEEE_predictions.xlsx                         ← NEW: MLM + Human Reviewer labels (N=1073)
│   │   ├── ARXIV_predictions.xlsx                        ← NEW: MLM + Human Reviewer labels (N=264)
│   │   └── ACM_predictions.xlsx                          ← NEW: MLM + Human Reviewer labels (N=1112)
│   └── Supplementary_Table_Per_Database_Metrics.xlsx     ← NEW: Table S1
├── models/
│   └── my_trained_model_Mig_review_with_SMOTE.joblib     ← NEW: imblearn Pipeline (TF-IDF + SMOTE + LR)
└── prompts/
    ├── Appendix A.docx                                   ← All prompts (Prompts 1–10)
    └── Appendix B.docx                                   ← Supplementary prompt materials
```

---

## What This Supports (mapped to Reviewer 2 comments)

### Comment 1 — Training-Evaluation Circularity
- **Script:** `code/01_compute_per_database_metrics.py`
- **Data:** 5 `*_predictions.xlsx` files in `data/predictions/`
- **Output:** Supplementary Table S1 with per-database Accuracy, Precision, Recall, F1, Kappa + 95% bootstrap CIs
- **Claim verified:** "Per-database performance metrics are reproducible from the trained model and input data available at DOI: 10.5281/zenodo.15291559"

### Comment 5 — SMOTE Implementation (No Data Leakage)
- **Script:** `code/02_inspect_model_pipeline.py`
- **Model:** `models/my_trained_model_Mig_review_with_SMOTE.joblib`
- **Script:** `code/03_reproduce_holdout_split.py`
- **Data:** `data/ml_training/WoS_health_revised_MO.xlsx`
- **Claims verified:**
  - Pipeline is `imblearn.pipeline.Pipeline` (SMOTE bypassed during `.predict()`)
  - Class distribution: 139 health-related (20%) vs 556 not-health-related (80%)
  - Hold-out split: train N=625 (125 pos / 500 neg), test N=70 (14 pos / 56 neg)
  - SMOTE (auto): generated 375 synthetic positives → balanced 500/500

### Comment 6 — LLM Reproducibility
- All prompts are documented in `prompts/Appendix A.docx` (Prompts 1–10) and `prompts/Appendix B.docx`
- LLM input/output data are in the `*_predictions.xlsx` files (LLM column)

---

## How to Run

```bash
# Clone the repo
git clone https://github.com/gdlf13/enhancing-systematic-reviews-llm-ml.git
cd enhancing-systematic-reviews-llm-ml

# Install dependencies
pip install -r requirements.txt

# Reproduce Table S1
python code/01_compute_per_database_metrics.py

# Inspect model pipeline (SMOTE verification)
python code/02_inspect_model_pipeline.py

# Reproduce hold-out split and class distribution
python code/03_reproduce_holdout_split.py
```

---

## Data Column Descriptions

### Prediction files (*_predictions.xlsx)
| Column | Description |
|--------|-------------|
| Authors / Author | Article authors |
| Title | Article title |
| Abstract | Article abstract |
| Year | Publication year |
| Human Reviewer | Human screening label: "Health related" or "Not health related" |
| LLM | GPT-4 screening label: "Health related" or "Not health related" |
| ML Model | MLM prediction: 1 (health related) or 0 (not health related) |

### Training data (WoS_health_revised_MO.xlsx)
- Column index 4 ("Unnamed: 4" / "Mig Review"): Human Reviewer labels used for training
- Column index 5 ("Unnamed: 5" / "GPT4 Review"): LLM labels

---

## Notes

- The model file `my_trained_model_Mig_review_with_SMOTE.joblib` is the trained imblearn Pipeline (TF-IDF + SMOTE + Logistic Regression) as described in the manuscript.
- The MLM was trained with scikit-learn 1.3.0 and imbalanced-learn. Loading with newer versions may produce warnings but does not affect predictions.
- Scopus predictions contain 7 records with missing ML Model values (NaN); these are excluded from metric computation (N=422 after filtering, from 429 total).
- The pooled metrics (Accuracy 95.9%, Kappa 0.794) are computed across the 5 non-WoS databases only. The manuscript-reported Table 1 figures (95.1%, 0.812) include WoS and are therefore not directly comparable.
