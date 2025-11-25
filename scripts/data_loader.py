import pandas as pd
import os

def load_data(file_path):
    """
    Loads the CSV data, handles the specific date format with timezone,
    and ensures correct column names exist.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} was not found.")
    
    # Load data
    df = pd.read_csv(file_path)
    
    # Check for required columns
    required_columns = ['headline', 'date', 'publisher', 'stock']
    if not all(col in df.columns for col in required_columns):
        missing = [col for col in required_columns if col not in df.columns]
        print(f"Warning: Missing columns {missing}")
    
    # Convert date (Handles "2020-06-05 10:30:54-04:00")
    # utc=True converts the offset (-04:00) to UTC time for consistent analysis
    if 'date' in df.columns:
        df['date'] = pd.to_datetime(df['date'], errors='coerce', utc=True)
        
    return df