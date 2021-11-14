# Import packages
import pandas as pd
from urllib.request import urlretrieve

# 0. Download a file from a s3 bucket

# Assign url of file: file with Lego mini-figures
# NOTE - had to install Certificates command..
url = 'https://cdn.rebrickable.com/media/downloads/minifigs.csv.gz?1636621682.3233504'
filename = 'LegoMinifigures.csv.gz'
# Save file locally
urlretrieve(url, filename)
#NOTE pd.read_csv automatically handles the Unzipping of gz files
df = pd.read_csv(filename)
print(df.head())

