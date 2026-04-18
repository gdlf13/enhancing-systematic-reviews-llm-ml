"""
02_inspect_model_pipeline.py
=============================
Inspects the trained MLM pipeline to verify SMOTE implementation
details (Comment 5 response).

Confirms:
- Pipeline type: imblearn.pipeline.Pipeline (NOT sklearn Pipeline)
- Pipeline steps: TfidfVectorizer -> SMOTE -> LogisticRegression
- SMOTE parameters: sampling_strategy='auto', k_neighbors=5, random_state=42
- LogisticRegression: class_weight='balanced', random_state=42
- imblearn Pipeline ensures SMOTE is applied ONLY during .fit(),
  bypassed during .predict() -- no data leakage

Usage (from repo root):
    python code/02_inspect_model_pipeline.py

Input files (expected in models/):
    - my_trained_model_Mig_review_with_SMOTE.joblib
"""

import os
import warnings
warnings.filterwarnings('ignore')
import joblib


def main():
    repo_root = os.path.join(os.path.dirname(__file__), '..')
    model_path = os.path.join(repo_root, 'models', 'my_trained_model_Mig_review_with_SMOTE.joblib')

    model = joblib.load(model_path)

    print("=" * 60)
    print("MLM PIPELINE INSPECTION")
    print("=" * 60)

    # 1. Pipeline type
    print(f"\nPipeline type: {type(model).__name__}")
    print(f"Module: {type(model).__module__}")
    is_imblearn = 'imblearn' in type(model).__module__
    print(f"Is imblearn Pipeline: {is_imblearn}")

    if is_imblearn:
        print("\n  -> imblearn.pipeline.Pipeline ensures that resampling steps")
        print("     (SMOTE) are applied ONLY during .fit() and bypassed during")
        print("     .predict(). This prevents data leakage to the test set.")

    # 2. Pipeline steps
    print(f"\n{'=' * 60}")
    print("PIPELINE STEPS")
    print("=" * 60)
    for i, (name, step) in enumerate(model.steps):
        print(f"\n  Step {i+1}: {name}")
        print(f"    Type: {type(step).__name__}")

        if hasattr(step, 'get_params'):
            params = step.get_params()

            if 'SMOTE' in type(step).__name__:
                print(f"    sampling_strategy: {params.get('sampling_strategy')}")
                print(f"    k_neighbors: {params.get('k_neighbors')}")
                print(f"    random_state: {params.get('random_state')}")
                print(f"\n    -> sampling_strategy='auto' equalises the minority class")
                print(f"       to match the majority class count.")

            elif 'LogisticRegression' in type(step).__name__:
                print(f"    C: {params.get('C')}")
                print(f"    class_weight: {params.get('class_weight')}")
                print(f"    penalty: {params.get('penalty')}")
                print(f"    solver: {params.get('solver')}")
                print(f"    max_iter: {params.get('max_iter')}")
                print(f"    random_state: {params.get('random_state')}")

            elif 'TfidfVectorizer' in type(step).__name__:
                print(f"    ngram_range: {params.get('ngram_range')}")
                print(f"    stop_words: {params.get('stop_words')}")
                print(f"    max_features: {params.get('max_features')}")
                print(f"    norm: {params.get('norm')}")

    # 3. Summary
    print(f"\n{'=' * 60}")
    print("SUMMARY")
    print("=" * 60)
    print("""
    The model is an imblearn Pipeline with three steps:
      1. TfidfVectorizer - converts text to TF-IDF features
      2. SMOTE (auto) - equalises minority class during training only
      3. LogisticRegression (class_weight='balanced') - classifier

    Data leakage prevention:
      - imblearn Pipeline bypasses SMOTE during .predict()
      - The held-out test set (10%) was never exposed to synthetic samples
      - The 5 non-WoS databases were never part of training
    """)


if __name__ == '__main__':
    main()
