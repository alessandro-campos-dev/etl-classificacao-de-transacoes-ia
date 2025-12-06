import pandas as pd
from src.utils.text_cleaning import clean_text

def transform(df):
    df["date"] = pd.to_datetime(df["date"], errors="coerce")
    df["amount"] = pd.to_numeric(df["amount"], errors="coerce")
    df["description_clean"] = df["description"].apply(clean_text)
    return df
