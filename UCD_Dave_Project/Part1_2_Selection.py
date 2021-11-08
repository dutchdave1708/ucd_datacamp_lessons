# import the relevant packages
import pandas as pd

# read the csv
df = pd.read_csv('Data_files/epi_r.csv')

# note, the basic dataset evaluation is done in the other file

# CLEANUP THE DATA
# 1. drop duplicate of title, keep the first only
df_unique = df.drop_duplicates('title', ignore_index=True)  #reset index 0 to n-1
print('total rows: '+ str(df_unique.count()))
#new dataset of 17736 rows.

# 2. drop rows for the drinks recipes
df_no_drinks = df_unique[(df_unique['drinks'] ==0) & (df_unique['drink'] == 0)]
print('total rows ex drinks: '+ str(df_no_drinks.count()))

# 3. drop rows with empty values
df_values = df_no_drinks[df_no_drinks['calories'].notnull()]
df_values = df_values[df_values['protein'].notnull()]
df_values = df_values[df_values['fat'].notnull()]
df_values = df_values[df_values['rating'].notnull()]
df_values = df_values[df_values['sodium'].notnull()]
df_values = df_values[df_values['alcoholic'].notnull()]
df_values = df_values[df_values['vegetarian'].notnull()]
print('total rows ex empty:  ' + str(df_values.count()))

# Make a selection of columns to chart:
# note to pass a list of columns headers into the df, therefor double [[columnames]]
df_selection = df_values[['title', 'rating', 'calories', 'protein', 'fat', 'sodium', 'alcoholic', 'vegetarian']]

print(df_selection.info())


#find the mean rating
print('Original file, pre-processed, rating avg:  ' + str(df['rating'].mean()))

print('File post processing, avg rating:  ' + str(df_selection['rating'].mean()))

# Can we find which value is the strongest indicator for rating?
# can we predict a rating for a new recipe?
# lets go to file Part1_3_Analysis