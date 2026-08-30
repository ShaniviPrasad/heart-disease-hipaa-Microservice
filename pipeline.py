import joblib
import numpy as np
from security import encrypt_data, decrypt_data

class SecureHeartDiseasePipeline:
    def __init__(self, model_path='heart_model.pkl', scaler_path='scaler.pkl'):
        self.model = joblib.load(model_path)
        self.scaler = joblib.load(scaler_path)
        self.threshold = 0.68  
        print("🚀 Secure Pipeline Initialized with High-Precision Model!")

    def predict_encrypted_patient(self, encrypted_payload):
        """
        Input: Encrypted Patient Data (JSON / Dict)
        Output: Encrypted Diagnostic Result Log
        """
        patient_id = decrypt_data(encrypted_payload['encrypted_patient_id'])
        patient_name = decrypt_data(encrypted_payload['encrypted_patient_name'])

        raw_features = encrypted_payload['clinical_features']
    
        scaled_features = self.scaler.transform([raw_features])

        prob_disease = self.model.predict_proba(scaled_features)[0][1]
        
        prediction = 1 if prob_disease >= self.threshold else 0
        risk_status = "HIGH RISK (Heart Disease Detected)" if prediction == 1 else "LOW RISK (Normal)"
    
        result_log = (
            f"Patient ID: {patient_id} | Name: {patient_name} | "
            f"Risk Score: {prob_disease * 100:.2f}% | Status: {risk_status}"
        )
        
        encrypted_log = encrypt_data(result_log)
        
        return {
            "decrypted_preview_for_doctor": result_log,
            "encrypted_log_for_database": encrypted_log
        }
if __name__ == "__main__":
    pipeline = SecureHeartDiseasePipeline()
    
    sample_encrypted_payload = {
        'encrypted_patient_id': encrypt_data("PAT_9901"),
        'encrypted_patient_name': encrypt_data("Rahul Verma"),
        'clinical_features': [63, 1, 3, 145, 233, 1, 2, 150, 0, 2.3, 3, 0, 2]
    }
    
    print("\n📩 Processing Encrypted Incoming Patient Payload...")
    output = pipeline.predict_encrypted_patient(sample_encrypted_payload)
    
    print("\n--- DOCTOR'S SECURE PREVIEW ---")
    print(output['decrypted_preview_for_doctor'])
    
    print("\n--- ENCRYPTED DATABASE LOG (AES-256) ---")
    print(output['encrypted_log_for_database'])