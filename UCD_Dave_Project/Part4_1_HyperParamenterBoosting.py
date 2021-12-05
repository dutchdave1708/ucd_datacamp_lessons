## Hyperparamenter boosting
# Copy logic from regression analysis from file Part1_4
# the logic in file Part3_4: all Accuracy cores were already very high, so no need to further attempt
# hyper-parameter boosting.
# Hence going back to Regression logic in Part1_4.

# import the relevant packages
# some packages used in previous runs of this scripts,
# so un-used now, means used previously or in now-commented-out code.

import pandas as pd
import numpy as np
from sklearn.linear_model import Ridge, LinearRegression
from sklearn.model_selection import train_test_split, GridSearchCV, RepeatedStratifiedKFold, RandomizedSearchCV, \
    RepeatedKFold
import warnings

# surpress warnings, as too many 'deprecated' warnings when running this
warnings.simplefilter("ignore", category=DeprecationWarning)

# read the csv
df = pd.read_csv('Data_files/epi_r.csv')
# set Number of standarddeviations for taking outliers
nrstd = 2  #default is 3, but trying different values.
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
#better results when running this twice as lower mean after first run.
for columnheader in columnheaders:
    df_selection = df_selection[np.abs(df_selection[columnheader] - df_selection[columnheader].mean()) <= (nrstd * df_selection[columnheader].std())]
#turn sodium milligrams into grams
df_selection['sodium'] = df_selection['sodium'].div(1000).round(2)
df_selection = df_selection.drop('title', axis=1)  #cant work with strings
# predicting calories: this will be a regression problem (not a categorisation problem)
# step 1.1 - drop the Target
X = df_selection.drop('calories', axis=1).values
# also, predict calories based on fat only, which is the 3rd column, index 2: print(X[...,2])
X_fat = X[...,2]
# step 1.2 - create Target
y = df_selection['calories'].values
# step 1.3 add dimension to array
y = y.reshape(-1,1)
X_fat = X_fat.reshape(-1,1)

# Hyperparameter Tuning
# reference used:
# https://machinelearningmastery.com/hyperparameter-optimization-with-random-search-and-grid-search/

# Define model
model = Ridge()

# Define search space  (ie, the range of parameters to find the best combination for)
space = dict()
space['solver']=['svd','cholesky', 'lsqr', 'sag', 'saga', 'lbfgs']
space['alpha']= [1e5,1e4,1e3,1e2,1e1,1,10,100]
space['fit_intercept']=[True, False]

# for a regression problem, recommended to use RepeatedKFold
cv = RepeatedKFold(n_splits=10, n_repeats=3, random_state=1)
#alternative also used: cv = RepeatedStratifiedKFold(n_splits=10, n_repeats=3, random_state=1)

#scoring. For regression, target is a negative value as close to 0 as possible
#n_jobs is argument to use cpu available. specify as -1 for 'all'
search=GridSearchCV(model, space, cv=cv, scoring='neg_mean_absolute_error', n_jobs=-1)

#also used: search=RandomizedSearchCV(model, space, n_iter=250, cv=cv, scoring='neg_mean_absolute_error', n_jobs=-1)

# fit the search on the dataset to train & evaluate the model's hyperparameter combinations

result = search.fit(X_fat,y)
#result = search.fit(X,y)  #this took hours to run, so only did  that once

# results
print('Beste Score: %s' % result.best_score_)
print('Best parameters: %s' % result.best_params_)

# best score, just on Fat predicting Calories
    #Beste Score: -90.15588347464163
    #Best parameters: {}
# best score after tuning, with all column prediction Calories
    #Beste Score: -55.34078453448871
    #Best parameters: {'alpha': 10.0, 'fit_intercept': True, 'normalize': False, 'solver': 'svd'}

