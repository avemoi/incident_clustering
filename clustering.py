import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from sklearn.cluster import AgglomerativeClustering


def agglomerative(data, distance):
    hierarchical_cluster = AgglomerativeClustering(distance_threshold=distance, affinity='euclidean', linkage='ward', n_clusters=None)
    labels = hierarchical_cluster.fit_predict(data)
    x = [tup[0] for tup in data]
    y = [tup[1] for tup in data]

    plt.scatter(x ,y, c=labels)
    # print(data)
    print(labels)
    # for i in np.unique(labels):
        # cluster = data[labels==i]
        # print(cluster)
        # mean = np.mean(cluster, axis=0)
        # radius = np.max(np.linalg.norm(cluster - mean, axis=1))
        # circle = plt.Circle(mean, radius, color='black', fill=False)
        # plt.gca().add_artist(circle)

    plt.show()

def linage(data):
    linkage_data = linkage(data, method='ward', metric='euclidean')
    dendrogram(linkage_data)
    plt.show()