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
df = pd.read_csv('LegoMinifigures.csv.gz')
print(df.head())

# unzip the file
#import gzip
#import shutil
#with gzip.open('file.txt.gz', 'rb') as f_in:
#    with open('file.txt', 'wb') as f_out:
 #       shutil.copyfileobj(f_in, f_out)
# Read file into a DataFrame and print its head



# 1. scrape data from webpage



# 2. load data from API
#***** stream from Twitter API ****
# Import package
import json

# String of path to file: tweets_data_path
tweets_data_path = 'tweets.txt'

# Initialize empty list to store tweets: tweets_data
tweets_data = []

# Open connection to file
tweets_file = open(tweets_data_path, "r")

# Read in tweets and store in list: tweets_data
for line in tweets_file:
    tweet = json.loads(line)
    tweets_data.append(tweet)

# Close connection to file
tweets_file.close()

# Print the keys of the first tweet dict
print(tweets_data[0].keys())



#***** import from API ****
# Import requests package
import requests
# Assign URL to variable: url
url = 'http://www.omdbapi.com/?apikey=72bc447a&t=the+social+network'
# Package the request, send the request and catch the response: r
r = requests.get(url)
# Print the text of the response
print(r.text)


#***** import directly into dataframe without saving locally ( and plot chart)
# Import packages
import matplotlib.pyplot as plt
import pandas as pd
# Assign url of file: url
url = 'https://s3.amazonaws.com/assets.datacamp.com/production/course_1606/datasets/winequality-red.csv'
# Read file into a DataFrame: df
df = pd.read_csv(url, sep = ';')
# Print the head of the DataFrame
print(df.head())
# Plot first column of df
pd.DataFrame.hist(df.ix[:, 0:1])
plt.xlabel('fixed acidity (g(tartaric acid)/dm$^3$)')
plt.ylabel('count')
plt.show()

#**** READING AN EXCEL FILE
# Read in all sheets of Excel file: xls
xls = pd.read_excel(url, sheet_name = None)
# Print the sheetnames to the shell
print(xls.keys())
# Print the head of the first sheet (using its name, NOT its index)
print(xls['1700'].head())


# Import packages
#import urlopen
from urllib.request import Request, urlopen

# Specify the url
url = "https://campus.datacamp.com/courses/1606/4135?ex=2"

# This packages the request: request
request = Request(url)

# Sends the request and catches the response: response
response = urlopen(request)

# Print the datatype of response
print(type(response))

# Be polite and close the response!
response.close()



#### extract html into local variable ###
# Import package
import requests


# Specify the url: url
url = 'http://www.datacamp.com/teach/documentation'

# Packages the request, send the request and catch the response: r
#request = Request(url)
r = requests.get(url)

# Extract the response: text
text = r.text

# Print the html
print(text)

###### extract using Soup ... HTML parsers
# Import packages
import requests
from bs4 import BeautifulSoup

# Specify url: url
url = 'https://www.python.org/~guido/'

# Package the request, send the request and catch the response: r
r = requests.get(url)

# Extract the response as html: html_doc
html_doc = r.text

# Create a BeautifulSoup object from the HTML: soup
soup = BeautifulSoup(html_doc)

# Get the title of Guido's webpage: guido_title
guido_title = soup.title


# Print the title of Guido's webpage to the shell
print(guido_title)

# Get Guido's text: guido_text
guido_text = soup.get_text()

# Print Guido's text to the shell
print(guido_text)