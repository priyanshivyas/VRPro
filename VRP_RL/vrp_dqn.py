import random
import numpy as np
import tensorflow as tf

class DQNAgent:
    def __init__(self, state_size, action_size):
        self.state_size = state_size
        self.action_size = action_size
        self.memory = []
        self.gamma = 0.95 # discount factor
        self.epsilon = 1.0 # exploration rate
        self.epsilon_min = 0.01
        self.epsilon_decay = 0.995
        self.learning_rate = 0.001
        self.model = self._build_model()

    def _build_model(self):
        # Neural network with 3 hidden layers
        model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(128, input_dim=self.state_size, activation='relu'),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(self.action_size, activation='linear')
        ])
        model.compile(loss='mse', optimizer=tf.keras.optimizers.Adam(lr=self.learning_rate))
        return model

    def remember(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    def act(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        else:
            return np.argmax(self.model.predict(state))

    def replay(self, batch_size):
        minibatch = random.sample(self.memory, batch_size)
        for state, action, reward, next_state, done in minibatch:
            target = reward
            if not done:
                target = (reward + self.gamma * np.amax(self.model.predict(next_state)[0]))
            target_f = self.model.predict(state)
            target_f[0][action] = target
            self.model.fit(state, target_f, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

def train_dqn(inputs, outputs, vehicle_capacity, avg_demand_per_vehicle):
    state_size = inputs.shape[1] # size of the state space
    action_size = inputs.shape[0] # size of the action space
    batch_size = 32 # size of the minibatch
    episodes = 1000 # number of episodes

    # Initialize the DQN agent
    agent = DQNAgent(state_size, action_size)

    for episode in range(episodes):
        state = np.zeros((1, state_size))
        state[0, -1] = vehicle_capacity # initialize the vehicle capacity
        done = False
        total_reward = 0
        num_vehicles_used = 0

        # Initialize the list of visited customers
        visited_customers = []

        while not done:
            # Select an action using the DQN agent
            action = agent.act(state)

            # Check if the action is valid
            if action in visited_customers:
                reward = -100
                next_state = state
                done = True
            else:
                visited_customers.append(action)
                reward = outputs[num_vehicles_used][action][0] - (avg_demand_per_vehicle / vehicle_capacity) * outputs[num_vehicles_used][action][1]
                next_state = np.zeros((1, state_size))
                next_state[0, :-1] = outputs[num_vehicles_used][action][:2]
                next_state[0, -1] = state[0, -1] - outputs[num_vehicles_used][action][1]

                # Check if the next state is terminal
                if next_state[0, -1] < 0:
                    reward = -100
                    done = True

            # Remember the current state, action, reward, and next state
            agent.remember(state, action, reward, next_state, done)

            # Update the total reward
            total_reward += reward

            # Set the current state to the next state
            state = next_state

        # Check if the episode is over
        if len(visited_customers) == action_size:
            done = True
            num_vehicles_used += 1

            # Check if there are any remaining vehicles
            if num_vehicles_used < outputs.shape[0]:
                state = np.zeros((1, state_size))
                state[0, -1] = vehicle_capacity
                visited_customers = []
                done = False
            else:
                reward = total_reward

        # Replay the minibatch
        if len(agent.memory) > batch_size:
            agent.replay(batch_size)

    # Decay the exploration rate
    if agent.epsilon > agent.epsilon_min:
        agent.epsilon *= agent.epsilon_decay

    # Print the episode statistics
    print("Episode:", episode + 1, "Total reward:", total_reward, "Epsilon:", agent.epsilon)

    # Save the DQN model
    agent.model.save('vrp_dqn.h5')
if __name__ == "__main__":
# Load the input and output data
    

# Generate some random data for demonstration purposes
    inputs = np.random.rand(10, 3)
    outputs = np.random.rand(1, 10, 3)

# Save the arrays to files with allow_pickle=False
    np.save('inputs.npy', inputs, allow_pickle=False)

    np.save('outputs.npy', outputs, allow_pickle=False)

# Set the vehicle capacity and average demand per vehicle
    vehicle_capacity = 200
    avg_demand_per_vehicle = np.mean(outputs[0, :, 1])

# Train the DQN model
    train_dqn(inputs, outputs, vehicle_capacity, avg_demand_per_vehicle)
