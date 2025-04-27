# Code

This folder contains all scripts necessary for data analysis, model training, and reproducibility of results for the project "Enhancing Systematic Reviews: Integrating LLM's, Prompt Engineering and Machine Learning for Scholarly Analysis".

## Contents

- `main_analysis.py`: Main entry point for reproducing the results. Loads the ML training dataset, applies the trained model, and generates predictions.
- Add any additional scripts for data cleaning, feature engineering, or evaluation here.

## Usage

1. Place the ML training dataset in `../data/ml_training/` and the trained model in `../models/`.
2. Activate the conda environment `plots`.
3. Install dependencies: `pip install -r ../requirements.txt`
4. Run the main script:

   ```bash
   python main_analysis.py
   ```

## Notes

- All scripts should be well documented and use English and snake_case for file names.
- For additional analyses, add new scripts and update this README accordingly.
