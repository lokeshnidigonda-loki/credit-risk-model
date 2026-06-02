# 📊 Credit Risk Analytics Dashboard

An end-to-end Machine Learning deployment pipeline designed to calculate financial credit default probabilities and assess lending risk. This platform integrates a robust Python scikit-learn predictive engine with a highly polished, responsive glassmorphism web analytics interface.

## 🛠️ Core Tech Stack & Engineering Highlights
* **Machine Learning Pipeline:** Scikit-Learn (Decision Tree Classifier), Pandas, NumPy, and Joblib for robust, automated serialization.
* **Web Deployment Framework:** Flask REST API backend structuring clean, secure communication vectors with the client layer.
* **Automated Software Quality Assurance:** Full test coverage validation engine engineered strictly via **Pytest**.
* **Modern UI/UX Interface:** Translucent dark-themed glassmorphism front-end styled via custom CSS3 backdrop filters and dynamic typography layers.

---

## 📈 System Architecture & Workflows

1. **Data Gathering & Mapping:** Cleans and processes key borrower risk metrics (`Age`, `Income`, `LoanAmount`, and `CreditScore`) directly out of flat storage matrices (`data/credit_data.csv`).
2. **Predictive Analytics Optimization:** Splitting historical operational metrics across a stratified train-test boundary to evaluate potential loss vectors before capital allocation.
3. **Automated Unit Testing Validation:** A test execution block enforces operational safety standards across core code logic blocks using `pytest`.
4. **Dynamic Risk-Glow Signaling Engine:** The user-facing page features dynamic lighting filters. If the Python backend predicts a sound investment, the screen lights up in a vibrant **Neon Green (Low Risk)**. If it surfaces a default pattern, it flashes a **Neon Red (High Risk)** indicator.

---

## ⚡ Automated Test Verification Suite
To verify the system's runtime stability and prediction logic integrity before local deployment, run the integrated testing modules:

```bash
python -m pytest -v test_model.py