# Enhancing Systematic Reviews: Integrating LLM's, Prompt Engineering and Machine Learning for Scholarly Analysis

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.15291559.svg)](https://doi.org/10.5281/zenodo.15291559)


## Project Title

Enhancing Systematic Reviews: Integrating LLM's, Prompt Engineering and Machine Learning for Scholarly Analysis

## Short Description

This repository contains all data, code, prompts, and documentation necessary to ensure full transparency and reproducibility of the results described in the associated Q1 journal article. All materials are structured according to open science best practices.

## Repository Structure

```
project-root/
│   README.md
│   LICENSE
│   requirements.txt
│
├── data/
│   ├── raw/           # Original datasets (ACM, Arxiv, IEEE, PubMed, Scopus, etc.)
│   ├── ml_training/   # Final dataset(s) used for ML model training
│   └── predictions/   # Outputs of model predictions (e.g., *_predictions.csv)
├── models/            # Trained ML models (e.g., .pkl, .pt), scripts for training/evaluation
├── prompts/           # All prompts used in the study (.md, .txt, .docx)
├── code/              # Main scripts for analysis, data prep, model training (to be added)
├── docs/              # Extra documentation, methodology, process notes
```

- **data/raw/**: All original, fully anonymized datasets (CSV format). No personal data included. If access is restricted, see below.
- **data/ml_training/**: Final dataset(s) used for ML model training.
- **data/predictions/**: Outputs of model predictions, for reproducibility and audit.
- **models/**: Only trained ML models and training/evaluation scripts.
- **prompts/**: All prompts used for LLMs or annotation, in markdown for transparency.
- **code/**: Main Python scripts for analysis, data processing, and model training.
- **docs/**: Additional documentation, methodology, or process descriptions.

## Reproducing the Analysis

1. Clone the repository:

   ```bash
   git clone [URL do projeto]
   cd [nome-da-pasta]
   ```

2. Activate the conda environment:

   ```bash
   conda activate plots
   ```

3. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Place the datasets in the correct subfolders under `data/` as described above. Place all prompts in `prompts/` as markdown files. Place trained models in `models/`.

5. Run the main analysis script (to be provided in `code/`):

   ```bash
   python code/main_analysis.py
   ```

6. For full reproducibility, follow any additional instructions in `docs/` or in the script headers.

## Licensing

- **Code**: MIT License (see LICENSE file)
- **Data & Documentation**: CC BY 4.0 (Creative Commons Attribution). See [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

## Citation

If you use this repository, please cite as:

> Oliveira, M. et al. (2025). Enhancing Systematic Reviews: Integrating LLM's, Prompt Engineering and Machine Learning for Scholarly Analysis. Zenodo. https://doi.org/DOI_PLACEHOLDER

## Ethics & Privacy

- All datasets are fully anonymized and irreversibly de-identified.
- No personal data is present in any shared files.
- Any restricted datasets are documented below.
- All scripts prioritize reproducibility and privacy compliance (GDPR, HIPAA).

### Restricted Data

If any dataset cannot be shared publicly, instructions for access will be provided in the data/ folder and documented here.

## Zenodo DOI

This repository is configured for Zenodo integration. After the first stable release (v1.0), a DOI will be minted and the badge above will be updated.

## Good Practices

- No file exceeds 100MB (use Git LFS if needed).
- All file/folder names are in English and snake_case.
- Scripts are documented and modular.
- Reproducibility is prioritized over output storage.
- All package installations must be done inside the `conda` environment `plots`.
- All prompts are provided in markdown for transparency and reuse.
- Datasets, prompts, and models are strictly separated for auditability.

---

For questions or requests, open an issue or contact the corresponding author.
