# Numpy array primarily should be used for numbers
# Pandas dataframes are ideal for mixed data types / strings
#delimiter changes the delimiter that loadtxt() is expecting.
#You can use ',' for comma-delimited.
#You can use '\t' for tab-delimited.
#skiprows allows you to specify how many rows (not indices) you wish to skip
#usecols takes a list of the indices of the columns you wish to keep.


# Open a file: file
file = open('DataCamp_text.txt', mode='r')

# Print it
print(file.read())

# print only a few lines
# Read & print the first 3 lines
with open('DataCamp_text.txt') as file :
    print(file.readline())
    print(file.readline())
    print(file.readline())

# Check whether file is closed
print(file.closed)

# Close file
file.close()

# Check whether file is closed
print(file.closed)


# Load a sheet into a DataFrame by name: df1
df1 = xls.parse('2004')  # sheet name
# Load a sheet into a DataFrame by index: df2
df2 = xls.parse(0)  # use by index

# Print the head of the DataFrame df2
print(df2.head())

# Import packages
import numpy as np
import h5py

# Assign filename: file
file = 'LIGO_data.hdf5'

# Load file: data
data = h5py.File(file, 'r')

# Print the datatype of the loaded file
print(type(data))

# Print the keys of the file
for key in data.keys():
    print(key)

#Connecting to a database
# import packages and functions
#create the data engine
# Connect to the engine
# Query the database
# Save the query results to a DataFrame
# # set columns names to keys from table.
# Close the connection

Exmaples

# Create engine: engine
engine = create_engine('sqlite:///Chinook.sqlite')

# Open engine in context manager
# Perform query and save results to DataFrame: df
with engine.connect() as con:
    rs = con.execute('Select * from Employee WHERE EmployeeId >= 6')
    df = pd.DataFrame(rs.fetchall())
    df.columns = rs.keys()

# Print the head of the DataFrame df
print(df.head())