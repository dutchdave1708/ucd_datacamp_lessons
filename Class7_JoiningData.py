# session 7
# print('session on 6 Oct is about joining data sets. Not as title suggests about Date&Times')
# different types of joining data sets

#print('concat() is a simple combining method, joins elements together along an axis')
print('Lesson 7')
#if you have 2 csvs

# syntax is merged_data= p.merge(leftdataframe, rightdataframe, on='columnname')
#print(left.shape, right, shape) - to understand shapes for the 2 dataframes
#print(joined_data.shape, merged_data.shape)
import pandas as pd
CAvideos = pd.read_csv('CAvideos.csv')
GBvideos = pd.read_csv('GBvideos.csv')

concat_data = pd.concat([CAvideos, GBvideos])
print(concat_data.shape)

left = CAvideos.set_index(['title', 'trending_date'])
right = GBvideos.set_index(['title', 'trending_date'])
joined_data = left.join(right, lsuffix='_CAN', rsuffix='_UK')

merged_data= pd.merge(CAvideos,GBvideos [['video_id','views','likes','dislikes']], on='video_id', how='left')
print(CAvideos.shape, GBvideos.shape)
print(merged_data.shape, joined_data.shape)
#left/right/outer

