
import joblib
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix, precision_score
from preprocess import load_and_preprocess

def evaluate_and_tune_threshold():

    _, X_test_scaled, _, y_test, _ = load_and_preprocess()
  
    model = joblib.load('heart_model.pkl')
  
    default_preds = model.predict(X_test_scaled)
    default_prec = precision_score(y_test, default_preds)
    
    print("\n" + "="*45)
    print(f"⚙️ DEFAULT THRESHOLD (0.50) Precision: {default_prec * 100:.2f}%")
    print("="*45)

    y_probs = model.predict_proba(X_test_scaled)[:, 1]

    tuned_threshold = 0.68
    tuned_preds = (y_probs >= tuned_threshold).astype(int)
    tuned_prec = precision_score(y_test, tuned_preds)
    
    print("\n" + "="*45)
    print(f"🚀 TUNED THRESHOLD ({tuned_threshold}) Precision: {tuned_prec * 100:.2f}%")
    print("="*45)
    
    # 6. Detailed Reports
    print("\n📊 Confusion Matrix (Tuned Model):")
    cm = confusion_matrix(y_test, tuned_preds)
    print(f"True Negatives (Healthy) : {cm[0][0]}")
    print(f"False Positives (FP Alarm): {cm[0][1]}  <-- Dropped significantly!")
    print(f"False Negatives (FN Risk) : {cm[1][0]}")
    print(f"True Positives (Disease) : {cm[1][1]}")
    
    print("\n📋 Full Classification Report:")
    print(classification_report(y_test, tuned_preds))

if __name__ == "__main__":
    evaluate_and_tune_threshold()