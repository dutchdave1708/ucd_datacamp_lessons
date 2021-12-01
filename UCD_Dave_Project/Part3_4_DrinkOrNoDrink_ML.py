# to try more machine learning logic
# Going back to Recipe dataset: can we determine of a recipe is a drink or not, based on ingredients
# similar data cleanup as before, but leaving drinks in there (as that as the target).
# then create a learning model, train & test data set
# then provide ingredients for new recipe and see what happens

# Import packages
import pandas as pd
import Custom_Functions as dave
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import seaborn as sns
#from sklearn.metrics import plot_confusion_matrix

# import dataset
recipes = dave.read_intodataframe('Data_files/epi_r.csv')
recipes = recipes.drop_duplicates('title', ignore_index=True)  # to reset index 0 to n-1

# show columns
# dave.df_showcolumns(recipes)

# remove all Nulls
recipes = dave.df_removeNulls(recipes)

# remove outliers, run that twice for better results
recipes = dave.df_removeOutliers(recipes, ['calories', 'protein', 'fat', 'sodium'], 3)
recipes = dave.df_removeOutliers(recipes, ['calories', 'protein', 'fat', 'sodium'], 3)

# there are 2 drinks column. We need to combine into 1
recipes['isdrink'] = np.where((recipes['drinks'] == 0.0) & (recipes['drink'] == 0.0), 0.0, 1.0)

# drop the other drinks columns, as not required anymore
recipes = recipes.drop(columns=['drinks', 'drink'])

print(recipes['title'].loc[recipes['isdrink'] == 1])
# about 690 drinks recipes

#print(recipes.head(10))
#print(recipes.describe())

## data ready for the Machine learning part: how best to create the best model to predict if new recipe is a drink or not

# too many columns to do a correlation map
# too many colkumns for box plot charts
# get skew results from columns
# Skewness is a measure of the asymmetry of the probability distribution
# of variable about its mean.
# Check wikipedia on skewness and what postive/negative values mean:
# https://en.wikipedia.org/wiki/Skewness
print(' the skewness values')
print(recipes.skew(axis=0))

titles = recipes['title']
recipes = recipes.drop(columns=['title'])
print(' column title is dropped ')
# set target & features, train & test data
X = recipes[recipes.columns[0:-1]].to_numpy()  # all columns except isdrink
y = recipes[recipes.columns[-1]].to_numpy()  # the target isdrink column only

print(X.shape)  # should be 677 columns  (680 - 2 drinks dropped - 1 target)
print(y.shape)  # should be only 1 column

# split data into train and test sets.
# Q: Why is random seed set to 42?
# A: as "The Answer to the Ultimate Question of Life, the Universe, and Everything is 42"
# from The Hitchhiker's Guide to the Galaxy.

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print('test & train dataset assigned, now doing standard scaler')

#use StandardScaler to scale to unit variance.
# Reason: Standardization of a dataset is a common requirement for many machine learning estimators:
# they might behave badly if the individual features do not more or less look like
# standard normally distributed data (e.g. Gaussian with 0 mean and unit variance).


# I should also run it would a scaler and compare results.
sc = StandardScaler()
X_train = sc.fit_transform(X_train)
X_test = sc.transform(X_test)

# Training the classifiers on training set
# Create a custom function, to subsequently call a few times for different models
# we can then compare the success of each model

#create dictionary to add results into
accuracy_scores = {}

#define the function to call repeatedly
def predictor(predictor, params):
    global accuracy_scores
    if predictor == 'lr':
        print('Training Logistic Regression on Training Set')
        from sklearn.linear_model import LogisticRegression
        classifier = LogisticRegression(**params)

    elif predictor == 'svm':
        print('Training Support Vector Machine on Training Set')
        from sklearn.svm import SVC
        classifier = SVC(**params)

    elif predictor == 'knn':
        print('Training K-Nearest Neighbours on Training Set')
        from sklearn.neighbors import KNeighborsClassifier
        classifier = KNeighborsClassifier(**params)

    elif predictor == 'dt':
        print('Training Decision Tree Classifier on Training Set')
        from sklearn.tree import DecisionTreeClassifier
        classifier = DecisionTreeClassifier(**params)

    elif predictor == 'nb':
        print('Training Naive Bayes Classifier on Training Set')
        from sklearn.naive_bayes import GaussianNB
        classifier = GaussianNB(**params)

    elif predictor == 'rfc':
        print('Training Random Forest Classifier on Training Set')
        from sklearn.ensemble import RandomForestClassifier
        classifier = RandomForestClassifier(**params)

