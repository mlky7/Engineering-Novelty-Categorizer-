
# Engineering Novelty Categorizer

The **Engineering Novelty Categorizer** is a machine learning system designed to automatically analyze hardware design descriptions and classify them into different **novelty tiers**. The goal of this project is to assist **intellectual property (IP) and legal reviewers** in quickly identifying how innovative a hardware design is, enabling faster evaluation and prioritization of potentially novel inventions.

This project aligns with **Sustainable Development Goal (SDG) 9: Industry, Innovation, and Infrastructure**, which focuses on fostering innovation and technological advancement.

## Project Overview

The system processes short **patent-style engineering descriptions** that represent hardware innovations. Each description is labeled with a **novelty tier**, indicating the level of innovation present in the design.

Rather than relying on complex deep learning architectures, the project implements a **simple and interpretable machine learning pipeline**. This approach ensures transparency and easier analysis of how models make their predictions.

## Methodology

The project follows a standard **Natural Language Processing (NLP) pipeline**:

1. **Text Preprocessing**

   * Cleaning and normalizing engineering descriptions
   * Removing unnecessary symbols and formatting inconsistencies

2. **Feature Extraction**

   * Converting text into numerical representations using **TF-IDF (Term Frequency–Inverse Document Frequency)**

3. **Model Training**

   * Training traditional machine learning classifiers including:

     * **K-Nearest Neighbors (KNN)**
     * **Decision Tree**
     * **Random Forest**

These models learn patterns in engineering terminology and design descriptions that correspond to different levels of innovation.

## Evaluation

To ensure fair evaluation across all novelty categories, the models are assessed using the **Macro-Averaged F1 Score**. This metric balances **precision and recall** for each class and is particularly useful when the dataset contains **imbalanced novelty tiers**.

## Outcome

The final system provides a **fast, interpretable, and efficient solution** for categorizing engineering design descriptions based on their level of novelty. This helps reviewers filter large volumes of design submissions and focus on the most innovative ideas.

---
