import numpy as np
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPRegressor
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from geneticalgorithm import geneticalgorithm as ga  # Make sure this library is installed

# Set random seed for reproducibility
np.random.seed(42)

# Generate synthetic input data: [Temperature, Feed Rate, Solids Content]
X = np.random.uniform(low=[160, 5, 10], high=[200, 20, 30], size=(100, 3))

# Generate corresponding output (moisture content) with some noise
y = (
    0.1 * (200 - X[:, 0]) +  # lower temp -> higher moisture
    0.05 * (20 - X[:, 1]) +  # lower feed rate -> more drying
    0.03 * (30 - X[:, 2]) +  # lower solids -> more moisture
    np.random.normal(0, 0.5, 100)  # noise
)

# Normalize features
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# Split data into training and validation sets
X_train, X_val, y_train, y_val = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# Train a neural network model
model = MLPRegressor(hidden_layer_sizes=(10, 10), max_iter=1000, random_state=1)
model.fit(X_train, y_train)

# Define objective function for GA (predict moisture)
def objective_function(x):
    x_scaled = scaler.transform([x])
    prediction = model.predict(x_scaled)[0]
    return prediction  # we aim to minimize this

# Define variable bounds
varbound = np.array([[160, 200], [5, 20], [10, 30]])

# GA parameters
algorithm_params = {
    'max_num_iteration': 50,
    'population_size': 15,
    'mutation_probability': 0.1,
    'elit_ratio': 0.01,
    'crossover_probability': 0.9,
    'parents_portion': 0.3,
    'crossover_type': 'uniform',
    'max_iteration_without_improv': None
}

# Run genetic algorithm
model_ga = ga(
    function=objective_function,
    dimension=3,
    variable_type='real',
    variable_boundaries=varbound,
    algorithm_parameters=algorithm_params
)

model_ga.run()

# Output best result
best_input = model_ga.output_dict['variable']
best_prediction = model_ga.output_dict['function']

print("\nOptimized Input Parameters (GA result):")
print(f"Inlet Temp: {best_input[0]:.2f} °C")
print(f"Feed Rate: {best_input[1]:.2f} L/h")
print(f"Solids Content: {best_input[2]:.2f} %")
print(f"Predicted Moisture Content: {best_prediction:.4f}")
