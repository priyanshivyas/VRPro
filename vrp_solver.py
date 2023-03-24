import numpy as np
from scipy.spatial.distance import pdist, squareform
from vrp_utils import nearest_neighbor

class VRPSolver:

    def __init__(self, num_customers, customer_locations, customer_demands, num_vehicles):
        self.num_customers = num_customers
        self.customer_locations = customer_locations
        self.customer_demands = customer_demands
        self.num_vehicles = num_vehicles
        self.distance_matrix = squareform(pdist(self.customer_locations))

    def solve(self):
        routes = []
        route_distances = []

        vehicle_capacities = np.ones(self.num_vehicles) * 10  # default capacity of 10

        for v in range(self.num_vehicles):
            route = []
            route_distance = 0

            curr_customer = 0  # start at the depot
            vehicle_capacity = vehicle_capacities[v]

            while True:
                # Find the nearest customer
                distances = self.distance_matrix[curr_customer][1:]
                feasible_customers = np.where(distances <= vehicle_capacity)[0]
                if len(feasible_customers) == 0:
                    break
                nearest_customer = feasible_customers[np.argmin(distances[feasible_customers])]

                # Add the customer to the route
                route.append(nearest_customer)
                route_distance += self.distance_matrix[curr_customer][nearest_customer + 1]
                vehicle_capacity -= self.customer_demands[nearest_customer]

                # Move to the new current customer
                curr_customer = nearest_customer + 1

            # Add the depot to the end of the route
            route.append(0)
            route_distance += self.distance_matrix[curr_customer][0]

            # Add the completed route and its distance to the overall solution
            routes.append(route)
            route_distances.append(route_distance)

        return routes, route_distances
