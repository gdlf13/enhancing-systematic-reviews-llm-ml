"""
03_reproduce_holdout_split.py
==============================
Reproduces the 90/10 hold-out split and class distribution analysis
(Comments 1 and 5 response).

Demonstrates:
- Original class distribution: 139 health-related (20%) vs 556 not (80%)
- Hold-out split: train N=625 (125 pos / 500 neg), test N=70 (14 pos / 56 neg)
- SMOTE effect: training set balanced to 500/500 (375 synthetic positives)

Usage (from repo root):
    python code/03_reproduce_holdout_split.py

Input files (expected in data/ml_training/):
    - WoS_health_revised_MO.xlsx
"""

import os
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


def main():
    repo_root = os.path.join(os.path.dirname(__file__), '..')
    data_path = os.path.join(
        repo_root, 'data', 'ml_training',
        'WoS_health_revised_MO.xlsx'
    )

    wos = pd.read_excel(data_path)

    # The Human Reviewer labels are in column 'Unnamed: 4' (header row is row 0)
    labels = wos.iloc[1:, 4]  # skip header row "Mig Review"

    print("=" * 60)
    print("WEB OF SCIENCE CLASS DISTRIBUTION AND HOLD-OUT SPLIT")
    print("=" * 60)

    # Original distribution
    health = (labels == 'Health related').sum()
    not_health = (labels == 'Not health related').sum()
    total = health + not_health

    print(f"\n--- Original Class Distribution ---")
    print(f"  Total records: {total}")
    print(f"  Health related (positive):     {health} ({100*health/total:.1f}%)")
    print(f"  Not health related (negative): {not_health} ({100*not_health/total:.1f}%)")
    print(f"  Imbalance ratio: 1:{not_health/health:.1f}")

    # Encode labels
    y = labels.map(lambda x: 1 if x == 'Health related' else 0).values
    X = np.arange(len(y))  # placeholder features (split is label-dependent only)

    # Reproduce the exact split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.1, random_state=42
    )

    print(f"\n--- Hold-Out Split (test_size=0.1, random_state=42) ---")
    print(f"  Training set: N={len(y_train)}")
    print(f"    Positive (health):     {y_train.sum()} ({100*y_train.sum()/len(y_train):.1f}%)")
    print(f"    Negative (not health): {(y_train==0).sum()} ({100*(y_train==0).sum()/len(y_train):.1f}%)")
    print(f"  Test set: N={len(y_test)}")
    print(f"    Positive (health):     {y_test.sum()} ({100*y_test.sum()/len(y_test):.1f}%)")
    print(f"    Negative (not health): {(y_test==0).sum()} ({100*(y_test==0).sum()/len(y_test):.1f}%)")

    # SMOTE effect (sampling_strategy='auto' equalises to majority)
    n_neg_train = (y_train == 0).sum()
    n_pos_train = y_train.sum()
    n_synthetic = n_neg_train - n_pos_train

    print(f"\n--- SMOTE Effect (sampling_strategy='auto') ---")
    print(f"  Before SMOTE: {n_pos_train} positive, {n_neg_train} negative")
    print(f"  SMOTE generates: {n_synthetic} synthetic positive samples")
    print(f"  After SMOTE: {n_neg_train} positive, {n_neg_train} negative (balanced)")
    print(f"\n  Note: SMOTE is applied ONLY to the training partition.")
    print(f"  The test set (N={len(y_test)}) is never exposed to synthetic samples.")


if __name__ == '__main__':
    main()
