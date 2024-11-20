import pandas as pd


def data_processing(path, cat1, cat2) -> dict:
    df = pd.read_csv(path)
    data_count = df.groupby([cat1])[cat2].count()
    return data_count.to_dict()




# print(df.to_string())





