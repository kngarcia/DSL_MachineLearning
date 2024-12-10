# DSL_MachineLearning
pip install colorama
antlr4 -Dlanguage=Python3 -visitor lde_lexer.g4 lde_parser.g4


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



### For
var numeros = [10, 20, 30, 40, 50]

for (var i = 0, i < size(numeros), i = i + 1) {
    write(numeros[i])
}

### While