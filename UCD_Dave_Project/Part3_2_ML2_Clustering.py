#unsupervised learning
# clustering
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# set number of cluster here, easier for re-running different values
nr_clusters = 3

#import to dataframe
df_samples = pd.read_csv('Data_files/Wine.csv')
#print(df_samples.shape)

#STEP 1 - Histogram of all measures to observe any particular strange things
#.... and just'to try'

#1.1 create the canvas for the charts
## NOTE- COMMENTED OUT TO SPEED UP SCRIPT IN SUBSEQUENT EXECUTIONS ##
    ##fig, axes = plt.subplots(ncols=3,nrows=5, figsize=(12,10))

#1.2 Fix error -AttributeError: 'numpy.ndarray' object has no attribute 'get_figure'
    #axe = axes.ravel()  # I dont know what it does, but it fixes it.

#1.3 draw chart for each column
##for col, ax in zip(df_samples, axe):
 ##   #ax.set_xticklabels([])
 ##   #ax.set_xticks([])  #it was messing up the charts, although end-result still not good
 ##   df_samples[col].value_counts().sort_index().plot.bar(ax=ax, title=col)
##plt.tight_layout()
##plt.show()

#1.4 chart shows customer segment column is out of place as already a cluster. Drop.
df_samples = df_samples.drop(columns=['Customer_Segment'])

# STEP 2 - Clustering
# 2.1 Convert to numpy array for clustering
np_samples = df_samples[df_samples.columns[0:13]].to_numpy()
#print(np_samples.shape)
#print(np_samples)

# 2.2 Initiate clustering model: 3 clusters to start with
model = KMeans(n_clusters=nr_clusters)
# fit model on array
model.fit(np_samples)

# use model to predict
label = model.predict(np_samples)
print(label)

#STEP 3 - centroids & chart
# get the cluster centers (called Centroids)
centroids = model.cluster_centers_
#print(model.cluster_centers_)

# plot any 2 columns of array on scatter chart and see the cluster-label
xs = np_samples[:,2]  # any column of the array
ys = np_samples[:,12]  # any other column of the array
plt.scatter(xs, ys, c=label)
plt.scatter(centroids[:,2] , centroids[:,12] , marker='D', s = 100, color = 'red') #NOTE: use same columns here of course
plt.show()

#STEP 4: if you have new data set: apply model to new datasets

new_samples = np.array([18,2,2.5,11,100,2.8,3,0.3,2,5,0.9,3,1250])
new_samples = new_samples.reshape(1,-1)
# apply model on new values
new_labels = model.predict(new_samples)
print('the new sample applied to model.. is part of cluster: ')
print(new_labels)

#STEP 4: measure inertia
ks = range(1, 10)
inertias = []

for k in ks:
    # Create a KMeans instance with k clusters: model
    model = KMeans(n_clusters=k)

    # Fit model to samples
    model.fit(np_samples)

    # Append the inertia to the list of inertias
    inertias.append(model.inertia_)

# Plot ks vs inertias
plt.plot(ks, inertias, '-o')  #-o is the marker and line to connect the markers.
plt.xlabel('number of clusters, k')
plt.ylabel('inertia')
plt.xticks(ks)
plt.show()

#NOTE, looking at chart, at 'the elbow', 3 or 4 clusters is probably best




# new_samples = {
#    'Alcohol':14,
#     'Malic_Acid':2,
#     'Ash':2.5,
#     'Ash_Alcanity': 11,
#     'Magnesium': 100,
#     'Total_Phenols': 2.8,
#     'Flavanoids': 3,
#     'Nonflavanoid_Phenols':0.3,
#     'Proanthocyanins':2,
#     'Color_Intensity': 5,
#     'Hue':0.9,
#     'OD280': 3,
#     'Proline': 1250
# }

