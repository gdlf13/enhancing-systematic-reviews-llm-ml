"""
01_compute_per_database_metrics.py
===================================
Reproduces Supplementary Table S1: per-database performance metrics
for the MLM Digital Reviewer (Comment 1 response).

The trained MLM (imblearn Pipeline: TF-IDF + SMOTE + Logistic Regression)
was developed on Web of Science data and applied WITHOUT retraining to
five additional databases. This script computes Accuracy, Precision,
Recall, F1-Score, and Cohen's Kappa for each database, with 95%
bootstrap confidence intervals (2,000 iterations).

Usage (from repo root):
    python code/01_compute_per_database_metrics.py

Input files (expected in data/predictions/):
    - PubMed_predictions.xlsx
    - Scopus_predictions.xlsx
    - IEEE_predictions.xlsx
    - ARXIV_predictions.xlsx
    - ACM_predictions.xlsx

Each file must contain columns:
    - 'ML Model': model predictions (0 or 1)
    - 'Human Reviewer': human labels ('Health related' or 'Not health related')

Output:
    - Prints per-database metrics table to console
    - Saves data/Supplementary_Table_S1_reproduced.xlsx
"""

import os
import pandas as pd
import numpy as np
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score,
    f1_score, cohen_kappa_score
)

# --- Configuration ---
# Paths relative to repo root (script lives in code/)
REPO_ROOT = os.path.join(os.path.dirname(__file__), '..')
DATA_DIR = os.path.join(REPO_ROOT, 'data', 'predictions')
OUTPUT_DIR = os.path.join(REPO_ROOT, 'data')
N_BOOTSTRAP = 2000
RANDOM_STATE = 42

DATABASES = {
    'PubMed':  'PubMed_predictions.xlsx',
    'Scopus':  'Scopus_predictions.xlsx',
    'IEEE':    'IEEE_predictions.xlsx',
    'arXiv':   'ARXIV_predictions.xlsx',
    'ACM':     'ACM_predictions.xlsx',
}


def encode_human_reviewer(x):
    """Convert Human Reviewer text labels to binary (1 = health related)."""
    s = str(x).strip().lower()
    if 'not' in s:
        return 0
    if 'health' in s:
        return 1
    return 0


def compute_metrics(y_true, y_pred):
    """Compute classification metrics."""
    return {
        'Accuracy': accuracy_score(y_true, y_pred),
        'Precision': precision_score(y_true, y_pred, zero_division=0),
        'Recall': recall_score(y_true, y_pred, zero_division=0),
        'F1-Score': f1_score(y_true, y_pred, zero_division=0),
        'Kappa': cohen_kappa_score(y_true, y_pred),
    }


def bootstrap_ci(y_true, y_pred, n_iterations=N_BOOTSTRAP, ci=95):
    """Compute bootstrap confidence intervals for all metrics."""
    rng = np.random.RandomState(RANDOM_STATE)
    n = len(y_true)
    boot_metrics = {k: [] for k in ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'Kappa']}

    for _ in range(n_iterations):
        idx = rng.randint(0, n, size=n)
        yt = y_true[idx]
        yp = y_pred[idx]
        if len(np.unique(yt)) < 2:
            continue
        m = compute_metrics(yt, yp)
        for k, v in m.items():
            boot_metrics[k].append(v)

    ci_results = {}
    alpha = (100 - ci) / 2
    for k, vals in boot_metrics.items():
        if vals:
            ci_results[k] = (np.percentile(vals, alpha), np.percentile(vals, 100 - alpha))
        else:
            ci_results[k] = (np.nan, np.nan)
    return ci_results


def main():
    results = []

    all_y_true = []
    all_y_pred = []

    for db_name, filename in DATABASES.items():
        filepath = os.path.join(DATA_DIR, filename)
        df = pd.read_excel(filepath)

        # Drop rows with missing predictions or labels
        df = df.dropna(subset=['ML Model', 'Human Reviewer'])

        y_true = df['Human Reviewer'].apply(encode_human_reviewer).values
        y_pred = df['ML Model'].astype(int).values

        metrics = compute_metrics(y_true, y_pred)
        cis = bootstrap_ci(y_true, y_pred)

        row = {'Database': db_name, 'N': len(df)}
        for metric_name in ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'Kappa']:
            val = metrics[metric_name]
            lo, hi = cis[metric_name]
            if metric_name == 'Kappa':
                row[metric_name] = f"{val:.3f}"
                row[f"{metric_name} 95% CI"] = f"[{lo:.3f}, {hi:.3f}]"
            else:
                row[metric_name] = f"{val*100:.1f}%"
                row[f"{metric_name} 95% CI"] = f"[{lo*100:.1f}%, {hi*100:.1f}%]"
        results.append(row)

        all_y_true.extend(y_true)
        all_y_pred.extend(y_pred)

    # Pooled metrics across all 5 databases
    all_y_true = np.array(all_y_true)
    all_y_pred = np.array(all_y_pred)
    pooled_metrics = compute_metrics(all_y_true, all_y_pred)
    pooled_cis = bootstrap_ci(all_y_true, all_y_pred)

    pooled_row = {'Database': 'Pooled (5 DB)', 'N': len(all_y_true)}
    for metric_name in ['Accuracy', 'Precision', 'Recall', 'F1-Score', 'Kappa']:
        val = pooled_metrics[metric_name]
        lo, hi = pooled_cis[metric_name]
        if metric_name == 'Kappa':
            pooled_row[metric_name] = f"{val:.3f}"
            pooled_row[f"{metric_name} 95% CI"] = f"[{lo:.3f}, {hi:.3f}]"
        else:
            pooled_row[metric_name] = f"{val*100:.1f}%"
            pooled_row[f"{metric_name} 95% CI"] = f"[{lo*100:.1f}%, {hi*100:.1f}%]"
    results.append(pooled_row)

    # Display
    results_df = pd.DataFrame(results)
    print("\n=== Supplementary Table S1: Per-Database MLM Performance ===\n")
    print(results_df.to_string(index=False))

    # Save
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_path = os.path.join(OUTPUT_DIR, 'Supplementary_Table_S1_reproduced.xlsx')
    results_df.to_excel(output_path, index=False)
    print(f"\nSaved to: {output_path}")


if __name__ == '__main__':
    main()
