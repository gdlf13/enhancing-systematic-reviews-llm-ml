# Data

This folder and its subfolders contain all datasets used in the project. Strict separation is enforced for clarity and reproducibility.

## Structure

- `ml_training/`: All fully anonymized datasets used for ML training and analysis (e.g., ACM, Arxiv, IEEE, PubMed, Scopus). No personal data.
- `predictions/`: Outputs of model predictions for audit and reproduction.

## Usage
- Place each dataset in the correct subfolder.
- Ensure all data is anonymized and compliant with privacy regulations (GDPR, HIPAA).
- Document any access restrictions in a README in the relevant subfolder.

## Notes
- Do not store personal or sensitive data.
- If a dataset cannot be shared publicly, provide instructions for access and document this here.
