from django.shortcuts import render
from .models import Review
import pickle
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import MinMaxScaler
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)

# Load your models
try:
    cv = pickle.load(open('Models/countVectorizer.pkl', 'rb'))
    scaler = pickle.load(open('Models/scaler.pkl', 'rb'))
    model_rf = pickle.load(open('Models/model_rf.pkl', 'rb'))
except Exception as e:
    logging.error(f"Error loading models: {e}")

def analyze_review(request):
    if request.method == 'POST':
        review_text = request.POST.get('review_text')
        try:
            # Preprocess the review text
            review_vector = cv.transform([review_text]).toarray()
            logging.info(f"Review Vector: {review_vector}")
            review_scaled = scaler.transform(review_vector)
            logging.info(f"Scaled Review: {review_scaled}")
            prediction = model_rf.predict(review_scaled)
            logging.info(f"Raw Prediction: {prediction}")
            # Check if prediction is a probability or class label
            if hasattr(model_rf, "predict_proba"):
                prediction_proba = model_rf.predict_proba(review_scaled)
                logging.info(f"Prediction Probabilities: {prediction_proba}")
        except Exception as e:
            logging.error(f"Error during prediction: {e}")
            prediction = ["Error"]
        return render(request, 'result.html', {'prediction': prediction[0]})
    return render(request, 'analyze.html')
