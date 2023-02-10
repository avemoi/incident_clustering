from fastapi import FastAPI
from db import get_all_coordinates
from sklearn.cluster import AgglomerativeClustering
import numpy as np
from helpers import get_circle_points
app = FastAPI()



@app.get("/")
async def root():
    distance = 0.0001
    data = get_all_coordinates()
    hierarchical_cluster = AgglomerativeClustering(distance_threshold=distance, affinity='euclidean', linkage='ward',
                                                   n_clusters=None)
    labels = hierarchical_cluster.fit_predict(data)

    data_array = np.array(data)
    available_clusters = np.unique(labels)
    cluster_center_rad_circle = []
    for current_class in available_clusters:
        samples = data_array[labels == current_class]
        cluster_center = np.mean(samples, axis=0)
        cluster_radius = np.max(np.linalg.norm(samples - cluster_center, axis=1))
        array_to_list = list(cluster_center)
        array_to_list.append(cluster_radius)
        cluster_center_rad_circle.append(array_to_list)

    for cluster in cluster_center_rad_circle:
        cluster.append(get_circle_points([cluster[0],cluster[1]], cluster[2]))


    return cluster_center_rad_circle


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
