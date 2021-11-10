# import the relevant packages
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# read the csv
df = pd.read_csv('Data_files/epi_r.csv')

# note 1, the basic dataset evaluation is done in the Part1_1_Load_ExploreData.py
# note 2, step-by-step clean up done in Part1_2_Selection.py
# note 3, some data processing, analysis and correlation visualisation done in Part1_3_CorrelationMap.py
# copying code through here to get ready for analysis.

# CLEANUP THE DATA
df_unique = df.drop_duplicates('title', ignore_index=True)  #reset index 0 to n-1
# 2. drop rows for the drinks recipes
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

# remove outliers > mean+3stdv
# We have to remove outliers in calories, using standard approach with 3 deviation from mean
df_selection2 = df_selection[np.abs(df_selection.calories - df_selection.calories.mean()) <= (3 * df_selection.calories.std())]
df_selection2 = df_selection2[np.abs(df_selection2.sodium - df_selection2.sodium.mean()) <= (3 * df_selection2.sodium.std())]
df_selection2 = df_selection2[np.abs(df_selection2.fat - df_selection2.fat.mean()) <= (3 * df_selection2.fat.std())]
df_selection2 = df_selection2[np.abs(df_selection2.protein - df_selection2.protein.mean()) <= (3 * df_selection2.protein.std())]
df_selection2 = df_selection2[np.abs(df_selection2.alcoholic - df_selection2.alcoholic.mean()) <= (3 * df_selection2.alcoholic.std())]
df_selection2 = df_selection2[np.abs(df_selection2.vegetarian - df_selection2.vegetarian.mean()) <= (3 * df_selection2.vegetarian.std())]

# use training and test data
# set target to Rating
# run various models
# do some charting

