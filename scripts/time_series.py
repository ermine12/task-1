import pandas as pd

def analyze_publication_frequency(df, date_col='date'):
    """
    Analyzes publication frequency over time.
    """
    # Ensure date is the index for resampling
    temp_df = df.set_index(date_col)
    
    # Resample by Day ('D') to count articles per day
    daily_counts = temp_df.resample('D').size()
    
    # Analysis of publishing times (Hour of day)
    hourly_counts = df[date_col].dt.hour.value_counts().sort_index()
    
    return daily_counts, hourly_counts