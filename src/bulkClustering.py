import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
from pathlib import Path

# Cluster Function, runs k-means clustering and saves the results (cluster) to a new column in the dataframe
def cluster(gridPoints, NUM_CLUSTERS, MIN_SCORE_THRESHOLD):
    clusteredGridPoints = gridPoints.copy()
    clusteredGridPoints = clusteredGridPoints.loc[clusteredGridPoints['score'] > MIN_SCORE_THRESHOLD]
    kmeans = KMeans(n_clusters=NUM_CLUSTERS, random_state=0).fit(clusteredGridPoints[["lat", "long"]], 0, clusteredGridPoints["score"])
    clusteredGridPoints['cluster'] = kmeans.labels_.tolist()
    return clusteredGridPoints

# Sort Cluster Function, sorts clusters by the average of scores contained in that cluster.
# i.e. we have to sort the clusters so that downtown (the densest area with highest score) is cluster 0, next dense is cluster 1, etc.
def sortClustersByScore(gridPoints, NUM_CLUSTERS):
    clusteredGridPoints = gridPoints.copy()
    clusterScoreSums = []
    for i in range(NUM_CLUSTERS):
        selectedCluster = gridPoints.loc[gridPoints['cluster'] == i]
        clusterScoreSums.append(selectedCluster['score'].mean())
    sortIndiciesDescending = np.argsort(clusterScoreSums)[::-1][:NUM_CLUSTERS].flatten()
    newClusters = {k: v for v, k in enumerate(sortIndiciesDescending)}
    clusteredGridPoints['cluster'] = gridPoints['cluster'].map(newClusters)
    return clusteredGridPoints

def exportClusteredGridPointsToCsv(gridPoints, name):
    filepath = Path('../res/grid_points/' + name + '.csv')
    filepath.parent.mkdir(parents=True, exist_ok=True)
    gridPoints.to_csv(filepath)

def runClustering(city, STD_DEV, numClusters):
    GridPoints = pd.read_csv('../res/grid_points/' + city + '_grid_points_' + str(STD_DEV) + '.csv', sep = ',')

    NUM_CLUSTERS = numClusters
    MIN_SCORE_THRESHOLD = 0.5 # minimum score to be considered in the clustering

    # Clustered `Grid Points` is a subset of `Grid Points` with only entries with a score > MIN_SCORE_THRESHOLD, with a cluster column added
    Clustered_GridPoints = cluster(GridPoints, NUM_CLUSTERS, MIN_SCORE_THRESHOLD)
    Clustered_GridPoints = sortClustersByScore(Clustered_GridPoints, NUM_CLUSTERS)

    exportClusteredGridPointsToCsv(Clustered_GridPoints, city + '_clustered_grid_points_' + str(STD_DEV) + '_' + str(numClusters))

for c in range(1, 11):
    #runClustering("yyz", 0.9, c)
    #runClustering("yvr", 0.9, c)
    #runClustering("yyc", 0.9, c)
    runClustering("ygk", 0.9, c)
#%%
