import numpy as np

def get_circle_points(center, radius):
    t = np.linspace(0, 2 * np.pi, 100)
    x = float(center[0]) + float(radius) * np.cos(t)
    y = float(center[1]) + float(radius) * np.sin(t)
    points = [(x[i], y[i]) for i in range(len(x))]
    return points