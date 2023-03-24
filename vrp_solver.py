import numpy as np
from scipy.spatial.distance import pdist, squareform
from vrp_utils import nearest_neighbor

class VRPSolver:
    def __init__(self, num_customers, customer_locations, num_vehicles):
        self.num_customers = num_customers
        self.customer_locations = customer_locations
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

            while True:
                # Find the nearest customer that can be serviced by the vehicle
                mask = (vehicle_capacities[v] > 0)
                dist_with_capacity = self.distance_matrix[curr_customer][1:] + np.where(mask, 0, np.inf)
                nearest_customer = np.argmin(dist_with_capacity)

                # If no customers are reachable, we're done with this route
                if np.isinf(dist_with_capacity[nearest_customer]):
                    break

                # Add the customer to the route
                route.append(nearest_customer)
                route_distance += self.distance_matrix[curr_customer][nearest_customer + 1]
                vehicle_capacities[v] -= 1

                # Move to the new current customer
                curr_customer = nearest_customer + 1

            # Add the depot to the end of the route
            route.append(0)
            route_distance += self.distance_matrix[curr_customer][0]

            # Add the completed route and its distance to the overall solution
            routes.append(route)
            route_distances.append(route_distance)

        return routes, route_distances
