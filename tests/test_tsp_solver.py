import unittest
import numpy as np
from tsp_solver import tsp_with_constraints, generate_cities, distance_matrix 
from utils import generate_time_windows

class TestTSPSolver(unittest.TestCase):
    def setUp(self):
        # Configuration de test
        self.cities = generate_cities(5)
        self.dist_matrix = distance_matrix(self.cities)
        self.time_windows = generate_time_windows(5)
        self.vehicle_capacity = 10
        self.demands = [2, 1, 3, 2, 1]
        self.blocked_routes = [(1, 3), (2, 4)]
        self.max_distance = 50

    def test_tsp_with_constraints(self):
        tour, total_distance = tsp_with_constraints(
            self.cities, self.dist_matrix, self.time_windows,
            self.vehicle_capacity, self.demands, self.blocked_routes,
            self.max_distance
        )
        # Vérifier que la tournée renvoyée est valide
        self.assertTrue(len(tour) > 0, "La tournée ne doit pas être vide.")
        self.assertTrue(total_distance > 0, "La distance totale doit être supérieure à zéro.")

if __name__ == "__main__":
    unittest.main()
