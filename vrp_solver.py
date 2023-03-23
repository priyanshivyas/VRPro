from vrp_utils import calculate_distance, find_nearest_customer
import numpy as np
import argparse

def solve_vrp(customer_locations, num_vehicles):
    """
    Solve the Vehicle Routing Problem using the nearest neighbor algorithm
    """
    num_customers = len(customer_locations) - 1 # Substract 1 from the length.
    visited_customers = set()
    vehicle_routes = [[] for _ in range(num_vehicles)]

    # Start at the first customer location for each vehicle
    current_location = [customer_locations[i] for i in range(num_vehicles)]

    # Loop through all customers and add to the nearest vehicle
    while len(visited_customers) < num_customers:
        for i, location in enumerate(current_location):
            if len(visited_customers) == num_customers:
                break
            nearest_customer = find_nearest_customer(location, customer_locations, visited_customers)
            vehicle_routes[i].append(nearest_customer)
            visited_customers.add(nearest_customer)

            # Update current location to nearest customer
            current_location[i] = customer_locations[nearest_customer]

    return vehicle_routes

if __name__ == '__main__':
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Solve the Vehicle Routing Problem using the nearest neighbor algorithm')
    parser.add_argument('--num_customers', type=int, help='Number of customers', required=True)
    parser.add_argument('--customer_locations', type=str, help='List of customer locations', required=True)
    parser.add_argument('--num_vehicles', type=int, help='Number of vehicles', required=True)
    args = parser.parse_args()

    # Load input data
    customer_locations = np.fromstring(args.customer_locations, sep=' ').reshape(args.num_customers, 2)

    # Solve the problem
    solution = solve_vrp(customer_locations, args.num_vehicles)

    # Print solution
    print('Vehicle routes:', solution)
    print('Number of vehicles:', len(solution))



