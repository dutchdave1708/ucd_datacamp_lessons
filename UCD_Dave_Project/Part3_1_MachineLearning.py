######### machine learning ######
# OBJECTIVE: I am keen to understand how recommendations are made as well as
# to create an input-model-output solution.
# I am using an IMDB movie data set, as easily available and easy to understand / recognise
# which makes it easier to verify if the code is somewhat correct
# Using various learnings and code-snippets from Datacamp, Kaggle, TowardsDataScience sources
# this is UNSUPERVISED learning,
# Note that Supervised learning is covered in Part1_4 with the regression analysis

###### IMDB movie recommendations ########
# import relevant libraries
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel

#import data that has movies, descriptions, rating, actors, director, revenue, etc.
# Source: Kaggle, which itself got it from IMDb
df_movies = pd.read_csv('Data_files/Imdb_movies.csv')
df_addtl_info = pd.read_csv('Data_files/Imdb_movie_credits.csv')

df_addtl_info = df_addtl_info.rename(columns={'movie_id':'id'})
df_movies2 = df_movies.merge(df_addtl_info, on='id')
df_movies2.rename(columns={'title_x':'title'}, inplace=True)  #duplicate column, so ranem and delete title_y
df_movies2.drop('title_y', inplace=True, axis=1)  #notice the use of INPLACE .. should have known that before!
df_movies2 = df_movies2.drop_duplicates(subset=['title'], keep='first')  #remove duplicate title

#for col in df_movies2.columns:
#    print(col)

#print(df_movies2.head())
#print(df_movies['spoken_languages'])

#out of interest... any movies with Dutch? --> 10 only!
df_dutchmovies = df_movies2.loc[df_movies2['spoken_languages'].str.contains('Nederlands', case = False)]
#print(df_dutchmovies['original_title'])

#movies with other languages? --> 318 (about 8%)
df_notenglishmovies = df_movies2.loc[df_movies2['spoken_languages'].str.contains('English', case = False) == False]
#print(df_notenglishmovies['original_title'])
#print(df_notenglishmovies.shape[0])

#merge main df with additonal info df
#change columnname from movieid to id for easier merge
#lets explore the dataset to see if there are some rows that should be discounted
avg_rating = df_movies2['vote_average'].mean()
#print(avg_rating)
avg_votecount = df_movies['vote_count'].mean()
#print(avg_votecount)
top50_highest_rated = df_movies2.nlargest(50, 'vote_average')
#print(top50_highest_rated[['original_title','vote_average','vote_count']])
# some highest rated movies have very low number of votes

#drop where less than 200 votes
#print(df_movies2.shape)
df_movies2 = df_movies2.loc[df_movies2['vote_count'] > 200]
#print(df_movies2.shape)

#short chart on distribution of number of votes
df_movies2['vote_count'].plot.hist(bins=500)
plt.xlabel("Number of votes")
plt.ylabel("Number of movies in that bin")
plt.title("Nr of vote Distribution")
#plt.show()

# take top 3000 rows.
df_movies2 = df_movies2.nlargest(3000, 'vote_count')

# re-index to avoid problems later


#print(df_movies2.min())
#print(df_movies2.loc[df_movies2.nsmallest(50, 'vote_count')])

# Weight the rating based on number of votes
# found a comment in QUORA a formula that *supposedly* is used by IMDb
# true or not, I'll use it for now
# weighted rating (WR) = (v ÷ (v+m)) × R + (m ÷ (v+m)) × A where:
# R = average for the movie
# v = number of votes for the movie
# m = minimum votes required to be counted
# a = the mean vote across the whole report


#create funciton to do this
A = df_movies2['vote_average'].mean()
m = 200

def vote_weighted(df, m=200, a=A):
    v = df['vote_count']
    R = df['vote_average']
    # Calculation based on the IMDB formulas
    return ((v/(v+m) * R) + (m/(m+v) * a))

#add a new column 'weight_vote' and apply function
df_movies2['vote_weighted'] = df_movies2.apply(vote_weighted, axis=1)
#print(df_movies2.head())

#Simple chart on distribution of number of votes
df_movies2['vote_weighted'].plot.hist(bins=500)
plt.xlabel("Weighted votes - bin")
plt.ylabel("Number of movies in that bin")
plt.title("Weighted vote distribution")
#plt.show()

#sort in order by weighted vote
# Sort movies based on score calculated above
df_movies2.sort_values('vote_weighted', ascending=False, inplace=True)
#show top 10

# Print top 10 movies
#print(df_movies2[['title', 'vote_count', 'vote_average', 'vote_weighted']].head(10))

#pop = df.sort_values('popularity', ascending=False)
popularity = df_movies2.sort_values('popularity', ascending=False)
plt.figure(figsize=(12,4))
plt.barh(popularity['title'].head(6), popularity['popularity'].head(6), align='center', color='orange')
plt.gca().invert_yaxis()  #flip to horizontal bars instead of vertical
plt.xlabel("Popularity")
plt.title("Most popular movies")
#plt.show()

#chart vote_weighted
plt.figure(figsize=(12,4))
plt.barh(df_movies2['title'].head(6), df_movies2['vote_weighted'].head(6), align='center', color='green')
plt.gca().invert_yaxis()  #flip to horizontal bars instead of vertical
plt.xlabel("Weighted_votes")
plt.title("Best movies as per weighted votes")
#plt.show()

revenue = df_movies2.sort_values('revenue', ascending=False)
plt.figure(figsize=(12,4))
plt.barh(revenue['title'].head(6), revenue['revenue'].head(6), align='center', color='blue')
plt.gca().invert_yaxis()
plt.xlabel("Revenue ($)")
plt.title("Highest revenue movies")
#plt.show()

### the difficult bit #####
# Making recommendations, based on movie descriptions and other info
# I did some research into which models to leverage from scikit-learn
# How to remove useless word
# How to interpret the different factors
# End goal: to create a function that leverage a model to make a top 5 recommendation on which movies
# are similar to the one used as input#


# Calculate tf-idf: this transforms words to vectors to be used for comparisons
# similar to how parts of images or sounds are translated to vectors for digital comparisons

#use title as the index, useful for later.
#df_movies2 = df_movies2.set_index('title')

# include the removall of words such as 'the', 'a'
tfidf = TfidfVectorizer(stop_words='english')
# Replace NaN with an empty string
df_movies['overview'] = df_movies['overview'].fillna('')

# Apply to vectorisation the overview column
tfidf_matrix = tfidf.fit_transform(df_movies['overview'])

# Lets see the output
print(tfidf_matrix.shape)
#--> 2567 rows by 14662 columns


# Compute the cosine similarity matrix
# this is a standard logic to give an assessment of how similar to pieces of text are
# this function is more advanced than simply 'comparing common words
# https://www.machinelearningplus.com/nlp/cosine-similarity/

#compare to itself
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# Change index to title, remove duplicates, if any)
indices = pd.Series(df_movies.index, index=df_movies['title']).drop_duplicates()
print(indices)
print(df_movies.info())

# Function thtat takes in movie title as input and outputing the similar movies
def get_similar(title, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = indices[title]

    # Get the pairwisesimilarity scores of all movies with that movies
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=False)  #had true before but the results were terrible

    # Get the scores of the 5  similar movies
    sim_scores = sim_scores[1:6]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 5 most similar movies
    return df_movies['title'].iloc[movie_indices]

print(get_similar("Pulp Fiction"))

