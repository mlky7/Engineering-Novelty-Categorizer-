# Patent Novelty Classification using Machine Learning

## 1. Project Aim

The aim of this project is to build a machine learning model that can automatically classify patent claim text into different novelty tiers.

The system analyzes the textual description of a patent claim and predicts the *level of novelty* using a trained machine learning model.

This helps in *automating patent analysis*, reducing manual effort in determining how novel or unique a patent claim is.

---

# 2. Dataset Description

The dataset used in this project is:
It contains *200 rows and 2 columns*.

## Columns in Dataset

| Column Name | Description |
|-------------|-------------|
| clean_text | Preprocessed patent claim text |
| novelty tier | Label representing the novelty category |

### Example Data

| clean_text | novelty tier |
|------------|--------------|
| logaided automatic query expansion approach... | 1 |
| power management deep discharge protection... | 0 |
| remote monitoring dynamic document management | 0 |

---

# 3. Project Input and Output

## Input
The input to the model is *Patent Claim Text*.
Example:
## Output
The output of the model is a *Predicted Novelty Tier*.
Example:
This means the patent claim belongs to *novelty category 2*.

---

# 4. Technologies and Libraries Used

The project is implemented using Python and the following libraries:

- *pandas* – for dataset loading and processing
- *scikit-learn* – for machine learning algorithms
- *joblib* – for saving and loading trained models

---

# 5. Machine Learning Algorithm Used

This project uses the *Random Forest Classifier*.

Random Forest is an *ensemble machine learning algorithm* that builds multiple decision trees and combines their predictions to produce a final result.

### Advantages of Random Forest

- Handles complex data patterns
- Reduces overfitting
- Provides better prediction accuracy than a single decision tree

---

# 6. Text Processing Technique

Since machine learning models cannot understand raw text, the patent claim text is converted into numerical features using *TF-IDF (Term Frequency – Inverse Document Frequency)*.

TF-IDF assigns importance scores to words based on:

- Frequency in the document
- Frequency across the dataset

This helps identify important words for classification.

---

# 7. Training Process (train_model.py)

The file *train_model.py* performs the model training.

### Steps performed in this script

1. Load the dataset using pandas  
2. Separate input text and output labels  
3. Convert text into numerical vectors using TF-IDF  
4. Split dataset into training and testing sets  
5. Train the Random Forest classifier  
6. Evaluate the model using accuracy score  
7. Save the trained model and vectorizer  

This script is responsible for *building the machine learning model*.

---

# 8. Prediction Script (predict.py)

The file *predict.py* is used to test the trained model.

### Steps performed

1. Load the saved Random Forest model  
2. Load the saved TF-IDF vectorizer  
3. Convert new input text into vector form  
4. Predict the novelty tier using the trained model  
5. Display the prediction result  

This script allows the system to *predict novelty tier for new patent claims*.

---

# 9. Saved Model

After training, the model is stored inside the folder:
This folder contains:
### rf_model.pkl
Stores the *trained Random Forest model*.

### tfidf_vectorizer.pkl
Stores the *TF-IDF vectorizer used to convert text into numerical features*.

Saving the model allows us to *reuse it without retraining*.

---

# 10. Model Performance

After training the model, the achieved accuracy was:
The classification report includes:

- Precision
- Recall
- F1-score

These metrics help evaluate the *performance of the machine learning model*.

---

# 11. Project Workflow
Dataset ↓ Text Vectorization (TF-IDF) ↓ Train/Test Split ↓ Model Training (Random Forest) ↓ Model Evaluation ↓ Save Model ↓ Prediction
# 12. Conclusion

This project demonstrates how machine learning can be used to *classify patent claims based on their novelty*.

The system processes textual patent data, converts it into numerical features, trains a machine learning model, and predicts the novelty category of new patent claims.

### Future Improvements

- Use larger datasets
- Apply advanced NLP models
- Improve model accuracy