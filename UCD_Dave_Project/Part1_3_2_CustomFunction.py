## Create custom function

# Custom Function template
    #def <function_name>([<parameters>]):
    #<statement(s)>

#libraries used later
import pandas as pd
import numpy as np


#practice with basic function
def setvariable (anumber, alist):
    y = anumber
    print(type(alist))
    return y

anumber = 50
y_new = setvariable(anumber,['test', 'a', 'list'])
print (y_new)

#  Define function to drop duplicates of provided dataframe and clear Nulls

def cleandataset(dataframe, key_columnname, columnslist, nrstdv):
     #print(dataframe.info())
     print('step 1: remove duplicates on key_column')
     #print(key_columnname)
     dataframe = dataframe.drop_duplicates([key_columnname], ignore_index=True)  # reset index 0 to n-1
     #print('values after removing duplicates')
     #print(dataframe.info())
     print('step 2: remove Nulls')
     df_no_outliers = dataframe.dropna() #remove rows with Nulls
     #print('values after removing Nulls')
     #print(df_no_outliers.info())
     print('step 3: clean up for range of columns provided')
     for columnname in columnslist:
         print(columnname)
         df_no_outliers = df_no_outliers[np.abs(df_no_outliers[columnname] - df_no_outliers[columnname].mean()) <= (
                 nrstdv * df_no_outliers[columnname].std())]
     #print('finished with iterator')
     #print(df_no_outliers.info())
     return (df_no_outliers)

def dropcolumns(dataframe, columnlist):
    newdf = dataframe.drop([columnlist], axis=1)
    return(newdf)

#try it out
df = pd.read_csv('Data_files/epi_r.csv')
print(df.info())
print('call function')
df_clean = cleandataset(df, 'title',['calories', 'sodium', 'fat', 'protein'],2)
print('finished calling the function')
print(df_clean.info())







