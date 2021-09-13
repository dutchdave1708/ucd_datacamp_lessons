# Class 2
# Types: boolean, integer, string, float
# Cover: indexing, tuples/lists, indexing, slicing
# tuple, list, dictionary
# tuple = a=(1,2,3,True)
# list = a=[1,2,3,True]
# dictionary = a={"id":1, "Value":"yes"}
# tuple/string: cannot update values.
# dictionary: can provide labels to values
# Pandas is a collection of arrays
# Assignment, to download a CSV, import into PyCharm and read the CSV
# select from list , do list[indexnumber], or range list[index:index]
# select from list of lists, do list[index][indexofsublist]
print("session2")

import pandas as pd
# downloaded the winemag.csv file from Kaggle onto local machine

df=pd.read_csv("winemag-data-130k-v2.csv")

print(type(df))
print(df.info())
print(df)

# finished the Intermediary Python course bar the case study at the end
