def read_intodataframe(filename):
    import pandas as pd
    df = pd.read_csv(filename)
    return df

def df_basicinfo(dataframe):
    print(dataframe.info())

def df_showcolumns(df):
    columnheaders = df.columns.tolist()
    for x in columnheaders:
        print(x)

def df_removeNulls (dataframe):
    columnheaders = dataframe.columns.tolist()
    for columnheader in columnheaders:
        dataframe = dataframe[dataframe[columnheader].notnull()]
    return dataframe

def df_removeOutliers(df, list_columns, nrstd):
    import numpy as np
    for X in list_columns:
        df = df[
            np.abs(df[X] - df[X].mean()) <= (nrstd * df[X].std())]
    return df
