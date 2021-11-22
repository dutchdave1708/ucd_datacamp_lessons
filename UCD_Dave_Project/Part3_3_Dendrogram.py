import pandas as pd
import numpy as np
from scipy.cluster.hierarchy import linkage, dendrogram
import matplotlib.pyplot as plt

# read the csv
df = pd.read_csv('Data_files/epi_r.csv')

# set Number of standarddeviations for taking outliers
nrstd = 2  #default is 3, but trying different values.

# note 1, the basic dataset evaluation is done in the Part1_1_Load_ExploreData.py
# note 2, step-by-step clean up done in Part1_2_Selection.py
# note 3, some data processing, analysis and correlation visualisation done in Part1_3_CorrelationMap.py
# copying code through here to get ready for analysis.

# CLEANUP THE DATA
df_unique = df.drop_duplicates('title', ignore_index=True)  #reset index 0 to n-1
# 2. drop rows for the drinks recipes
df_no_drinks = df_unique[(df_unique['drinks'] ==0) & (df_unique['drink'] == 0)]
# 3. Drop all rows with empty colums
df_selection = df_no_drinks.dropna()
# 4. remove outliers > mean+3stdv
columnheaders = ['calories', 'sodium', 'fat', 'protein']  #not title
for columnheader in columnheaders:
    df_selection = df_selection[np.abs(df_selection[columnheader] - df_selection[columnheader].mean()) <= (nrstd * df_selection[columnheader].std())]
#late addition: better results when running this twice as lower mean after first run.
for columnheader in columnheaders:
    df_selection = df_selection[np.abs(df_selection[columnheader] - df_selection[columnheader].mean()) <= (nrstd * df_selection[columnheader].std())]

#late addition: turn sodium milligrams into grams
df_selection['sodium'] = df_selection['sodium'].div(1000).round(2)

#labels in deperate df for later
df_labels = df_selection['title']
df_labels.reset_index(drop=True, inplace=True)
df_labels50 = df_labels.head(50)
list_labels = df_labels50.values.tolist()

#drop title from selection to work with ML
df_selection = df_selection.drop('title', axis=1)
df_selection.reset_index(drop=True, inplace=True)
df_selection50 = df_selection.head(50)
selection_array = df_selection50.to_numpy()

## create hierarchical cluster
# Calculate the linkage: mergings
mergings = linkage(selection_array, method='complete')

#print('calculated mergings')

# Plot the dendrogram, using varieties as labels
#print('start dendrogram')
dendrogram(mergings,
           labels=list_labels,
           leaf_rotation=90,
           leaf_font_size=6,
)
plt.show()
