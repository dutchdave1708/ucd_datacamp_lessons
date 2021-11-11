# import the relevant packages
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt



# read the csv
df = pd.read_csv('Data_files/epi_r.csv')

# note, the basic dataset evaluation is done in the other file

# CLEANUP THE DATA
# 1. Only work with unique recipes. Keep the first one.
df_unique = df.drop_duplicates('title', ignore_index=True)  #reset index 0 to n-1
print('total rows: '+ str(df_unique.count()))
#new dataset of 17736 rows.

# 2. drop rows for the drinks recipes
df_no_drinks = df_unique[(df_unique['drinks'] ==0) & (df_unique['drink'] == 0)]
print('total rows ex drinks: '+ str(df_no_drinks.count()))

# 3. Make a selection of columns we care about:
# note to pass a list of columns headers into the df, therefor double [[columnames]]

df_selection = df_no_drinks[['title', 'rating', 'calories', 'protein', 'fat', 'sodium', 'alcoholic', 'vegetarian']]

# 4. drop rows with empty values
df_selection = df_selection[df_selection['calories'].notnull()]
df_selection = df_selection[df_selection['protein'].notnull()]
df_selection = df_selection[df_selection['fat'].notnull()]
df_selection = df_selection[df_selection['rating'].notnull()]
df_selection = df_selection[df_selection['sodium'].notnull()]
df_selection = df_selection[df_selection['alcoholic'].notnull()]
df_selection = df_selection[df_selection['vegetarian'].notnull()]
print('total rows ex empty:  ' + str(df_selection.count()))

#5a Create chart to map calories to ratings, see if there is a normal range
plt.scatter(df_selection['rating'], df_selection['calories'])
plt.scatter(df_selection['rating'], df_selection['sodium'])
plt.title('Calorie / Sodium values outliers?')
plt.ylabel('Calories & Sodium')
plt.xlabel('Rating')
plt.show()
# certainly some outliers
#5. futher clean up. Find mean of rating
print(df_selection.info())
print('Original file, pre-processed, rating avg:  ' + str(df['rating'].mean()))
print('File post processing, avg rating:  ' + str(df_selection['rating'].mean()))

print('Min & max values for key columns: calories, fat, sodium, protein')
print('Min& Max for calories: ' + str(df_selection.calories.max()) + ' , ' + str(df_selection.calories.min()))
print('Min& Max for sodium: ' + str(df_selection.sodium.max()) + ' , ' + str(df_selection.sodium.min()))
print('Min& Max for fat: ' + str(df_selection.fat.max()) + ' , ' + str(df_selection.fat.min()))
print('Min& Max for protein: ' + str(df_selection.protein.max()) + ' , ' + str(df_selection.protein.min()))

# The max is out of range, we have to remove outliers in calories, using  approach with 3 deviation mean
# keep only the ones that are within + 3 to - 3 standard deviations in the column 'Data'.
df_selection2 = df_selection[np.abs(df_selection.calories - df_selection.calories.mean()) <= (3 * df_selection.calories.std())]
df_selection2 = df_selection2[np.abs(df_selection2.sodium - df_selection2.sodium.mean()) <= (3 * df_selection2.sodium.std())]
df_selection2 = df_selection2[np.abs(df_selection2.fat - df_selection2.fat.mean()) <= (3 * df_selection2.fat.std())]
df_selection2 = df_selection2[np.abs(df_selection2.protein - df_selection2.protein.mean()) <= (3 * df_selection2.protein.std())]

#NOTE - i had also removed the ones where calories is too low, but on reflection those are valid numbers
#df_selection2 = df_selection2[~(np.abs(df_selection2.calories - df_selection2.calories.mean()) > (3 * df_selection2.calories.std()))]


# now check again with same cahrts
plt.scatter(df_selection2['rating'], df_selection2['calories'])
plt.scatter(df_selection2['rating'], df_selection2['sodium'])
plt.title('Calorie / Sodium values outliers?')
plt.ylabel('Calories & Sodium')
plt.xlabel('Rating')
plt.show()

# much better distribution of values. Probbaly still some bad data, but less impactful.

print('Dataframe info post cleanup')
print(df_selection2.info())
print(df_selection2.calories.max(), df_selection2.calories.min())
print('Mean for Calories, before removing outliers:  ' + str(df_selection['calories'].mean()) + ' after: ' + str(df_selection2['calories'].mean()))
print('Mean for Sodium, before removing outliers:  ' + str(df_selection['sodium'].mean()) + ' after: ' + str(df_selection2['sodium'].mean()))
print('Mean for fat, before removing outliers:  ' + str(df_selection['fat'].mean()) + ' after: ' + str(df_selection2['fat'].mean()))
print('Mean for Protein, before removing outliers:  ' + str(df_selection['protein'].mean()) + ' after: ' + str(df_selection2['protein'].mean()))

print('..and lastly, how the rating has evolved during cleanups')
print('Original: ' + "{:.2f}".format((df['rating'].mean())) + ' Unique: ' +
        "{:.2f}".format((df_unique['rating'].mean())) + ' No Nulls: ' + "{:.2f}".format((df_selection['rating'].mean())) +
        ' NoOutliers: ' + "{:.2f}".format((df_selection2['rating'].mean())))

# Can we find which value is the strongest indicator for rating?
# can we predict a rating for a new recipe?
# lets go to file Part1_3_Analysis