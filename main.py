from fastapi import FastAPI
from db import get_all_coordinates
from sklearn.cluster import AgglomerativeClustering
import numpy as np

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
    cluster_centers = []
    for current_class in available_clusters:
        samples = data_array[labels == current_class]
        cluster_center = np.mean(samples, axis=0)
        cluster_centers.append(tuple(cluster_center))
    return cluster_centers


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
