# import the relevant packages
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.model_selection import cross_val_score

#import seaborn as sns

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
# 3. Drop all rows with empty colums
df_selection = df_no_drinks.dropna()#[['title', 'rating', 'calories', 'protein', 'fat', 'sodium', 'alcoholic', 'vegetarian']]
# 4. remove outliers > mean+3stdv
# We have to remove outliers in calories, using standard approach with 3 deviation from mean
columnheaders = ['calories', 'sodium', 'fat', 'protein']  #not title
for columnheader in columnheaders:
    df_selection = df_selection[np.abs(df_selection[columnheader] - df_selection[columnheader].mean()) <= (3 * df_selection[columnheader].std())]

print('Data processing done')
print('total rows ex drinks: '+ str(df_selection.title.count()))

#predicting ratings: this will be a regression problem (not a categorisation problem)
# Target value = number of calories
# First: create chart with regression line

#Step 1 - drop the Target
X = df_selection.drop('calories', axis =1).values
X = df_selection.drop('title', axis=1).values  #cant work with strings
#Step 2 - create Target
y = df_selection['calories'].values

print(type(X))
print(type(y))

#first, predict calories based on fat
X_fat = X[:,4]
print(type(y))
print(type(X_fat))
#add dimension to array
y = y.reshape(-1,1)
X_fat = X_fat.reshape(-1,1)
print('plot a scatter chart')
plt.scatter(X_fat, y)
plt.ylabel('Calorie values in recipe')
plt.xlabel('Fat values in recipe')
plt.show()

#fit a regression model

reg = LinearRegression()
reg.fit(X_fat, y)

prediction = np.linspace(min(X_fat), max(X_fat)).reshape(-1,1)

#plotting this line on the chart
plt.scatter(X_fat, y, color = 'orange')
plt.plot(prediction, reg.predict(prediction), color = 'black', linewidth = 4)
plt.ylabel('Calorie values in recipe')
plt.xlabel('Fat values in recipe')
plt.show()

# Next step: using test & train data to calculate R^2
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.3, random_state = 42)
reg_all = LinearRegression()
reg_all.fit(X_train, y_train)
y_pred = reg_all.predict(X_test)
print("R^2: {}".format(reg_all.score(X_test, y_test)))
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print("Root Mean Squared Error: {}".format(rmse))

#k-fold CV
reg = LinearRegression()
cv_results = cross_val_score(reg, X, y, cv = 5)  #reports R^2
print(cv_results)


