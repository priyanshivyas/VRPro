import argparse
import numpy as np
from vrp_solver import solve_vrp
from vrp_utils import calculate_distance, find_nearest_customer
def parse_args():
    parser = argparse.ArgumentParser(description='Solve the VRP problem using the nearest neighbor algorithm')
    parser.add_argument('--input_file', type=str, help='Input data file in CSV format')
    parser.add_argument('--num_vehicles', type=int, help='Number of vehicles available')
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

def main():
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
