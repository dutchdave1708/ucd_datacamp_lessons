# to load csv into a panda dataframe
# then do basic analysis to understand shape/size/info of datafile

# import the relevant packages
import pandas as pd

# read the csv
df = pd.read_csv('Data_files/epi_r.csv')

# the basic dataset evaluation is done in the other file
# drop duplicate of title, keep the first only
#print('# of rows before = '+ str(df.shape[0]))
df_unique = df.drop_duplicates('title', ignore_index=True)  #reset index 0 to n-1
#print (df_unique)
#print('# of rows after delete = ' + str(df_unique.shape[0]))

#new dataset of 17736 rows.

# drop rows for the drinks recipes
df_no_drinks = df_unique.drop(df_unique[(df_unique['drinks' == 1] ) | (df_unique.drink == 1)].index)


#make a selection of columns to chart: 
# note to pass a list of columns headers into the df, therefor double [[columnames]]
df_selection = df_no_drinks[['title', 'rating', 'calories', 'protein', 'fat', 'sodium', 'alcoholic', 'vegetarian']]




print(df_selection)
#print (unique_rows.loc[(unique_rows['christmas'] == 1) | (unique_rows['christmas eve'] == 1)])
# 1081
#print(df_selection['drink'])

