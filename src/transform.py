import os
import pandas as pd

def transform_data(input_path, output_path):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    df = pd.read_csv(input_path)
    
    # Extract date portion (YYYY-MM-DD)
    df['date'] = pd.to_datetime(df['timestamp']).dt.strftime('%Y-%m-%d')
    
    df.to_csv(output_path, index=False)

if __name__ == "__main__":
    transform_data("data/clean/events.csv", "data/transformed/events.csv")
