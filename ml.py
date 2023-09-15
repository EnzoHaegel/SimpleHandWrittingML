import os
from PIL import Image

# 1. Initialisation du réseau de neurones


def sigmoid(x):
    return 1.0 / (1.0 + pow(2.71, -x))


def sigmoid_prime(x):
    return x * (1.0 - x)


# Augmentation de la taille de la couche cachée et initialisation
hidden_size = 128
weights_hidden = [[0.5 for _ in range(256)] for _ in range(hidden_size)]
biases_hidden = [0.5 for _ in range(hidden_size)]
weights_output = [0.5 for _ in range(hidden_size)]
bias_output = 0.5


def forward(input_vector, weights_hidden, biases_hidden, weights_output, bias_output):
    hidden_activations = [sigmoid(sum([i*w + b for i, w, b in zip(
        input_vector, weights_hidden[h], biases_hidden)])) for h in range(hidden_size)]
    output = sigmoid(
        sum([h*w for h, w in zip(hidden_activations, weights_output)]) + bias_output)
    return output

# Formation avec la couche cachée


def train(inputs, targets, epochs=5000, lr=0.05):
    global weights_hidden, biases_hidden, weights_output, bias_output
    for epoch in range(epochs):
        for input_vector, desired_output in zip(inputs, targets):
            # Forward pass
            hidden_activations = [sigmoid(sum([i*w + b for i, w, b in zip(
                input_vector, weights_hidden[h], biases_hidden)])) for h in range(hidden_size)]
            output = sigmoid(
                sum([h*w for h, w in zip(hidden_activations, weights_output)]) + bias_output)

            # Calculate error
            error = desired_output - output

            # Update output weights
            for j, activation in enumerate(hidden_activations):
                weights_output[j] += lr * error * \
                    sigmoid_prime(output) * activation

            # Update hidden weights and biases
            for j in range(hidden_size):
                for k, input_value in enumerate(input_vector):
                    weights_hidden[j][k] += lr * error * \
                        sigmoid_prime(hidden_activations[j]) * input_value

    return weights_hidden, biases_hidden, weights_output, bias_output


# Train the network
train(inputs, targets)

# 2. Traitement de l'image


def load_image(filename):
    with Image.open(filename) as img:
        return [pixel == 0 for row in list(img.getdata()) for pixel in row]


def load_dataset():
    dataset = {"1": [], "2": []}

    for label in ["1", "2"]:
        for i in range(10):
            filename = f"./Dataset/{label}/{i:03}.png"
            dataset[label].append(load_image(filename))

    return dataset

# 3. Formation du réseau de neurones


dataset = load_dataset()

inputs = dataset["1"] + dataset["2"]
targets = [1] * 10 + [0] * 10

weights = [0.5 for _ in range(256)]  # car 16x16=256 pixels
biases = [0.5 for _ in range(256)]

weights, biases = train(inputs, targets, weights, biases)

# Testons notre modèle


def predict(filename):
    test_input = load_image(filename)
    prediction = forward(test_input, weights, biases)
    return 1 if prediction > 0.5 else 2


print(predict("./Dataset/test/004.png"))
