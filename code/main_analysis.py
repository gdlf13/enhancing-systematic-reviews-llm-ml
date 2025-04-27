"""
Main analysis script for reproducing the results of:
Enhancing Systematic Reviews: Integrating LLM's, Prompt Engineering and Machine Learning for Scholarly Analysis

This script loads the ML training dataset, applies the trained model, and generates predictions for evaluation.

Requirements: see ../../requirements.txt
Activate the conda environment 'plots' before running.
"""
import pandas as pd
import joblib
import os

DATA_TRAIN = os.path.join('..', 'data', 'ml_training', 'ml_training_dataset.csv')  # Update filename as needed
MODEL_PATH = os.path.join('..', 'models', 'final_model.pkl')  # Update filename as needed
PREDICTIONS_PATH = os.path.join('..', 'data', 'predictions', 'model_predictions.csv')

# Load training data
df = pd.read_csv(DATA_TRAIN)

# Load trained model
model = joblib.load(MODEL_PATH)

# Predict (assuming binary classification, adapt as needed)
preds = model.predict(df.drop(columns=['target']))

# Save predictions
output = df.copy()
output['predicted_label'] = preds
output.to_csv(PREDICTIONS_PATH, index=False)

print(f"Predictions saved to {PREDICTIONS_PATH}")
