# just a simple evidence of accessing data from sql database using Python

# 1 - created database on AWS via freesqldatabase.com
# 2 - create table Testdata
# 3 - and added a few rows of content via phpMyAdmin.co interface
# 4 - create 2nd table Anewtable via this script
# 5 - inserted a row of data
# 6 - extracted data via a SQL statement and a function.

# Connect and retrieve data
import pandas as pd
import sqlalchemy as db
from sqlalchemy import create_engine
from sqlalchemy import insert
from sqlalchemy import Table, Column, Integer, String, MetaData

# sql4.freesqldatabase.com
# account: sql4450835
# database: sql4450835

# create DB connection details
engine = create_engine('mysql://sql4450835:69RIi1YeYI@sql4.freesqldatabase.com/sql4450835')
connection = engine.connect()

#create SQL statement to execute
sql = "SELECT * FROM Testdata WHERE WebId IN (1,2)"
# connect and extract data into dataframe (convert from standard output List type)
df = pd.read_sql_query(sql, engine)
print(df)

# create a table via this Python interface
meta = MetaData()
Anewtable = Table(
   'Anewtable', meta,
   Column('id', Integer, primary_key = True),
   Column('Anumber', Integer),
   Column('lastname', String(32)),
)
#create the table with info stored in meta object, via specific db connect engine
meta.create_all(engine)

#print(engine.select(['Anewtable']))

#Inserting one record
# NOTE: runs only once, as primary key on id.
# I know I should add a IF EXIST statement around this.
query = db.insert(Anewtable).values(id=1, Anumber=1, lastname='MyOwnlastname')
#Result = connection.execute(query)
#print(Result)

# show values from table (essentially a select * from)
results = connection.execute(db.select([Anewtable])).fetchall()
print(results)  # returns a list
print(type(results))
df = pd.DataFrame(results)
print(df)  #returns a dataframe


# Do a join statement
sql = "SELECT Testdata.WebID, Anewtable.lastname FROM Testdata  JOIN Anewtable ON Testdata.WebID = Anewtable.id WHERE Testdata.WebId IN (1,2)"
df = pd.read_sql_query(sql, engine)
print(df)

#INSERT INTO
# `Testdata`
# (`WebID`, `Webpage`, `Content`, `UpdateDate`)
# VALUES ('1', 'www.nu.nl', 'Dutch news website.', '2021-11-13'),
# ('2', 'www.bbc.co.uk', 'UK news website', '2021-11-13');