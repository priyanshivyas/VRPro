import argparse
import numpy as np
import pandas as pd
from vrp_solver import VRP

def main():
    parser = argparse.ArgumentParser(description='Solve Vehicle Routing Problem')
    # parser.add_argument('--num_customers', type=int, required=True, help='Number of customers')
    # parser.add_argument('--customer_locations', type=str, required=True, help='CSV file containing customer locations')
    # parser.add_argument('--num_vehicles', type=int, required=True, help='Number of vehicles')

    parser.add_argument('--num_customers', type=int, default=14,
                        help='number of customers (default: 5)')
    parser.add_argument('--customer_locations', type=str, default='customers.csv',
                        help='path to CSV file containing customer locations')
    parser.add_argument('--num_vehicles', type=int, default=3,
                    help='number of vehicles (default: 3)')
    args = parser.parse_args()

    # Load customer locations from CSV file
    customer_locations = np.loadtxt(args.customer_locations, delimiter=',', skiprows=1, usecols=(0,1))

    # Check if number of customers matches the shape of customer_locations array
    if args.num_customers != customer_locations.shape[0]:
        print(f"Error: Number of customers in input ({args.num_customers}) does not match the number of rows in {args.customer_locations} ({customer_locations.shape[0]}).")
        return

    # Reshape customer_locations array to match VRP solver input format
    customer_locations = customer_locations.reshape(args.num_customers, 2)

    # Solve VRP problem
    vrp = VRP(num_customers=args.num_customers, customer_locations=customer_locations, num_vehicles=args.num_vehicles)
    solution = vrp.solve()
    
    # Print solution
    print("Total distance: ", solution['total_distance'])
    print("Routes:")
    for i, route in enumerate(solution['routes']):
        print(f"Vehicle {i}: {route}")

if __name__ == '__main__':
    main()
