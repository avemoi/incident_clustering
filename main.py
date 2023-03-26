from fastapi import FastAPI
from db import get_all_coordinates
from clustering import get_clusters_number

app = FastAPI()


@app.get("/")
async def root(time_window: int, distance_in_m: int = 20, cluster_threshold: int = 1):
    data = get_all_coordinates(time_window)
    cluster_number = get_clusters_number(distance_in_m, data)
    if cluster_number > cluster_threshold:
        return {"send": 1}
    return {"send": 0}
