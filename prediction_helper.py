import joblib
import numpy as np

def predict_risk(age, income, loan_amount, credit_score):
    try:
        # Load the saved model file cleanly
        model = joblib.load('models/credit_model.pkl')
        
        # Format the features exactly as expected by Scikit-learn
        features = np.array([[age, income, loan_amount, credit_score]])
        prediction = model.predict(features)
        
        if prediction[0] == 1:
            return "High Risk (Likely to Default)"
        else:
            return "Low Risk (Safe to Approve)"
    except FileNotFoundError:
        return "Error: Model file not found. Please run train_model.py first."