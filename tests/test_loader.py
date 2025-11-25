import sys
import os
import pandas as pd
import pytest

# Add the src directory to the path so we can import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../scripts')))

from descriptive import get_headline_stats

# Removed duplicate function definition since it's imported

def test_get_headline_stats():
    # Sample data
    data = {
        "headline": ["This is a headline", "This is a much longer headline for testing"]
    }
    df = pd.DataFrame(data)

    # Run the function
    stats, _ = get_headline_stats(df)

    # Assertions (Checks)
    # Count should be 2 because we have 2 rows
    assert stats['count'] == 2
    # Max length should be len('This is a much longer headline for testing') = 42
    assert stats['max'] == 42