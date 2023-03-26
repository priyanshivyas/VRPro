import numpy as np
import csv

customer_demands = []
def load_data(filename):
    """
    Load customer locations and demands from a CSV file
    """
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        next(reader)  # skip header row
        customer_locations = []
        for row in reader:
            customer_locations.append([float(row[0]), float(row[1])])
            customer_demands.append(int(row[2]))
        return np.array(customer_locations), np.array(customer_demands)

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

def nearest_neighbor(curr_location, distance_matrix, remaining_capacity, unvisited_customers):
    valid_customers = [i for i in unvisited_customers if remaining_capacity >= customer_demands[i]]
    if not valid_customers:
        return None
    distances = distance_matrix[curr_location][valid_customers]
    return valid_customers[np.argmin(distances)]


