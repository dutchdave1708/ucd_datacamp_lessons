# import the relevant packages
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


# read the csv
df = pd.read_csv('Data_files/epi_r.csv')

# note 1, the basic dataset evaluation is done in the Part1_1_Load_ExploreData.py
# note 2, step-by-step clean up done in Part1_2_Selection.py
# copying code through here to get ready for analysis.

# CLEANUP THE DATA
df_unique = df.drop_duplicates('title', ignore_index=True)  #reset index 0 to n-1
# 2. drop rows for the drinks recipes
df_no_drinks = df_unique[(df_unique['drinks'] ==0) & (df_unique['drink'] == 0)]
# 3. drop rows with empty values
df_values = df_no_drinks[df_no_drinks['calories'].notnull()]
df_values = df_values[df_values['protein'].notnull()]
df_values = df_values[df_values['fat'].notnull()]
df_values = df_values[df_values['rating'].notnull()]
df_values = df_values[df_values['sodium'].notnull()]
df_values = df_values[df_values['alcoholic'].notnull()]
df_values = df_values[df_values['vegetarian'].notnull()]
# Make a selection of columns we care about:
df_selection = df_values[['title', 'rating', 'calories', 'protein', 'fat', 'sodium', 'alcoholic', 'vegetarian']]


# 1 -- Can we find which value is the strongest indicator for rating?

correlations_1 = df_selection.corr(method = 'pearson')
correlations_2 = df_selection.corr(method = 'kendall')

print(correlations_1)
print(correlations_2)

#Create chart using Seaborn
title1 = 'Correlations (Pearson) between recipe values'
title2 = 'Correlations (Kendall) between recipe values'
sns.heatmap(correlations_1, xticklabels=correlations_1.columns, yticklabels=correlations_1.columns, annot=True
            )
plt.title(title1)
plt.show()

sns.heatmap(correlations_2, xticklabels=correlations_1.columns, yticklabels=correlations_1.columns, annot=True
            )
plt.title(title2)
plt.show()

# findings with Pearson: no strong correlation, but (in order) Protein, Sodium, Calories correlate most to Rating than the others
# findings with Kendall: no strong correlation, but (in order) Calories, fat, sodium correlate most to Rating

# 2 -- can we predict a rating for a new recipe?
