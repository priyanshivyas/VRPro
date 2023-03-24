from vrp_utils import calculate_distance, find_nearest_customer
import numpy as np
import argparse

# def solve_vrp(customer_locations, num_vehicles):
#     """
#     Solve the Vehicle Routing Problem using the nearest neighbor algorithm
#     """
#     num_customers = len(customer_locations) - 1 # Substract 1 from the length.
#     visited_customers = set()
#     vehicle_routes = [[] for _ in range(num_vehicles)]

#     # Start at the first customer location for each vehicle
#     current_location = [customer_locations[i] for i in range(num_vehicles)]

#     # Loop through all customers and add to the nearest vehicle
#     while len(visited_customers) < num_customers:
#         for i, location in enumerate(current_location):
#             if len(visited_customers) == num_customers:
#                 break
#             nearest_customer = find_nearest_customer(location, customer_locations, visited_customers)
#             vehicle_routes[i].append(nearest_customer)
#             visited_customers.add(nearest_customer)

#             # Update current location to nearest customer
#             current_location[i] = customer_locations[nearest_customer]

#     return vehicle_routes

class VRP:
    def __init__(self, num_customers, customer_locations, num_vehicles):
        self.num_customers = num_customers
        self.customer_locations = customer_locations
        self.num_vehicles = num_vehicles


def solve_vrp(customer_locations, num_vehicles):
    # Initialize solution
    solution = [[] for i in range(num_vehicles)]
    unvisited_customers = set(range(len(customer_locations)))
    visited_customers = set()

    # Iterate over vehicles
    for vehicle in range(num_vehicles):
        # Select random customer as starting point
        current_customer = np.random.choice(list(unvisited_customers))
        while True:
            # Remove current customer from unvisited set and add to visited set
            unvisited_customers.remove(current_customer)
            visited_customers.add(current_customer)

            # Add current customer to current vehicle route
            solution[vehicle].append(current_customer)

            # Find nearest unvisited customer to current customer
            nearest_customer = find_nearest_customer(customer_locations[current_customer],
                                                      customer_locations,
                                                      visited_customers)
            if nearest_customer is None:
                # No more unvisited customers, end route
                break

            current_customer = nearest_customer

        print('Route {} :'.format(vehicle), solution[vehicle])

    return solution


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



