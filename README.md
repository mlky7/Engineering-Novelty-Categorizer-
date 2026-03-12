# Engineering Novelty Categorizer

**SDG Goal: SDG 9 – Industry, Innovation and Infrastructure**

This project builds a machine learning system to classify engineering patent documents into **novelty tiers (0–3)** based on their textual descriptions.
The goal is to assist reviewers and researchers by automatically identifying the level of innovation in hardware-related patents.

The project uses the **Harvard USPTO Patent Dataset (HUPD)** from Hugging Face and focuses on patents from the year **2018**.
A full data engineering pipeline, feature extraction, model training, fine-tuning, and false positive analysis were implemented.

---

## Project Objectives

* Extract hardware-related patents from raw JSON patent files
* Clean and preprocess patent text data
* Assign novelty scores and novelty tiers
* Train multiple machine learning models
* Fine-tune models to reduce false positives
* Compare models using Macro F1 score
* Perform false positive analysis for deeper evaluation

---

## Dataset

**Source:**
HUPD – Harvard USPTO Patent Dataset
[https://huggingface.co/datasets/HUPD/hupd](https://huggingface.co/datasets/HUPD/hupd)

---

## Libraries Used

pandas, numpy, matplotlib, seaborn, scikit-learn, xgboost, json, os, re, nltk, tqdm, joblib

---

## Repository Structure

```
├── data_processed/
│   Processed datasets generated during data engineering
│   Includes filtered, cleaned, and balanced patent datasets
│
├── notebooks/
│   Contains individual notebooks from team members
│   Used for experiments, testing, and intermediate work
│
├── visualization/
│   Contains plots, charts, and analysis visuals
│
├── data_engineering.ipynb
│   Main data engineering pipeline
│
├── model_training.ipynb
│   Initial model training
│
├── model_finetuning.ipynb
│   Hyperparameter tuning using GridSearch
│
├── false_positive_analysis.ipynb
│   Analysis of incorrect predictions
│
└── README.md
```

---
