# 🧬 OncoTarget Mining

### Computational Mining of Public Transcriptomic Data for Immune-Evasion Candidate Prioritization

OncoTarget Mining is a computational pipeline that combines single-cell RNA sequencing (scRNA-seq), supervised machine learning, and public transcriptomic datasets to explore immune-response profiles and prioritize immune-evasion candidates.

## 🔬 Overview

The pipeline uses a PBMC 3k reference atlas to derive cytotoxic transcriptional signatures and train a Random Forest classifier. The resulting model is applied to independent public transcriptomic datasets retrieved from ENA / NCBI / SRA.

The project is designed as a reproducible proof-of-concept for transforming heterogeneous public transcriptomic data into computationally testable biological hypotheses.

## 🧠 Pipeline

```text
PBMC 3k scRNA-seq
        │
        ▼
Cytotoxicity signatures
NKG7 · GZMA · CCL5 · GNLY · PRF1
        │
        ▼
Random Forest Classifier
        │
        ▼
Public Transcriptomic Datasets
ENA / NCBI / SRA
        │
        ▼
Functional Stratification
        │
        ▼
Immune-Evasion Candidate Prioritization
        │
        ▼
CD274 / PD-L1
```

## 📊 Main Result

### PRJEB108071

The primary cohort contained 46 samples.

| Predicted profile | Samples | Percentage |
|---|---:|---:|
| Moderate Response | 32 | 69.57% |
| Low / Immunosuppressive | 14 | 30.43% |
| Total | 46 | 100% |

Among the evaluated immune-evasion candidates:

| Candidate | Δ Expression |
|---|---:|
| CD274 (PD-L1) | +0.042990 |
| PDCD1 | -0.209052 |
| TIGIT | -0.229288 |
| HAVCR2 | -0.503626 |

CD274 was the only candidate with a positive expression delta within the evaluated panel and was therefore computationally prioritized for downstream validation.

This is a computational prioritization, not a demonstration of causality, therapeutic efficacy, or clinical utility.

## 🛠️ Technologies

- Python
- Scanpy / AnnData
- Pandas / NumPy
- Scikit-learn
- Joblib
- ENA / NCBI / SRA resources
- Streamlit / interactive visualization components

## 📁 Repository Structure

```text
onco-target-scRNA/
│
├── 01_onco_target_analysis.ipynb
├── 01_fetch_genomic_metadata.py
├── onco_target_random_forest.joblib
├── model_features.json
├── top10_oncotarget_genes.json
├── onco_targets_priorizados_evasion.csv
├── mineria_multi_bioproject_resumen.csv
├── reporte_oncotargets_pbmc3k.csv
├── Informe_Tecnico_OncoTarget_Mining.md
├── requirements.txt
├── README.md
└── LICENSE
```

## 📚 Documentation

- [Project Overview](PROJECT_OVERVIEW.md)
- [Scientific / Executive Report](Informe_Tecnico_OncoTarget_Mining.md)

The Project Overview explains the questions, objectives, scope, results, limitations, and potential R&D relevance of the project.

## 🚀 Reproducibility

```bash
git clone https://github.com/GarP23/onco-target-scRNA.git
cd onco-target-scRNA
python -m venv .venv
```

Linux / macOS:

```bash
source .venv/bin/activate
```

Windows:

```bash
.venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

The main analysis is documented in:

```text
01_onco_target_analysis.ipynb
```

## ⚠️ Scientific Scope

OncoTarget Mining is a computational research and data-mining project.

It does not provide medical diagnosis, patient prognosis, therapeutic recommendations, clinical biomarkers, or proof of causal biological mechanisms.

The results are intended to generate hypotheses that require independent computational and experimental validation.

## 👤 Author

GarP23

Repository:
https://github.com/GarP23/onco-target-scRNA

## 📜 License

MIT License
