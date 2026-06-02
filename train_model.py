import pandas as pd
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

def train_and_save():
    # Automatically create the models folder if it's missing
    if not os.path.exists('models'):
        os.makedirs('models')
        
    # 1. Load Data
    df = pd.read_csv('data/credit_data.csv')
    
    # 2. Extract Features matching your CSV columns exactly
    X = df[['Age', 'Income', 'LoanAmount', 'CreditScore']]
    
    # Map 'Low' risk to 0 and 'High' risk to 1 for the Machine Learning model
    y = df['Risk'].map({'Low': 0, 'High': 1})
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # 3. Train Model
    model = DecisionTreeClassifier(random_state=42)
    model.fit(X_train, y_train)
    
    # 4. Evaluate
    predictions = model.predict(X_test)
    acc = accuracy_score(y_test, predictions)
    print(f"🎉 Model trained successfully! Accuracy: {acc * 100:.2f}%")
    
    # 5. Save the model
    joblib.dump(model, 'models/credit_model.pkl')
    print("💾 Saved model to: models/credit_model.pkl")

if __name__ == "__main__":
    train_and_save()