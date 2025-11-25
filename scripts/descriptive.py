import pandas as pd

def get_headline_stats(df, column='headline'):
    """Stats for text lengths."""
    df['headline_length'] = df[column].astype(str).apply(len)
    headline_lengths = df['headline_length']
    stats = headline_lengths.describe()
    return stats, headline_lengths

def analyze_publishers(df, column='publisher', top_n=10):
    """Return publishers and counts separately"""
    counts = df[column].value_counts().head(top_n)
    publishers = counts.index.tolist()
    values = counts.values.tolist()
    return publishers, values

def analyze_stocks(df, column='stock', top_n=10):
    """
    New: Counts which stocks are mentioned most frequently.
    """
    return df[column].value_counts().head(top_n)