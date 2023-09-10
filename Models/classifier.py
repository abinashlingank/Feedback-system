import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split 
from sklearn.svm import SVC
import joblib

loaded_classifier = joblib.load('svm_classifier.pkl')

tfidf_vectorizer = joblib.load('tfidf_vectorizer.pkl')

# Use the loaded classifier to make predictions
x = ["US says India is disappointed Xi and Putin aren't attending G-20, but Biden sees it as an opportunity"]
x_tfidf = tfidf_vectorizer.transform(x)
y_pred = loaded_classifier.predict(x_tfidf)


print(f"Predicted Department for 'x': {y_pred[0]}")