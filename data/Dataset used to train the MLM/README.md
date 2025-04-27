# Dataset Used to Train the Machine Learning Model (MLM)

This folder contains the dataset(s) specifically used to train the machine learning models developed and evaluated in this project.

## Contents

- One or more CSV files with fully anonymized, preprocessed data ready for ML training.
- Each file should be clearly named (e.g., `mlm_training_data.csv`).

## Guidelines

- **Anonymization:** All data must be fully anonymized and compliant with GDPR and HIPAA. No direct or indirect patient identifiers are allowed.
- **Format:** Use CSV format. Include a header row with clear, English column names.
- **Documentation:** For each file, document:
  - Source and provenance (e.g., which raw datasets were used)
  - Preprocessing steps (e.g., cleaning, feature engineering)
  - Target variable/label definition
  - Description of each feature/column
- **Versioning:** If the dataset is updated, increment the file version and document the changes in this README.

## Example Entry

| Column Name      | Description                       |
|------------------|-----------------------------------|
| title            | Title of the publication          |
| abstract         | Abstract text                     |
| year             | Year of publication               |
| label            | Target variable (e.g., 1=Health)  |

## Usage

- Use the files in `../ml_training/` as input for training scripts in the `code/` folder.
- Only processed, anonymized data ready for ML should be placed in `ml_training/`.

## Compliance & Ethics

- Ensure all data complies with privacy and ethical guidelines.
- If any uncertainty exists regarding data compliance, request clarification before use.

---
For questions, contact the project maintainers or open an issue in the repository.
