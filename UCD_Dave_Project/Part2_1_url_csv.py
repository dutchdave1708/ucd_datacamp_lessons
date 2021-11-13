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

# 1. Download via an API

import rebrick
import json

# init rebrick module for general reading
rebrick.init("your_API_KEY_here")

# get set info
response = rebrick.lego.get_set(6608)
print(json.loads(response.read()))

# init rebrick module including user reading
rebrick.init("your_API_KEY_here", "your_USER_TOKEN_here")

# if you don't know the user token you can use your login credentials
rebrick.init("your_API_KEY_here", "your_username_here", "your_password_here")

# get user partlists
response = rebrick.users.get_partlists()
print(json.loads(response.read()))