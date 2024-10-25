import numpy as np
import networkx as nx

def generate_cities(n):
    return np.random.rand(n, 2) * 100  # n villes sur une carte 100x100

def distance_matrix(cities):
    n = len(cities)
    dist_matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(i + 1, n):
            dist = np.linalg.norm(cities[i] - cities[j])
            dist_matrix[i, j] = dist_matrix[j, i] = dist
    return dist_matrix
