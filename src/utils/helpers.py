import pandas as pd

def check_missing_values(df: pd.DataFrame):
    return df.isnull().sum()

def create_delay_label(df: pd.DataFrame):
    df["is_delayed"] = (df["arr_delay"] > 15).astype(int)
    return df