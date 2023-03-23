# VRPro
# Vehicle Routing Problem (VRP) Solver

## Introduction

The Vehicle Routing Problem (VRP) Solver is a Python program that optimizes vehicle routes for deliveries or pickups. It takes in customer coordinates and the number of vehicles available, and outputs the most efficient routes for each vehicle while visiting all customers. This solver is designed for businesses looking to optimize their delivery or pickup routes, and can lead to significant cost savings by minimizing the number of vehicles required and the driving distances.

## Requirements

The program requires Python 3.x and several external libraries. These libraries include:

* numpy
* argparse
* matplotlib (for data visualization)

## Installation

1. Clone the repository to your local machine.
2. Ensure that Python 3.x is installed on your machine.
3. Install the required external libraries by running `pip install -r requirements.txt` in the command line.
4. Run the program using `python main.py` in the command line.

## Usage

To use the program, enter the following command in the command line: `python main.py --customers [file] --vehicles [number]`

The `--customers` option specifies the file containing customer coordinates to be loaded, and the `--vehicles` option specifies the number of vehicles available for deliveries or pickups. The customer coordinates file should be in CSV format, with each row containing the customer's X and Y coordinates.

For example:

```
python main.py --customers customers.csv --vehicles 3
```

The program will output the optimized routes for each vehicle and the number of vehicles used.

## Algorithm

The VRP Solver program uses a simple nearest neighbor algorithm to optimize the vehicle routes. This algorithm selects the closest unvisited customer to a given location, creates a route for a vehicle, and then repeats until all customers are visited. The algorithm is designed to be efficient for small to medium-sized VRP instances.

## Contributing

Contributions to the Vehicle Routing Problem (VRP) Solver are welcome. Please submit any bug reports or feature requests to the GitHub Issues page.

## License

The Vehicle Routing Problem (VRP) Solver is licensed under the MIT License. Please see the `LICENSE` file for more information.
