import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics import accuracy_score, classification_report
import joblib

# 1. Load Dataset
data = pd.read_csv("RandomForestDataset.csv")

print("Dataset Shape:", data.shape)
print(data.head())

X = data["clean_text"]
y = data["novelty tier"]

vectorizer = TfidfVectorizer(
    stop_words="english",
    max_features=5000,
    ngram_range=(1,2)
)

X_vec = vectorizer.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(
    X_vec,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)


# 5. Train Random Forest Model
# ------------------------------------------------
model = RandomForestClassifier(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

model.fit(X_train, y_train)

# ------------------------------------------------
# 6. Make Predictions
# ------------------------------------------------
y_pred = model.predict(X_test)

# ------------------------------------------------
# 7. Evaluate Model
# ------------------------------------------------
accuracy = accuracy_score(y_test, y_pred)

print("\nModel Accuracy:", accuracy)
print("\nClassification Report:\n")
print(classification_report(y_test, y_pred))

# ------------------------------------------------
# 8. Save Model
# ------------------------------------------------
joblib.dump(model, "saved_model/rf_model.pkl")
joblib.dump(vectorizer, "saved_model/tfidf_vectorizer.pkl")

print("\nModel and Vectorizer Saved Successfully.")
