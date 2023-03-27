import numpy as np
import pandas as pd

def read_csv_file(csv_file):
    """
    Reads the CSV file and returns a Pandas DataFrame.
    """
    return pd.read_csv(csv_file)

def preprocess_data(data):
    """
    Preprocesses the data and returns the input and output data for the RL model.
    """
    # Extract the x and y coordinates, and the demand of the customers
    x = data['x'].values
    y = data['y'].values
    demand = data['demand'].values

    # Extract the capacity of the vehicle and the number of vehicles available
    vehicle_capacity = data['vehicle_capacity'].values[0]
    num_vehicles = int(data['num_vehicles'].values[0])

    # Compute the total demand of all the customers
    total_demand = np.sum(demand)

    # Compute the average demand per vehicle
    avg_demand_per_vehicle = total_demand / num_vehicles

    # Compute the distance matrix between all the customer locations
    dist_matrix = np.zeros((len(x), len(x)))
    for i in range(len(x)):
        for j in range(len(x)):
            dist_matrix[i][j] = np.sqrt((x[i] - x[j])**2 + (y[i] - y[j])**2)

    # Create the input and output data for the RL model
    inputs = np.concatenate((dist_matrix, np.reshape(demand, (-1, 1))), axis=1)
    outputs = np.zeros((num_vehicles, len(x), 2))

    return inputs, outputs, vehicle_capacity, avg_demand_per_vehicle

input_file = 'inputs.csv'
df = pd.read_csv(input_file)
data = df.to_numpy()
output_file = 'inputs.npy'
np.save(output_file, data)


