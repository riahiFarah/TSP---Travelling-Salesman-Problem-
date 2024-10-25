import numpy as np

def generate_time_windows(n):
    return [(np.random.randint(0, 5), np.random.randint(5, 10)) for _ in range(n)]
