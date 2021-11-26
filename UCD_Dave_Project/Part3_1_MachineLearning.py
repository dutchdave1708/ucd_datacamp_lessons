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

# 1.2 - merge datasets and rename some columns for ease later
df_addtl_info = df_addtl_info.rename(columns={'movie_id':'id'})
df_movies2 = df_movies.merge(df_addtl_info, on='id')
df_movies2.rename(columns={'title_x':'title'}, inplace=True)  #duplicate column, so rename and delete title_y
df_movies2.drop('title_y', inplace=True, axis=1)  #notice the use of INPLACE .. should have known that before!
df_movies2 = df_movies2.drop_duplicates(subset=['title'], keep='first')  #remove duplicate title

# 1.3 list all columns so we know what is there exactly
#for col in df_movies2.columns:
 #       print(col)

#STEP 2 - Some  exploring of the data

#2.1..out of interest... any movies with Dutch? --> 10 only!
df_dutchmovies = df_movies2.loc[df_movies2['spoken_languages'].str.contains('Nederlands', case = False)]
print('movies with Dutch language: ')
print(df_dutchmovies['original_title'])

#2.2...movies with other languages? --> 318 (about 8%)
df_notenglishmovies = df_movies2.loc[df_movies2['spoken_languages'].str.contains('English', case = False) == False]
#print(df_notenglishmovies['original_title'])

#2.3   explore the dataset to see if there are some rows that should be discounted
avg_rating = df_movies2['vote_average'].mean()
#print(avg_rating)
avg_votecount = df_movies['vote_count'].mean()
#print(avg_votecount)
top50_highest_rated = df_movies2.nlargest(50, 'vote_average')
#print(top50_highest_rated[['original_title','vote_average','vote_count']])
# NOTE --> some highest rated movies have very low number of votes, need to be excluded

#3 - DROP where vote count is less than 200 votes
df_movies2 = df_movies2.loc[df_movies2['vote_count'] > 200]

#4 - Charting..
#4.1 chart on distribution of number of votes
df_movies2['vote_count'].plot.hist(bins=500)  # trial&error on nr of  bins, otherwise chart is useless
plt.xlabel("Number of votes")
plt.ylabel("Number of movies in that bin")
plt.title("Number of vote Distribution")
plt.show()

# Decide to take top 3000 rows.
df_movies2 = df_movies2.nlargest(3000, 'vote_count')

#print(df_movies2.min())
#print(df_movies2.loc[df_movies2.nsmallest(50, 'vote_count')])

#5 - Calculate Weighted Votes

# Weight the rating based on number of votes
# I found a comment on QUORA with formula that *supposedly* is used by IMDb
# true or not, I'll use it for now
# weighted rating (WR) = (v ÷ (v+m)) × R + (m ÷ (v+m)) × A where:
# R = average for the movie
# v = number of votes for the movie
# m = minimum votes required to be counted
# A = the mean vote across the whole report


#5.1 create function to do this
A = df_movies2['vote_average'].mean()
m = 200

def vote_weighted(df, m=200, a=A):
    v = df['vote_count']
    R = df['vote_average']
    # Calculation based on the IMDB formulas
    return ((v/(v+m) * R) + (m/(m+v) * a))

#5.2 Add a new column 'vote_weighted' and apply function
df_movies2['vote_weighted'] = df_movies2.apply(vote_weighted, axis=1)

#5.3 Chart on distribution of Weighted_Vote
df_movies2['vote_weighted'].plot.hist(bins=500)
plt.xlabel("Weighted votes - bin")
plt.ylabel("Number of movies in that bin")
plt.title("Weighted vote distribution")
plt.show()

#5.4 Chart in order by weighted vote
# Print top 10 movies
# print(df_movies2[['title', 'vote_count', 'vote_average', 'vote_weighted']].head(10))
popularity = df_movies2.sort_values('popularity', ascending=False)
plt.figure(figsize=(12,4))
plt.barh(popularity['title'].head(6), popularity['popularity'].head(6), align='center', color='orange')
plt.gca().invert_yaxis()  #flip to horizontal bars instead of vertical
plt.xlabel("Popularity")
plt.title("Most popular movies")
plt.show()

#5.5 chart Vote - Unweighted
df_movies2.sort_values('vote_average', ascending=False, inplace=True)
plt.figure(figsize=(12,4))
plt.barh(df_movies2['title'].head(6), df_movies2['vote_average'].head(6), align='center', color='green')
plt.gca().invert_yaxis()  #flip to horizontal bars instead of vertical
plt.xlabel("AVG unweighted votes")
plt.title("Best movies as per vote avg, min 200 votes")
plt.show()

#5.6 chart vote_weighted
df_movies2.sort_values('vote_weighted', ascending=False, inplace=True)
plt.figure(figsize=(12,4))
plt.barh(df_movies2['title'].head(6), df_movies2['vote_weighted'].head(6), align='center', color='green')
plt.gca().invert_yaxis()  #flip to horizontal bars instead of vertical
plt.xlabel("Weighted votes")
plt.title("Best movies as per weighted votes")
plt.show()

