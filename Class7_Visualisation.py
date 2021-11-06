# download/ import  the right package
import matplotlib.pyplot as plt  #matplot is a large library, so just download a subset
import pandas as pd # import pandas library

fig,ax = plt.subplots()  # creates empty canvas

#plt.show()  # show canvas

#x=[1,2,3,4,5]
#y=[1,2,3,4,5]

data = pd.read_csv("GBvideos.csv")  #downlaoded from Kaggle, stored locally

#print(data.head())
#print(data.info)
#print(list(data))  #list the column headers in order

#set values for axis
x = data['channel_title'].head(10)
y1 = data['views'].head(10)
#y2 = data['likes'].head(5)

#ax.plot(x, y1)
#ax.plot(x, y2)

#plt.show()

# create a few different charts from this dataset
# downloaded from matplotlib.org

#labels = ['G1', 'G2', 'G3', 'G4', 'G5']
#men_means = [20, 35, 30, 35, 27]
#women_means = [25, 32, 34, 20, 25]
#men_std = [2, 3, 4, 1, 2]
#women_std = [3, 5, 2, 3, 3]
width = 0.35       # the width of the bars: can also be len(x) sequence

#fig, ax = plt.subplots()

ax.bar(x, y1, width, label='Title')  #yerr=men_std
#ax.bar(labels, women_means, width, yerr=women_std, bottom=men_means, label='Women')

ax.set_ylabel('Views')
ax.set_xlabel('Shows')
ax.set_title('Views by title')
ax.legend()

plt.show()



