import pandas as pd
import numpy as np
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/heart-disease/processed.cleveland.data"
columns = ['age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 
           'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']
print("📥 Downloading Real UCI Heart Disease Dataset...")
df = pd.read_csv(url, names=columns, na_values="?")

df = df.dropna()

df['target'] = df['target'].apply(lambda x: 1 if x > 0 else 0)
np.random.seed(42)
df['patient_id'] = [f"PAT_{1000 + i}" for i in range(len(df))]
df['patient_name'] = [f"Patient_Record_{1000 + i}" for i in range(len(df))]

df = df[['patient_id', 'patient_name'] + columns]

df.to_csv("heart_raw.csv", index=False)
print(f"✅ Real Dataset Saved! Total Records: {len(df)} patients.")