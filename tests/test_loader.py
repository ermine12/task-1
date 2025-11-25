import sys
import os
import pandas as pd
import pytest

# Add the src directory to the path so we can import modules
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from descriptive import get_headline_stats

def test_headline_stats():
    """
    Test if the headline statistics function calculates correctly.
    """
    # Create dummy data
    data = {
        'headline': ['Short headline', 'This is a much longer headline for testing'],
        'date': ['2020-01-01', '2020-01-02'],
        'publisher': ['Pub A', 'Pub B']
    }
    df = pd.DataFrame(data)
    
    # Run the function
    stats = get_headline_stats(df)
    
    # Assertions (Checks)
    # Count should be 2 because we have 2 rows
    assert stats['count'] == 2
    # Max length should be len('This is a much longer headline for testing') = 42
    assert stats['max'] == 42