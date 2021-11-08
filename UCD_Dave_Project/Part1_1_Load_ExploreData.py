# to load csv into a panda dataframe
# then do basic analysis to understand shape/size/info of datafile

# import the relevant packages
import pandas as pd

# read the csv
df = pd.read_csv('Data_files/epi_r.csv')

# explore the file
print('The first 10 rows are...')
print(df.head(10)) #show 10 rows

#but there are many columns (680), and we want to see the all to be able to make a selection
# note, reason for many columns is tht all ingredients and text values are converted to columns with float as value

for col in df.columns:
    print(col)

print('show datatypes of the dataframe')
print(df.dtypes) # show datatypes of columns
#679 columns of type float, 1 object (the title column)

print('Show basic info of dataframe')
df.info() # show info on columns, missing values, etc

# explore 3 columns specifically
print('describe title column')
print(df.title.describe()) # gives various info on that column. depends on type
#20052 titles, of which 17736 unique
#Pastry Dough appears 28 times

print('describe rating column')
print(df.rating.describe()) # gives various info on that column. depends on type
# confirm there are no strange outliers

print('describe banana column')
print(df.banana.describe()) # gives various info on that column. depends on type
# reviewing how measures are converted to float values

# drop duplicate of title, keep the first only
print('# of rows before = '+ str(df.shape[0]))
unique_rows = df.drop_duplicates('title', ignore_index=True)  #reset index 0 to n-1
print (unique_rows)
print('# of rows after delete = ' + str(unique_rows.shape[0]))

#new dataset of 17736 rows.
#now explore the rating, we only want those with meaningful ratings



#show recipes relating to
#1. Diwali
print ('25 Diwali recipes include: ')
print(unique_rows.loc[unique_rows['diwali'] == 1])
#2. Christmas
#print ('Christmas recipes include: ')
#print(df.loc[df['christmas'] == 1] | (df.loc[df['christmas eve'] == 1]))
#2. Christmas
print ('Christmas recipes include: 1039 rows')
print (unique_rows.loc[unique_rows['christmas'] == 1])
# result = 1039

print ('Christmas OR christmas eve recipes:  ')
print (unique_rows.loc[(unique_rows['christmas'] == 1) | (unique_rows['christmas eve'] == 1)])
# 1081

print ('Which Christmas eve recipes are not Christmas recipes?')
print (unique_rows.loc[(unique_rows['christmas'] == 0) & (unique_rows['christmas eve'] == 1)])
# 42

print ('Which christmas recipes are not Christmas Eve recipes?')
print (unique_rows.loc[(unique_rows['christmas'] == 1) & (unique_rows['christmas eve'] == 0)])
# 750

#make a selection of columns to chart:
print(' SWITCH TO FILE Part1_2_Selection.py')


