import pandas as pd
from security import encrypt_data, decrypt_data
def process_and_encrypt_dataset(input_file, output_file):
    df = pd.read_csv(input_file)
    print("📂 Original Data Loaded Successfully!")
    print("🔒 Encrypting Patient Identities (PHI)...")
    df['encrypted_patient_id'] = df['patient_id'].apply(lambda x: encrypt_data(str(x)))
    df['encrypted_patient_name'] = df['patient_name'].apply(lambda x: encrypt_data(str(x)))
    clean_df = df.drop(columns=['patient_id', 'patient_name'])
    clean_df.to_csv(output_file, index=False)
    print(f"✅ Encrypted Dataset Saved to '{output_file}'!")
if __name__ == "__main__":
    process_and_encrypt_dataset('heart_raw.csv', 'heart_encrypted.csv')