import pandas as pd

COLUMNS = ["Name", "Type", "Sector", "Location"]

def load_data(uploaded_file):
    return pd.read_csv(uploaded_file)

def save_data(df, filename):
    df.to_csv(filename, index=False)
