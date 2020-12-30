import pandas as pd


def load_dataframe_csv(path, name, header=None, error_bad_lines=False):
    return pd.read_csv(path+name, header=header, error_bad_lines=error_bad_lines)


def save_dataframe_csv(df, path, name):
    df.to_csv(path+name, index=False)
