import numpy as np
from scipy.spatial.distance import pdist, squareform
from vrp_utils import nearest_neighbor

class VRPSolver:

    def __init__(self, num_customers, customer_locations, customer_demands, num_vehicles, vehicle_capacity):
        self.num_customers = num_customers
        self.customer_locations = customer_locations
        self.customer_demands = customer_demands
        self.num_vehicles = num_vehicles
        self.vehicle_capacity = vehicle_capacity
        self.distance_matrix = squareform(pdist(self.customer_locations))
        if customer_demands is None:
            self.customer_demands = np.random.randint(1, 10, size=self.num_customers)
        else:
            self.customer_demands = customer_demands

    def solve(self):
        unvisited_customers = set(range(1, self.num_customers))
        visited_customers = set()
        vehicle_capacities = [self.vehicle_capacity] * self.num_vehicles
        routes = [[] for _ in range(self.num_vehicles)]
        route_distances = [0] * self.num_vehicles

        for v in range(self.num_vehicles):
            curr_location = 0
            remaining_capacity = vehicle_capacities[v]
            while unvisited_customers:
                nearest_customer = nearest_neighbor(curr_location, self.distance_matrix, remaining_capacity)
                if nearest_customer is None:
                    break
                remaining_capacity -= self.customer_demands[nearest_customer]
                if remaining_capacity < 0:
                    remaining_capacity = vehicle_capacities[v]
                    routes[v].insert(0, 0)
                    route_distances[v] += self.distance_matrix[curr_location][0]
                    curr_location = 0
                    continue
                if nearest_customer in unvisited_customers:
                    routes[v].append(nearest_customer)
                    visited_customers.add(nearest_customer)
                    unvisited_customers.remove(nearest_customer)
                    route_distances[v] += self.distance_matrix[curr_location][nearest_customer]
                    curr_location = nearest_customer
            if curr_location != 0:
                routes[v].append(0)
                route_distances[v] += self.distance_matrix[curr_location][0]

        return routes, route_distances

