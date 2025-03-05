import pandas as pd

def load_data(file_path):
    """Load and prepare initial data"""
    df = pd.read_csv(file_path, index_col='date', parse_dates=True)
    return df

def clean_data(df):
    """Clean data removing outliers"""
    lower = df['value'].quantile(0.025)
    upper = df['value'].quantile(0.975)

    return df[(df['value'] >= lower) & (df['value'] <= upper)].copy()