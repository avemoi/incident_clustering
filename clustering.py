import numpy as np
from sklearn.cluster import DBSCAN


def get_clusters_number(distance_in_meters, data):
    meters_per_radian = 6371000
    distance_in_meters = distance_in_meters  # e.g. 20m
    epsilon = distance_in_meters / meters_per_radian
    db = DBSCAN(
        eps=epsilon, min_samples=1, algorithm="ball_tree", metric="haversine"
    ).fit(np.radians(data))
    cluster_labels = db.labels_
    num_clusters = len(set(cluster_labels))
    return num_clusters
