import math
from lde_parserVisitor import lde_parserVisitor
from lde_parser import lde_parser


class evalVisitor(lde_parserVisitor):
    # Manejo de listas
    def visitLista(self, ctx: lde_parser.ListaContext):
        elementos = [self.visit(exp) for exp in ctx.expresion()]
        return elementos

    # Manejo de matrices
    def visitMatriz(self, ctx: lde_parser.MatrizContext):
        filas = [self.visit(lista) for lista in ctx.lista()]
        return filas

    # Manejo de la regla inicial `programa`
    def visitPrograma(self, ctx: lde_parser.ProgramaContext):
        return self.visit(ctx.expresion())

    # Manejo de expresiones
    def visitExpresion(self, ctx: lde_parser.ExpresionContext):
        izquierda = self.visit(ctx.termino(0))
        for i in range(1, len(ctx.termino())):
            operador = ctx.getChild(i * 2 - 1).getText()
            derecha = self.visit(ctx.termino(i))
            if operador == '+':
                if isinstance(izquierda, list) and isinstance(derecha, list):
                    izquierda = self.sumar_vectores_o_matrices(izquierda, derecha)
                else:
                    izquierda += derecha
            elif operador == '-':
                if isinstance(izquierda, list) and isinstance(derecha, list):
                    izquierda = self.restar_vectores_o_matrices(izquierda, derecha)
                else:
                    izquierda -= derecha
        return izquierda

    # Manejo de términos
    def visitTermino(self, ctx: lde_parser.TerminoContext):
        izquierda = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            operador = ctx.getChild(i * 2 - 1).getText()
            derecha = self.visit(ctx.factor(i))
            if operador == '*':
                if isinstance(izquierda, list) and isinstance(derecha, (int, float)):
                    izquierda = self.multiplicar_por_escalar(izquierda, derecha)
                elif isinstance(derecha, list) and isinstance(izquierda, (int, float)):
                    izquierda = self.multiplicar_por_escalar(derecha, izquierda)
                elif isinstance(izquierda, list) and isinstance(derecha, list):
                    izquierda = self.multiplicar_matrices(izquierda, derecha)
                else:
                    izquierda *= derecha
            elif operador == '@':
                if isinstance(izquierda, list) and isinstance(derecha, list):
                    izquierda = self.producto_punto(izquierda, derecha)
                else:
                    raise ValueError("El operador @ solo se puede usar con vectores.")
            elif operador == '^':
                if derecha == -1:
                    izquierda = self.calcular_inversa(izquierda)
                elif derecha == 0:
                    izquierda = self.calcular_transpuesta(izquierda)
                else:
                    raise ValueError("El operador ^ solo soporta -1 (inversa) y 0 (transpuesta).")
            elif operador == '/':
                if isinstance(izquierda, list) or isinstance(derecha, list):
                    raise ValueError("Error: No se puede dividir listas o matrices.")
                izquierda /= derecha
            elif operador == '%':
                if isinstance(izquierda, list) or isinstance(derecha, list):
                    raise ValueError("Error: No se puede aplicar módulo a listas o matrices.")
                izquierda %= derecha
        return izquierda

    # Manejo de factores
    def visitFactor(self, ctx: lde_parser.FactorContext):
        if ctx.NUMERO():
            texto = ctx.NUMERO().getText()
            return float(texto) if '.' in texto else int(texto)
        elif ctx.expresion():
            return self.visit(ctx.expresion())
        elif ctx.RESTA():
            return -self.visit(ctx.factor())
        elif ctx.trigonometrica():
            return self.visit(ctx.trigonometrica())
        elif ctx.lista():
            return self.visit(ctx.lista())
        elif ctx.matriz():
            return self.visit(ctx.matriz())
        else:
            raise ValueError("Error: Factor no válido.")

    # Manejo de funciones trigonométricas
    def visitTrigonometrica(self, ctx: lde_parser.TrigonometricaContext):
        operador = ctx.getChild(0).getText()
        argumento = self.visit(ctx.expresion())
        if operador == 'sin':
            return round(math.sin(math.radians(argumento)), 4)
        elif operador == 'cos':
            return round(math.cos(math.radians(argumento)), 4)
        elif operador == 'tan':
            return round(math.tan(math.radians(argumento)), 4)
        elif operador == 'asin':
            return round(math.degrees(math.asin(argumento)), 4)
        elif operador == 'acos':
            return round(math.degrees(math.acos(argumento)), 4)
        elif operador == 'atan':
            return round(math.degrees(math.atan(argumento)), 4)
        elif operador == 'sinh':
            return round(math.sinh(argumento), 4)
        elif operador == 'cosh':
            return round(math.cosh(argumento), 4)
        elif operador == 'tanh':
            return round(math.tanh(argumento), 4)
        else:
            raise ValueError("Error: Función trigonométrica no reconocida.")

    # Métodos auxiliares para operaciones con vectores y matrices

    def sumar_vectores_o_matrices(self, a, b):
        if len(a) != len(b):
            raise ValueError("Las colecciones no son del mismo tamaño")
        if all(isinstance(x, list) for x in a) and all(isinstance(y, list) for y in b):  # Matrices
            return [self.sumar_vectores_o_matrices(x, y) for x, y in zip(a, b)]
        elif all(not isinstance(x, list) for x in a) and all(not isinstance(y, list) for y in b):  # Vectores
            return [x + y for x, y in zip(a, b)]
        else:
            raise ValueError("Error: No se pueden sumar vectores y matrices juntos.")

    def restar_vectores_o_matrices(self, a, b):
        if len(a) != len(b):
            raise ValueError("Las colecciones no son del mismo tamaño")
        if all(isinstance(x, list) for x in a) and all(isinstance(y, list) for y in b):  # Matrices
            return [self.restar_vectores_o_matrices(x, y) for x, y in zip(a, b)]
        elif all(not isinstance(x, list) for x in a) and all(not isinstance(y, list) for y in b):  # Vectores
            return [x - y for x, y in zip(a, b)]
        else:
            raise ValueError("Error: No se pueden restar vectores y matrices juntos.")

    def multiplicar_por_escalar(self, matriz, escalar):
        if all(isinstance(x, list) for x in matriz):  # Matriz
            return [self.multiplicar_por_escalar(fila, escalar) for fila in matriz]
        elif all(not isinstance(x, list) for x in matriz):  # Vector
            return [x * escalar for x in matriz]
        else:
            raise ValueError("Error: La multiplicación por escalar solo aplica a vectores o matrices.")

    def multiplicar_matrices(self, A, B):
        if len(A[0]) != len(B):
            raise ValueError("El número de columnas de A debe ser igual al número de filas de B.")
        resultado = []
        for fila in A:
            nueva_fila = []
            for j in range(len(B[0])):
                suma = sum(fila[k] * B[k][j] for k in range(len(B)))
                nueva_fila.append(suma)
            resultado.append(nueva_fila)
        return resultado

    def producto_punto(self, A, B):
        if len(A) != len(B):
            raise ValueError("Los vectores deben tener el mismo tamaño para calcular el producto punto.")
        return sum(x * y for x, y in zip(A, B))

    def calcular_transpuesta(self, matriz):
        if not all(isinstance(row, list) for row in matriz):
            raise ValueError("Solo se puede calcular la transpuesta de matrices.")
        return [list(fila) for fila in zip(*matriz)]

    def calcular_inversa(self, matriz):
        if len(matriz) != len(matriz[0]):
            raise ValueError("Solo las matrices cuadradas tienen inversa.")

        # Crear matriz aumentada (identidad)
        n = len(matriz)
        identidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        matriz = [fila + identidad[i] for i, fila in enumerate(matriz)]

        # Aplicar eliminación gaussiana
        for i in range(n):
            # Normalizar la fila actual
            pivote = matriz[i][i]
            if pivote == 0:
                raise ValueError("La matriz no es invertible.")
            for j in range(2 * n):
                matriz[i][j] /= pivote
            # Hacer ceros en la columna del pivote
            for k in range(n):
                if k != i:
                    factor = matriz[k][i]
                    for j in range(2 * n):
                        matriz[k][j] -= factor * matriz[i][j]

        # Extraer la parte derecha (matriz inversa)
        inversa = [fila[n:] for fila in matriz]
        return inversa
