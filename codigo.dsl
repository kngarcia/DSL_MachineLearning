var X = [[1.0, 0.0], [0.0, 1.0], [1.0, 1.0], [0.0, 0.0], [0.5, 0.5], [0.2, 0.8], [0.8, 0.2], [0.3, 0.7], [0.6, 0.4], [0.4, 0.6], [0.9, 0.1], [0.1, 0.9]]
var y = [[1, 0, 0], [0, 1, 0], [0, 0, 1], [1, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 0, 1], [0, 0, 1], [0, 1, 0], [1, 0, 0], [0, 1, 0]]
var layers = [2, 5, 3]
var learningrate = 0.01
var epochs = 3000
var mlp_sigmoid = classifier(X, y, layers, sigmoid, learningrate, epochs)
var predictions_sigmoid = mlp_sigmoid.predict(X)
write(predictions_sigmoid)