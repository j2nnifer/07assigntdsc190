import os
import pandas as pd

def clean_data(input_path, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df = pd.read_csv(input_path)
    
    # Drop rows with any missing fields
    df = df.dropna()
    
    # Enforce positive duration_seconds
    df = df[df['duration_seconds'] > 0]
    
    # Normalize timestamp to ISO 8601 (YYYY-MM-DDTHH:MM:SS)
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df = df.dropna(subset=['timestamp'])
    df['timestamp'] = df['timestamp'].dt.strftime('%Y-%m-%dT%H:%M:%S')
    
    df.to_csv(output_path, index=False)
    print(f"Cleaned records: {len(df)}")

if __name__ == "__main__":
    clean_data("data/raw/events.csv", "data/clean/events.csv")
