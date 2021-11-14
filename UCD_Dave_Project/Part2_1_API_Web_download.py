# Evidence ability to download data from API or webscraping
# Loading of .csv file used in 'Part1_' exercises.

# Import packages
import pandas as pd
from urllib.request import urlretrieve

# 0. Download a file from a s3 bucket

# Assign url of file: file with Lego mini-figures
url = 'https://cdn.rebrickable.com/media/downloads/minifigs.csv.gz'
# Save file locally
urlretrieve(url, 'LegoMinifigures.csv.gz')

# read the content into a dataframe
df = pd.read_csv('LegoMinifigures.csv.gz')
print(df.head())





