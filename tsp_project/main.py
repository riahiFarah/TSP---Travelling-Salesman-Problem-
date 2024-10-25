from tsp_solver import tsp_with_constraints, generate_cities, distance_matrix
from utils import generate_time_windows

# Exemple d'utilisation
cities = generate_cities(5)
dist_matrix = distance_matrix(cities)
time_windows = generate_time_windows(5)
vehicle_capacity = 10
demands = [1, 1, 1, 1, 1]  # Moins de demandes pour chaque ville
blocked_routes = [(1, 3)]  # Réduire le nombre de routes impraticables
max_distance = 150  # Augmenter la distance maximale possible pour chaque segment

# Appel de la fonction tsp_with_constraints
tour, total_distance = tsp_with_constraints(cities, dist_matrix, time_windows, vehicle_capacity, demands, blocked_routes, max_distance)

# Affichage des résultats
print(f"Tournée: {tour}, Distance totale: {total_distance}")
