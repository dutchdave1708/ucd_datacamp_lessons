# ** notes from Data Camp cleaning chapter // useful comments **
# sales is een csv file ingelezen in een Panda dataframe
#read header
sales.header(2) # 2 rows
sales.dtypes # show datatypes of columns
sales.info() # show info on columns, missing values, etc
sales.['ColumnName'].describe() # gives various info on that column. depends on type
sales['ColumnName'].sum()  # sums all columns in that columnname. if string: concatenates. if int/float: sums
#remove a character from a strong
sales['Columnname'] = Sales['ColumnName'].str.strip('$')  # strips character $
sales['Columnname'] = Sales['ColumnName'].astype(int)  # change datatype to int
assert sales['ColumnName'].dtype == 'int'  #verify if now int.

##  cleaning up date in categories
# White spaces & inconsistencies: .str.upper() / .str.strip() / .str.lower()
# Categories : pandas.cut() / .replace() / pandas.qcut()

##  replacing two columns with new columns and categories
# Create ranges for categories
label_ranges = [0, 60, 180,np.inf]
label_names = ['short', 'medium', 'long']

# Create wait_type column from wait_min column
airlines['wait_type'] = pd.cut(airlines['wait_min'], bins = label_ranges, labels = label_names)

# Create mappings and replace
mappings = {'Monday':'weekday', 'Tuesday':'weekday', 'Wednesday': 'weekday', 'Thursday': 'weekday', 'Friday': 'weekday', 'Saturday': 'weekend', 'Sunday': 'weekend'}
#create day_week column from day column
airlines['day_week'] = airlines['day'].replace(mappings)

## replacing values with nothing
# Replace "Miss" with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Miss", "")
# Replace "Ms." with empty string ""
airlines['full_name'] = airlines['full_name'].str.replace("Ms.", "")
# Assert that full_name has no honorifics
assert airlines['full_name'].str.contains('Ms.|Mr.|Miss|Dr.').any() == False

### download netflix_titles.csv from Kaggle
# drag & drop into UCD_Dave1 project

#import pandas to work with data sets
import pandas as pd

#import the netflix data file
netflix_data = pd.read_csv("netflix_titles.csv")

# show first few rows and some columns
print(netflix_data.head())
    #you can set parameter to show all rows & columns
    #pd.options.display.max_columns = 12  #use None for all
    #pd.options.display.max_rows = 10    #use None for all
    #print(netflix_data.head())
        # set back to default
        # pd.options.display.max_columns = 5
        #pd.options.display.max_rows = 5

# show all  columns headers
print(netflix_data.columns.values)

# show number of rows and columns
print(netflix_data.shape)

# count missing values per row
missing_values_count = netflix_data.isnull().sum()
print(missing_values_count[:12])  # rows:columns, so e.g. use [0:12] for all rows and first 12 columns

# drop rows where data is missing
    #droprows= netflix_data.dropna()  #axis=0
    #print(netflix_data.shape,droprows.shape)

# drop columns where data is missing
    #droprows= netflix_data.dropna(axis=1)
    #print(netflix_data.shape,droprows.shape)

# fill all empty  values with 0
    #cleaned_data = netflix_data.fillna(0)
# fill all empty column values with that comes in the next column
    #cleaned_data = netflix_data.fillna(method='bfill', axis=0).fillna(0)

##  replace values via loc on dataframes
# Find values of acct_cur that are equal to 'euro'
acct_eu = banking['acct_cur'] == 'euro'

# Convert acct_amount where it is in euro to dollars
banking.loc[acct_eu, 'acct_amount'] = banking.loc[acct_eu, 'acct_amount'] * 1.1


# Unify acct_cur column by changing 'euro' values to 'dollar'
banking.loc[acct_eu, 'acct_cur'] = 'dollar'

# Assert that only dollar currency remains
assert banking['acct_cur'].unique() == 'dollar'