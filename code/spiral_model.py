
import numpy as np

def q(n):
    return 0.15 * n

def curvature(n):
    return 18.69 / n + 0.172

def get_coordinates(n_values):
    coords = []
    for n in n_values:
        c = curvature(n)
        x = np.cos(c * n + q(n))
        y = np.sin(c * n + q(n))
        coords.append((n, x, y))
    return coords
