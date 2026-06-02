from flask import Flask, render_template, request
from prediction_helper import predict_risk

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('correct.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Extract inputs submitted from your HTML web page form
        age = float(request.form['age'])
        income = float(request.form['income'])
        loan_amount = float(request.form['loan_amount'])
        credit_score = float(request.form['credit_score'])
        
        # Run prediction via our helper script
        result = predict_risk(age, income, loan_amount, credit_score)
        
        return render_template('correct.html', prediction_text=f"Risk Assessment: {result}")
    except Exception as e:
        return render_template('correct.html', prediction_text=f"Error processing details: {str(e)}")

if __name__ == '__main__':
    app.run(debug=True)