# now fit selected classifier on the dataset
    classifier.fit(X_train, y_train)

    # print('predicting a result drink/nodrink')
    # predict = classifier.predict(sc.transform([[   << need all column values here, but too many for now >>
    # ]]))
    # if single_predict > 0:
    #     print('is a Drink')
    # else:
    #     print('is not a Drink')
    #print('Predicting Test Set Result')
    #y_pred = classifier.predict(X_test)
    #result = np.concatenate((y_pred.reshape(len(y_pred), 1), y_test.reshape(len(y_test), 1)), 1)
    #print(result, '\n')
    print('Create confusion matrix')
    from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
    y_pred = classifier.predict(X_test)
    cm = confusion_matrix(y_test, y_pred)
    print(cm, '\n')
  #  plot_confusion_matrix(classifier, X_test, y_test, cmap="pink")
    print('True positives :', cm[0][0])
    print('False positives :', cm[0][1])
    print('False negatives :', cm[1][0])
    print('True negatives :', cm[0][1], '\n')

    #print('Classification Report')
    #print(classification_report(y_test, y_pred,target_names=['0', '1'], zero_division=1))

    print('Evaluating model performance')
    accuracy = accuracy_score(y_test, y_pred)
    print(accuracy, '\n')
# add to dictionary
    accuracy_scores[classifier] = accuracy * 100

    ## commented out because takes TOO long to run ##
    ## and I have evinced this learning in file 1_4 ##
    # print('do K-Fold cross validation')
    # from sklearn.model_selection import cross_val_score
    # accuracies = cross_val_score(estimator=classifier, X=X_train, y=y_train, cv=5)
    # print("accuracy: {:.2f} %".format(accuracies.mean() * 100))
    # accuracy_scores[classifier] = accuracies.mean() * 100

# Now run a few different classifiers
# and append the accuracy score to the accuracy_scores list
# we can then compare which one is most accurate

# 1. Logistic Regression
print('FIRST CLASSIFIER MODEL: LR')
predictor('lr', {'penalty': 'l1', 'solver': 'liblinear'})
# 2. SVM kernel = linear
print('SECOND CLASSIFIER MODEL: SVM-1')
predictor('svm', {'C': .5, 'gamma': 0.8, 'kernel': 'linear', 'random_state': 0})
# 3. SVM kernel = rbf
print('THIRD CLASSIFIER MODEL: SVM-2')
predictor('svm', {'C': .25, 'gamma': 0.1, 'kernel': 'rbf', 'random_state': 0})
# 4. KNN
print('FOURTH CLASSIFIER MODEL: KNN')
predictor('knn', {'algorithm': 'auto', 'n_jobs': 1, 'n_neighbors': 8, 'weights': 'distance'})
# 5. Decision tree
print('FIFTH MODEL: DT')
predictor('dt', {'criterion': 'entropy', 'max_features': 'auto', 'splitter': 'best', 'random_state': 0})
# 6. Naive Bayes
print('SIXTH MODEL: Bayes')
predictor('nb', {})
# 7. Random Forrest
print('SEVENTH MODEL: Random Forrest')
predictor('rfc', {'criterion': 'gini', 'max_features': 'log2', 'n_estimators': 100,'random_state':0})


# which Classifier has the best accuracy
maxKey = max(accuracy_scores, key=lambda x: accuracy_scores[x])
print('The model with highest accuracy score is  {0} with an accuracy of  {1:.2f}'.format(maxKey, accuracy_scores[maxKey]))

# Create chart for accuracy of the classifiers
plt.figure(figsize=(12, 6))
model_accuracies = list(accuracy_scores.values())
model_names = ['LogisticRegression', 'SVC',
               'K-SVC', 'KNN', 'Decisiontree', 'NBayes', 'RandomForest']
sns.barplot(x=model_accuracies, y=model_names, palette='YlGn')
plt.title('Accuracy scores per model')
plt.show()

