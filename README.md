# DSL_MachineLearning
pip install colorama
antlr4 -Dlanguage=Python3 -visitor lde_lexer.g4 lde_parser.g4
pip install matplotlib

sudo apt-get install python3-tk
sudo apt-get install qt5-default pyqt5-dev-tools


# Casos de prueba

## Operaciones Básicas

write(5+3)
write(3-8)
write(-3-48)
write(10^-8 - 10^-8)
write(7%3)
write(7^3)
write(sin(30))

## Matrices

[[1, 2], [3, 4]] + [[5, 6], [7, 8]]
[[1, 2], [3, 4]] - [[5, 6], [7, 8]]
[[1]] + [[2]]
[[1, 2], [3, 4]] * [[5, 6], [7, 8]] 
[[1, 2], [3, 4]] ^ 0
[[1, 2], [3, 4]] ^ -1

## Condicionales y bucles

### If - Else

if (5 > 3) {
    if (3 > 1) {
        write("Ambos son verdaderos");
    }
}

for (var i = 1, i <= 5, i = i + 1) {
    if (i % 2 == 0) {
        write(i);
    }
}

### For
var numeros = [10, 20, 30, 40, 50]

for (var i = 0, i < size(numeros), i = i + 1) {
    write(numeros[i])
}

### While

var i = 0

while (i < 0) {
    write(i)
    i = i + 1
}

## Clusters

var data = [[1.0, 2.0], [1.5, 1.8], [5.0, 8.0], [8.0, 8.0], [1.0, 0.6], [9.0, 11.0], [8.0, 2.0], [10.0, 2.0], [9.0, 3.0], [3.0, 3.0], [4.0, 4.0], [5.0, 5.0], [6.0, 6.0], [7.0, 7.0]]
var k = 3
var clusters = cluster(data, k)
write(clusters)

## Perceptron

