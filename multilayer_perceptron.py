import math
import random

class MultiLayerPerceptron:
    def __init__(self, X, y, layers, activation_function, learning_rate, epochs):
        self.X = X
        self.y = y
        self.layers = layers
        self.activation_function_name = activation_function.lower()
        self.learning_rate = learning_rate
        self.epochs = epochs
        self.weights = []
        self.biases = []
        self.activation_function = self.get_activation_function()
        self.activation_derivative = self.get_activation_derivative()
        self.initialize_weights()

    def initialize_weights(self):
        """Inicializa pesos y sesgos aleatoriamente."""
        for i in range(len(self.layers) - 1):
            input_size = self.layers[i]
            output_size = self.layers[i + 1]
            self.weights.append([[random.uniform(-1, 1) for _ in range(input_size)] for _ in range(output_size)])
            self.biases.append([random.uniform(-1, 1) for _ in range(output_size)])

    def get_activation_function(self):
        """Selecciona la función de activación."""
        if self.activation_function_name == "sigmoid":
            return self.sigmoid
        elif self.activation_function_name == "relu":
            return self.relu
        elif self.activation_function_name == "tanh_act":
            return self.tanh
        else:
            raise ValueError(f"Función de activación '{self.activation_function_name}' no soportada.")

    def get_activation_derivative(self):
        """Selecciona la derivada de la función de activación."""
        if self.activation_function_name == "sigmoid":
            return self.sigmoid_derivative
        elif self.activation_function_name == "relu":
            return self.relu_derivative
        elif self.activation_function_name == "tanh_act":
            return self.tanh_derivative
        else:
            raise ValueError(f"Función de activación '{self.activation_function_name}' no soportada.")

    # Funciones de activación
    def sigmoid(self, x):
        return [1 / (1 + math.exp(-xi)) for xi in x]

    def relu(self, x):
        return [max(0, xi) for xi in x]

    def tanh(self, x):
        return [math.tanh(xi) for xi in x]

    # Derivadas de las funciones de activación
    def sigmoid_derivative(self, x):
        return [xi * (1 - xi) for xi in x]

    def relu_derivative(self, x):
        return [1 if xi > 0 else 0 for xi in x]

    def tanh_derivative(self, x):
        return [1 - xi ** 2 for xi in x]

    def forward_propagation(self, inputs):
        """Realiza la propagación hacia adelante."""
        activations = inputs
        all_activations = [inputs]
        for i, (w, b) in enumerate(zip(self.weights, self.biases)):
            net_inputs = []
            for w_i, b_i in zip(w, b):
                net_input = sum(i * w_ij for i, w_ij in zip(activations, w_i)) + b_i
                net_inputs.append(net_input)
            activations = self.activation_function(net_inputs)
            all_activations.append(activations)
        return all_activations

    def backward_propagation(self, activations, y_sample):
        """Realiza la retropropagación."""
        if not isinstance(y_sample, list):
            y_sample = [y_sample]
        # Cálculo del error
        deriv = self.activation_derivative(activations[-1])
        errors = [(a - y) * d for a, y, d in zip(activations[-1], y_sample, deriv)]
        for i in reversed(range(len(self.weights))):
            delta = errors
            # Actualización de pesos y sesgos
            for j in range(len(self.weights[i])):
                for k in range(len(self.weights[i][j])):
                    self.weights[i][j][k] -= self.learning_rate * delta[j] * activations[i][k]
                self.biases[i][j] -= self.learning_rate * delta[j]
            if i != 0:
                deriv = self.activation_derivative(activations[i])
                errors = []
                for k in range(len(self.weights[i - 1])):
                    error = sum(self.weights[i][j][k] * delta[j] for j in range(len(delta)))
                    errors.append(error * deriv[k])

    def train(self):
        """Entrena el modelo."""
        for epoch in range(self.epochs):
            for x_sample, y_sample in zip(self.X, self.y):
                activations = self.forward_propagation(x_sample)
                self.backward_propagation(activations, y_sample)

    def predict(self, X_new):
        """Realiza predicciones para nuevos datos."""
        predictions = []
        for x_sample in X_new:
            activations = self.forward_propagation(x_sample)
            predictions.append(activations[-1])
        return predictions
        
    def evaluate(self, X_test, y_test):
        """Evalúa el modelo en un conjunto de prueba y calcula métricas de rendimiento."""
        predictions = self.predict(X_test)
        if isinstance(y_test[0], list):  # Clasificación con codificación one-hot
            y_test = [yt.index(1) for yt in y_test]
            predictions = [pred.index(max(pred)) for pred in predictions]

        if all(isinstance(y, int) for y in y_test):  # Clasificación
            true_positive = sum(1 for yt, yp in zip(y_test, predictions) if yt == yp)
            precision = true_positive / len(predictions)
            return {
                "precision": precision,
                "accuracy": precision,  # Igual para este caso binario
            }
        else:  # Regresión
            mse = sum((yt - yp) ** 2 for yt, yp in zip(y_test, predictions)) / len(y_test)
            mean_y = sum(y_test) / len(y_test)
            sst = sum((yt - mean_y) ** 2 for yt in y_test)
            sse = sum((yt - yp) ** 2 for yt, yp in zip(y_test, predictions))
            r_squared = 1 - (sse / sst)
            return {
                "mse": mse,
                "r_squared": r_squared
            }

    def get_metrics(self):
        """Devuelve un resumen de las métricas del modelo."""
        return {
            "epochs": self.epochs,
            "learning_rate": self.learning_rate,
            "layers": self.layers,
            "activation_function": self.activation_function_name
        }
