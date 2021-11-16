# import the relevant packages
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score

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
df_selection = df_selection.drop('title', axis=1)  #cant work with strings

print('total rows ex drinks: '+ str(df_selection.calories.count()))
print('Data processing done')

############# data prep done ###########
# predicting ratings: this will be a regression problem (not a categorisation problem)
# step 1: set Target value = number of calories
# step 1.1 - drop the Target
X = df_selection.drop('calories', axis=1).values
# first, predict calories based on fat
# doing it this way as I have changed feature a few times.
# note, feature fat is 3rd column, index 2: print(X[...,2])
X_fat = X[...,2]

# step 1.2 - create Target
y = df_selection['calories'].values

# step 1.3 add dimension to array
y = y.reshape(-1,1)
X_fat = X_fat.reshape(-1,1)

# step 2: create chart with regression line
# step 2.1: plot scatter chart
print('plot a scatter chart')
plt.scatter(X_fat, y)
plt.xlabel('Fat values in recipe')
plt.ylabel('Calorie values in recipe')
plt.show()

# step 2.2 fit a regression model
reg = LinearRegression()
prediction = np.linspace(min(X_fat), max(X_fat)).reshape(-1,1)
reg.fit(X_fat, y)
y_pred = reg.predict(prediction)
#print(reg.score(X_fat, y))

#plotting this line on the chart
plt.scatter(X_fat, y, color = 'orange')
plt.plot(prediction, y_pred, color = 'black', linewidth = 4)
plt.xlabel('Fat values in recipe')
plt.ylabel('Calorie values in recipe')
plt.show()

# Next step: using test & train data to calculate R^2
X_train, X_test, y_train, y_test = train_test_split(X_fat, y, test_size = 0.3, random_state = 42)
reg_all = LinearRegression()
reg_all.fit(X_train, y_train)
print("R^2: {}".format(reg_all.score(X_test, y_test)))

y_pred = reg_all.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error: {}".format(rmse))

#k-fold CV
reg = LinearRegression()
cv_results = cross_val_score(reg, X_fat, y, cv = 5)  #reports R^2
print(cv_results)


