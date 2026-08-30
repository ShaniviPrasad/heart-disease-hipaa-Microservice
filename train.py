
import pandas as pd
import joblib
from sklearn.linear_model import LogisticRegression
from preprocess import load_and_preprocess

def train_heart_model():
    X_train_scaled, X_test_scaled, y_train, y_test, feature_names = load_and_preprocess()
    
    print("\n🤖 Training Logistic Regression Model with L2 Regularization...")
    model = LogisticRegression(C=0.1, max_iter=1000, random_state=42)
    model.fit(X_train_scaled, y_train)
    train_acc = model.score(X_train_scaled, y_train)
    test_acc = model.score(X_test_scaled, y_test)
    
    print(f"📈 Training Accuracy: {train_acc * 100:.2f}%")
    print(f"📊 Testing Accuracy : {test_acc * 100:.2f}%")
 
    print("\n🔍 Feature Weights (Coefficients) learned by Model:")
    coef_df = pd.DataFrame({
        'Feature': feature_names,
        'Weight': model.coef_[0]
    }).sort_values(by='Weight', ascending=False)
    
    print(coef_df)
    joblib.dump(model, 'heart_model.pkl')
    print("\n✅ Trained Model Saved to 'heart_model.pkl'!")

if __name__ == "__main__":
    train_heart_model()