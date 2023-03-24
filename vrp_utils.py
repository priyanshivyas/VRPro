import numpy as np
import csv

def load_data(filename):
    """
    Load customer locations from a CSV file
    """
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header row
        customer_locations = []
        for row in reader:
            customer_locations.append([float(row[0]), float(row[1])])
        return np.array(customer_locations)

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

def nearest_neighbor(curr_customer, distance_matrix, capacity):
    nearest_customer = np.argmin(distance_matrix[curr_customer][1:] + np.where(capacity < 1e-8, np.inf, 0)) + 1
    return nearest_customer