#5.7 chart vote weighted and foreign movies
df_notenglishmovies = df_movies2.loc[df_movies2['spoken_languages'].str.contains('English', case = False) == False]
df_notenglishmovies.sort_values('vote_weighted', ascending=False, inplace=True)
plt.figure(figsize=(12,4))
plt.barh(df_notenglishmovies['title'].head(6), df_notenglishmovies['vote_weighted'].head(6), align='center', color='green')
plt.gca().invert_yaxis()  #flip to horizontal bars instead of vertical
plt.xlabel("Weighted votes")
plt.title("Non-english movies as per weighted votes")
plt.show()
#5.7 chart on top 6 by Revenue
revenue = df_movies2.sort_values('revenue', ascending=False)
plt.figure(figsize=(12,4))
plt.barh(revenue['title'].head(6), revenue['revenue'].head(6), align='center', color='blue')
plt.gca().invert_yaxis()
plt.xlabel("Revenue ($)")
plt.title("Highest revenue movies")
plt.show()
# 5.8 Which movies have biggest difference weighted/non-weighted
# calculate delta avg to weighted vote, add to df
df_movies2['delta'] = abs(df_movies2['vote_average'] - df_movies2['vote_weighted'])
df_movies2.sort_values('delta', ascending=False, inplace=True)
print('movies with biggest delta weighted-unweighted rating:')
print(df_movies2[['title','delta', 'vote_weighted','vote_average','vote_count']].to_string(index=False,max_rows=10))

# 5.9 plot weighted rating per year by extractng year from Release Data
df_movies2.dropna(subset=["release_date"], axis = 0 , inplace= True)
df_movies2['year'] = df_movies2['release_date'].str.extract(r'(\d{4})')
sns.stripplot(y="vote_average", x="year", data=df_movies2, jitter=1)
plt.xlabel("Release year")
plt.ylabel("Movie rating")
plt.title("Ratings per year")
plt.show()

# 5.10 By year was useless, do converting to Decade
# .. which took a long time to work out!

# convert from dtype object to integer
df_movies2['year'] = df_movies2['year'].astype(int)
# do integer-divide * 10 logic to effectively '0' last year-digit and get the decade
df_movies2['decade']= (((df_movies2['year'])//10)*10)
#print(df_movies2['decade'])

# plot on stripplot, which looks good
sns.stripplot(y="vote_average", x="decade", data=df_movies2, jitter=1)
plt.xlabel("Release decade")
plt.ylabel("Movie rating - weighted")
plt.title("Ratings per decade")
plt.show()

#print(df_movies2['title'].loc[df_movies2['decade'] == 1920])

### the difficult bit #####
# Making recommendations, based on movie descriptions and other info
# I did some research into which models to leverage from scikit-learn
# How to remove useless words
# How to translate words to vectors, just like with images/sounds
# End goal: to create a function that leverage a model to make a top 5 recommendation on which movies
# are similar to the one used as input#

# Note: using the original file content with all ~5000 movies, regardless of number of votes.

# STEP 1: Calculate tf-idf: this transforms words to vectors to be used for comparisons
# similar to how parts of images or sounds are translated to vectors for digital comparisons

# STEP 1.1: remove words such as 'the', 'a'. standard function for that.
tfidf = TfidfVectorizer(stop_words='english')
# STEP 1.2: Replace NaN with an empty string
df_movies['overview'] = df_movies['overview'].fillna('')
# STEP 1.3: Fit the vectorisation on overview column
tfidf_matrix = tfidf.fit_transform(df_movies['overview'])

# Lets see the shape
#print(tfidf_matrix.shape)
# note all the additional columns in the matrix with values

# STEP 2 - Compute the cosine similarity matrix
# this is a standard logic to give an assessment of how similar to pieces of text are
# this function is more advanced than simply 'comparing common words'
# https://www.machinelearningplus.com/nlp/cosine-similarity/

# STEP 2.1 - Compare to itself
cosine_sim = linear_kernel(tfidf_matrix, tfidf_matrix)

# STEP 2.2 - Create 1-dimensional array with index values for the function
indices = pd.Series(df_movies.index, index=df_movies['title']).drop_duplicates()
#print(indices)

# STEP 2.3 - Create function that takes in movie title as input and outputs the similar movies
def get_similar(title, cosine_sim=cosine_sim):
    # Get the index of the movie that matches the title
    idx = indices[title]

    # Get the similarity scores of all movies with the movie provided
    sim_scores = list(enumerate(cosine_sim[idx]))

    # Sort the movies based on the similarity scores
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=False)  #had true before but the results were terrible

    # Get the scores of the 5 similar movies based on the description
    sim_scores = sim_scores[1:6]

    # Get the movie indices
    movie_indices = [i[0] for i in sim_scores]

    # Return the top 5 most similar movies
    return df_movies['title'].iloc[movie_indices]

print('')
print('Recommendations based on movie: ' + movie_title)
print(get_similar(movie_title))
print('')
print('**************************************************************')
print( "                   THE END      ")