import numpy as np

def calculate_distance(x1, y1, x2, y2):
    """
    Calculate the Euclidean distance between two points
    """
    return np.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

def find_nearest_customer(location, customer_locations, visited_customers):
    """
    Find the nearest unvisited customer to a given location
    """
    shortest_distance = np.inf
    nearest_customer = None
    for i, customer_location in enumerate(customer_locations):
        if i not in visited_customers:
            distance = calculate_distance(location[0], location[1],
                                           customer_location[0], customer_location[1])
            if distance < shortest_distance:
                shortest_distance = distance
                nearest_customer = i
    return nearest_customer

