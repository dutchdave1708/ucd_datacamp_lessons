# import the relevant packages
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# read the csv
df = pd.read_csv('Data_files/epi_r.csv')

# note 1, the basic dataset evaluation is done in the Part1_1_Load_ExploreData.py
# note 2, step-by-step clean up done in Part1_2_Selection.py
# copying code through here to get ready for analysis.


# CLEANUP THE DATA
# 1. Only work with unique recipes. Keep the first one.
df_unique = df.drop_duplicates('title', ignore_index=True)  #reset index 0 to n-1
# 2. drop rows for the drinks recipes, only interested in food.
df_no_drinks = df_unique[(df_unique['drinks'] ==0) & (df_unique['drink'] == 0)]
# 3. Make a selection of columns we care about:
df_selection = df_no_drinks[['title', 'rating', 'calories', 'protein', 'fat', 'sodium', 'alcoholic', 'vegetarian']]
# 4. drop rows with empty values
df_selection = df_selection[df_selection['calories'].notnull()]
df_selection = df_selection[df_selection['protein'].notnull()]
df_selection = df_selection[df_selection['fat'].notnull()]
df_selection = df_selection[df_selection['rating'].notnull()]
df_selection = df_selection[df_selection['sodium'].notnull()]
df_selection = df_selection[df_selection['alcoholic'].notnull()]
df_selection = df_selection[df_selection['vegetarian'].notnull()]

# We have to remove outliers in calories, using standard approach with 3 deviation from mean
df_selection2 = df_selection[np.abs(df_selection.calories - df_selection.calories.mean()) <= (3 * df_selection.calories.std())]
df_selection2 = df_selection2[np.abs(df_selection2.sodium - df_selection2.sodium.mean()) <= (3 * df_selection2.sodium.std())]
df_selection2 = df_selection2[np.abs(df_selection2.fat - df_selection2.fat.mean()) <= (3 * df_selection2.fat.std())]
df_selection2 = df_selection2[np.abs(df_selection2.protein - df_selection2.protein.mean()) <= (3 * df_selection2.protein.std())]
df_selection2 = df_selection2[np.abs(df_selection2.alcoholic - df_selection2.alcoholic.mean()) <= (3 * df_selection2.alcoholic.std())]
df_selection2 = df_selection2[np.abs(df_selection2.vegetarian - df_selection2.vegetarian.mean()) <= (3 * df_selection2.vegetarian.std())]


#5. Can we find which value is the strongest indicator for rating?
correlations_1 = df_selection.corr(method = 'pearson')
correlations_2 = df_selection.corr(method = 'kendall')

correlations_1_2 = df_selection2.corr(method = 'pearson')
correlations_2_2 = df_selection2.corr(method = 'kendall')
# seeing the different in correlation values before and after removing outliers.
print(correlations_1)
print(correlations_1_2)
print(correlations_2)
print(correlations_2_2)


#6. Create chart using Seaborn. Using data without outliers.
title1 = 'Correlations (Pearson) between recipe values'
title2 = 'Correlations (Kendall) between recipe values'
sns.heatmap(correlations_1_2, xticklabels=correlations_1.columns, yticklabels=correlations_1.columns, annot=True
            )
plt.title(title1)
plt.show()

sns.heatmap(correlations_2_2, xticklabels=correlations_1.columns, yticklabels=correlations_1.columns, annot=True
            )
plt.title(title2)
plt.show()

# findings with Pearson: no strong correlation, but (in order) Protein, Sodium, Calories correlate most to Rating than the others
# findings with Kendall: no strong correlation, but (in order) Calories, fat, sodium correlate most to Rating

#sns.set_theme(color_codes=True)
#sns.regplot(x="rating", y="calories", data=df_selection)
#plt.show()

# 7 -- can we predict a rating for a new recipe?
print('Go to file Part1_4_Prediction.py to see if we can predict a rating')
