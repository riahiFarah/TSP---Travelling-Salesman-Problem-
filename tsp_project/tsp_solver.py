import numpy as np
import networkx as nx

def generate_cities(n):
    return np.random.rand(n, 2) * 100  # n villes sur une carte 100x100
