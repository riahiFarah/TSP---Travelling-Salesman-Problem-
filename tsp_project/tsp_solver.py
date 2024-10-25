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


def tsp_with_constraints(cities, dist_matrix, time_windows, vehicle_capacity, demands, blocked_routes, max_distance):
    # Initialisation du graphe
    G = nx.Graph()
    n = len(cities)
    
    # Ajout des arêtes aux graphes, sauf pour les routes impraticables
    for i in range(n):
        for j in range(i + 1, n):
            if (i, j) not in blocked_routes:
                G.add_edge(i, j, weight=dist_matrix[i, j])

    # Fonction pour vérifier si une ville peut être visitée dans sa fenêtre temporelle
    def is_within_time_window(city, current_time):
        return time_windows[city][0] <= current_time <= time_windows[city][1]
    
    # Fonction pour vérifier la capacité du véhicule
    def has_sufficient_capacity(current_capacity, city):
        return current_capacity >= demands[city]

    # Algorithme simple pour résoudre le TSP avec contraintes
    current_city = 0
    visited = [False] * n
    visited[0] = True
    tour = [0]
    total_distance = 0
    current_time = 0
    current_capacity = vehicle_capacity
    rest_stop_threshold = max_distance / 2  # Distance après laquelle un arrêt de repos est nécessaire
    distance_since_last_stop = 0

    while len(tour) < n:
        # Recherche de la ville la plus proche non visitée respectant les contraintes
        next_city = None
        min_distance = float('inf')
        for i in range(n):
            if not visited[i] and has_sufficient_capacity(current_capacity, i):
                if is_within_time_window(i, current_time):
                    dist = dist_matrix[current_city, i]
                    if dist < min_distance and (current_city, i) not in blocked_routes:
                        min_distance = dist
                        next_city = i
        
        if next_city is None:
            raise ValueError("Aucune ville n'est accessible en respectant les contraintes.")
        
        # Mettre à jour l'état du parcours
        tour.append(next_city)
        visited[next_city] = True
        total_distance += min_distance
        current_time += min_distance / 50  # Exemple de vitesse : 50 unités de distance par unité de temps
        current_capacity -= demands[next_city]
        distance_since_last_stop += min_distance

        # Si on dépasse la distance maximale, un arrêt est requis
        if distance_since_last_stop > rest_stop_threshold:
            print(f"Arrêt de repos requis après avoir parcouru {distance_since_last_stop} unités.")
            current_time += 1  # On ajoute une unité de temps pour l'arrêt
            distance_since_last_stop = 0

        current_city = next_city
    
    # Retour à la ville de départ pour compléter le cycle
    total_distance += dist_matrix[current_city, 0]
    tour.append(0)
    
    return tour, total_distance
