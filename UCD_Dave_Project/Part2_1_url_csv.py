# NOTE - had to install Certificates command..
# NOTE - website to see files and schema: https://rebrickable.com/downloads/
# Import packages
import pandas as pd
from urllib.request import urlretrieve

# 0. Download a file from a url, a file with all Lego sets
url = 'https://cdn.rebrickable.com/media/downloads/sets.csv.gz?1636989653.989331'
filename = 'Legosets.csv.gz'
# Save file locally
urlretrieve(url, filename)
df_legosets = pd.read_csv(filename)

#files with theme categories
url = 'https://cdn.rebrickable.com/media/downloads/themes.csv.gz?1636989652.4253716'
filename = 'Themes.csv.gz'
# Save file locally
urlretrieve(url, filename)
df_themes = pd.read_csv(filename)

print(df_themes.info())  #442 categories
print(df_legosets.info())  #18327 rows

#Merge  dataframe df_legosets with df_themes
#df_themes has column id, name and parentid
#df_legosets has column theme_id which references theme.id
#I want the theme.name in the merged dataframe.
df_merged = pd.merge(df_legosets, df_themes, left_on='theme_id', right_on='id')

print('Number of rows: ' + str((df_merged.shape[0]+1)) + ' and Columns from merged dataset: ' + str(df_merged.columns.tolist()))

#change some columnname
df_merged = df_merged.rename(columns={'name_x': 'set_name', 'name_y':'theme_name'})
#drop duplicate columns
df_merged = df_merged.drop(['id', 'parent_id'], axis=1)
print('Columns after update from merged dataset: ' + str(df_merged.columns.tolist()))
