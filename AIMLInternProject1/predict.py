import joblib

model = joblib.load("saved_model/rf_model.pkl")
vectorizer = joblib.load("saved_model/tfidf_vectorizer.pkl")
sample = ["cloud based system for remote monitoring"]
sample_vec = vectorizer.transform(sample)
prediction = model.predict(sample_vec)
print("Predicted Novelty Tier:", prediction[0])