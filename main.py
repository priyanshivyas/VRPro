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
    if args.customer_locations is not None:
        customer_locations, customer_demands = load_data(args.customer_locations)
        customer_locations = customer_locations.reshape(args.num_customers, 2)
    else:
        np.random.seed(args.random_seed)
        customer_locations = np.random.rand(args.num_customers, 2)
        customer_demands = np.random.randint(1, 10, size=args.num_customers)
    # np.random.seed(args.random_seed)
    # # customer_locations = np.random.rand(args.num_customers, 2)
    # customer_demands = np.random.randint(1, 10, size=args.num_customers)

    # Solve the VRP instance
    vrp_solver = VRPSolver(num_customers=args.num_customers, customer_locations=customer_locations, customer_demands=customer_demands, num_vehicles=args.num_vehicles)
    routes, route_distances = vrp_solver.solve()

    # Print the solution
    # print_solution(routes, route_distances)

    # vrp_solver = VRPSolver(num_customers=args.num_customers, customer_locations=customer_locations, num_vehicles=args.num_vehicles)
    # routes, route_distances = vrp_solver.solve()

    for i, route in enumerate(routes):
        print(f'Route {i + 1}: {route}, Distance: {route_distances[i]}')

if __name__ == '__main__':
    main()
