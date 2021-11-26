######### machine learning ######
# OBJECTIVE: I am keen to understand how recommendations are made as well as
# to create an input-model-output solution.
# I am using an IMDB movie data set, as easily available and easy to understand / recognise
# which makes it easier to verify if the code is somewhat correct
# Using various learnings and code-snippets from Datacamp, Kaggle, TowardsDataScience sources
# this is UNSUPERVISED learning,
# Note that Supervised learning is covered in Part1_4 with the regression analysis

###### IMDB movie recommendations ########

# STEP 0 - Import relevant libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

#just putting this at top now, easier for running the script now it is finished
#get recommendations based on this title provided (if it is in the dataset)
movie_title = 'Spectre' #Quantum of Solace / Spectre / The Lone Ranger /

# STEP 1 - Import data that has movies, descriptions, rating, actors, director, revenue, etc.
# Source: Kaggle, which itself got it from IMDb
df_movies = pd.read_csv('Data_files/Imdb_movies.csv')
df_addtl_info = pd.read_csv('Data_files/Imdb_movie_credits.csv')

df_addtl_info = df_addtl_info.rename(columns={'movie_id':'id'})
df_movies2 = df_movies.merge(df_addtl_info, on='id')
df_movies2.rename(columns={'title_x':'title'}, inplace=True)  #duplicate column, so rename and delete title_y
df_movies2.drop('title_y', inplace=True, axis=1)  #notice the use of INPLACE .. should have known that before!
df_movies2 = df_movies2.drop_duplicates(subset=['title'], keep='first')  #remove duplicate title

print(df_movies2.dtypes)
print(df_movies2['release_date'])


df_movies2['year'] = df_movies2['release_date'].str.extract(r'(\d{4})')
df_movies2.dropna(subset=["release_date"], axis = 0 , inplace= True)

#pd.to_numeric(df_movies2['year'], errors='coerce').convert_dtypes()
print(df_movies2['year'])
print(df_movies2['year'].dtype)
df_movies2['year'] = df_movies2['year'].astype(int)
print(df_movies2['year'].dtype)

df_movies2['decade']= (((df_movies2['year'])//10)*10)
print(df_movies2['decade'])

sns.stripplot(y="vote_average", x="decade", data=df_movies2, jitter=1)

plt.xlabel("Release year")
plt.ylabel("Movie rating")
plt.title("Ratings per year")
plt.show()