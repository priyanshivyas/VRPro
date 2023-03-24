import argparse
import numpy as np
import pandas as pd
from vrp_solver import solve_vrp, VRP
from vrp_utils import calculate_distance, find_nearest_customer
def parse_args():

    parser = argparse.ArgumentParser(description='Vehicle Routing Problem with Pickup and Delivery')

    parser.add_argument('--num_customers', type=int, default=5,
                        help='number of customers (default: 5)')
    parser.add_argument('--customer_locations', type=str, default='customers.csv',
                        help='path to CSV file containing customer locations')
    parser.add_argument('--num_vehicles', type=int, default=3,
                    help='number of vehicles (default: 3)')

    return parser.parse_args()
def load_data(input_file):
    with open(input_file, 'r') as f:
        data = np.genfromtxt(f, delimiter=',', dtype=float, skip_header=1)
    return data
# def main():
#     args = parse_args()
#     input_data = load_data(args.input_file)
#     num_customers = input_data.shape[0]
#     num_vehicles = args.num_vehicles
    
#     # Call the solver function
#     # routes, num_used_vehicles = solve_vrp(num_customers, input_data, num_vehicles)
#     routes, num_used_vehicles = solve_vrp(num_customers, input_data)
    
#     # Output the results
#     print(f"Optimized routes: {routes}")
#     print(f"Number of vehicles used: {num_used_vehicles}")
# if __name__ == '__main__':
#     main()

# import argparse
# import numpy as np
# from vrp_solver import solve_vrp

# def main():
#     # Parse command-line arguments
#     parser = argparse.ArgumentParser(description='Solve the Vehicle Routing Problem using the nearest neighbor algorithm')
#     parser.add_argument('--num_customers', type=int, help='Number of customers', required=True)
#     parser.add_argument('--customer_locations', type=str, help='List of customer locations', required=True)
#     parser.add_argument('--num_vehicles', type=int, help='Number of vehicles', required=True)
#     args = parser.parse_args()

#     # Load input data
#     customer_locations = np.fromstring(args.customer_locations, sep=' ').reshape(args.num_customers, 2)

#     # Solve the problem
#     solution = solve_vrp(customer_locations, args.num_vehicles)

#     # Print solution
#     print('Vehicle routes:', solution)

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description='Solve the Vehicle Routing Problem using the nearest neighbor algorithm')
    parser.add_argument('--num_customers', type=int, help='Number of customers', required=True)
    parser.add_argument('--customer_locations', type=str, help='List of customer locations', required=True)
    parser.add_argument('--num_vehicles', type=int, help='Number of vehicles', required=True)
    args = parser.parse_args()

    # read customer locations from CSV file
    customer_locations = load_data(args.customer_locations)

    # reshape customer_locations to be num_customers x 2
    customer_locations = customer_locations.reshape(args.num_customers, 2)

    # initialize VRP instance
    vrp = vrp(num_customers=args.num_customers, customer_locations=customer_locations, num_vehicles=args.num_vehicles)

    # solve VRP instance
    solution = vrp.solve()

    # print solution
    print(solution)

    print('Input data:', customer_locations, args.num_vehicles)
    solution = solve_vrp(customer_locations, args.num_vehicles)
    print('Output solution:', solution)

if __name__ == '__main__':
    main()
