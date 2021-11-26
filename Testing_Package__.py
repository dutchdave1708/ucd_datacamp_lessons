def read_cleandataframe(filename, nrstd, keycol, clean_col):
    #filename is filepath to read
    #nrstd is number of standard deviation for data cleaning
    #keycol is key column to remove duplicates fro
    #clean_col is a list of columsn to remove outliers from

    # import the relevant packages
    import pandas as pd
    # import file
    df = pd.read_csv(filename)
    # CLEANUP THE DATA
    # 1. Remove duplicates from key column
    #df = df.drop_duplicates(keycol, ignore_index=True)  # reset index 0 to n-1
    # 2. drop rows with empty values, iterate through list to remove Null
    #columnheaders = df.columns.tolist()
    #for columnheader in columnheaders:
        # print(columnheader)
     #   df = df[df[columnheader].notnull()]

    #Column_cleanup = clean_col

    #for X in Column_cleanup:
    #    df = df[
    #        np.abs(df[X] - df[X].mean()) <= (nrstd * df[X].std())]

    # what if we run that twice?  (as after first run, the range will be more narrow and with a lower mean
    #for X in Column_cleanup:
    #    df = df[
    #        np.abs(df[X] - df[X].mean()) <= (nrstd * df[X].std())]

    #print('Dataframe info post cleanup')
    print(df.info())
    return df
