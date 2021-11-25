import Custom_Functions as dave

df = dave.read_intodataframe('Data_files/epi_r.csv')

dave.df_basicinfo(df)

dave.df_showcolumns(df)

df = dave.df_removeNulls(df)
dave.df_basicinfo(df)

df = dave.df_removeOutliers(df, ['calories','protein','fat', 'sodium'], 3)

dave.df_basicinfo(df)