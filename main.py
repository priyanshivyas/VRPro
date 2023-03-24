import argparse
import numpy as np
from vrp_solver import VRPSolver
from vrp_utils import load_data


def main():
    parser = argparse.ArgumentParser(description='Vehicle Routing Problem')
    parser.add_argument('--num_customers', type=int, default=14, help='Number of customers (default: 14)')
    parser.add_argument('--customer_locations', type=str, default='customers.csv', help='Path to customer locations CSV file (default: customers.csv)')
    parser.add_argument('--num_vehicles', type=int, default=3, help='Number of vehicles (default: 3)')
    args = parser.parse_args()

    customer_locations = load_data(args.customer_locations)
    customer_locations = customer_locations.reshape(args.num_customers, 2)

    vrp_solver = VRPSolver(num_customers=args.num_customers, customer_locations=customer_locations, num_vehicles=args.num_vehicles)
    routes, route_distances = vrp_solver.solve()

    for i, route in enumerate(routes):
        print(f'Route {i + 1}: {route}, Distance: {route_distances[i]}')

if __name__ == '__main__':
    main()
