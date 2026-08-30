import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import joblib

def load_and_preprocess():
    df = pd.read_csv("heart_encrypted.csv")
    print(f"📂 Encrypted Dataset Loaded! Total rows: {len(df)}")
    X = df.drop(columns=['encrypted_patient_id', 'encrypted_patient_name', 'target'])
    y = df['target']
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    joblib.dump(scaler, 'scaler.pkl')
    print("✅ Feature Scaling Complete! Saved 'scaler.pkl'")
    
    print(f"📊 Training Samples: {X_train_scaled.shape[0]}, Testing Samples: {X_test_scaled.shape[0]}")
    return X_train_scaled, X_test_scaled, y_train, y_test, X.columns

if __name__ == "__main__":
    load_and_preprocess()