import math
from lde_parserVisitor import lde_parserVisitor
from lde_parser import lde_parser


class evalVisitor(lde_parserVisitor):
    def __init__(self):
        super().__init__()
        self.variables = {}  # Diccionario para almacenar las variables

    def es_matriz(self, estructura):
        return isinstance(estructura, list) and all(isinstance(fila, list) for fila in estructura) and all(len(fila) == len(estructura[0]) for fila in estructura)

    def es_vector(self, estructura):
        return isinstance(estructura, list) and all(not isinstance(x, list) for x in estructura)

    def visitPrograma(self, ctx: lde_parser.ProgramaContext):
        resultados = [self.visit(child) for child in ctx.getChildren()]
        return [r for r in resultados if r is not None]

    def visitDeclaracion(self, ctx: lde_parser.DeclaracionContext):
        nombre = ctx.ID().getText()
        valor = self.visit(ctx.expresion())
        self.variables[nombre] = valor
        return f"Variable '{nombre}' asignada con el valor {valor}."

    def visitWriteStmt(self, ctx: lde_parser.WriteStmtContext):
        valor = self.visit(ctx.expresion())
        print(valor)
        return valor

    def visitExpresion(self, ctx: lde_parser.ExpresionContext):
        izquierda = self.visit(ctx.termino(0))
        for i in range(1, len(ctx.termino())):
            operador = ctx.getChild(i * 2 - 1).getText()
            derecha = self.visit(ctx.termino(i))
            if operador == '+':
                izquierda = self.sumar_o_restaurar(izquierda, derecha, 'sumar')
            elif operador == '-':
                izquierda = self.sumar_o_restaurar(izquierda, derecha, 'restar')
        return izquierda

    def visitTermino(self, ctx: lde_parser.TerminoContext):
        izquierda = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            operador = ctx.getChild(i * 2 - 1).getText()
            derecha = self.visit(ctx.factor(i))
            if operador == '*':
                izquierda = self.multiplicar(izquierda, derecha)
            elif operador == '@':
                izquierda = self.producto_punto(izquierda, derecha)
            elif operador == '^':
                izquierda = self.transponer_o_invertir(izquierda, derecha)
            elif operador == '/':
                izquierda = self.dividir(izquierda, derecha)
            elif operador == '%':
                izquierda = self.modulo(izquierda, derecha)
        return izquierda

    def visitFactor(self, ctx: lde_parser.FactorContext):
        if ctx.NUMERO():
            return float(ctx.NUMERO().getText()) if '.' in ctx.NUMERO().getText() else int(ctx.NUMERO().getText())
        elif ctx.ID():
            nombre = ctx.ID().getText()
            if nombre in self.variables:
                return self.variables[nombre]
            else:
                raise ValueError(f"Error: La variable '{nombre}' no está definida.")
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

    def visitLista(self, ctx: lde_parser.ListaContext):
        # Handle list expressions like [1, 2, 3]
        return [self.visit(exp) for exp in ctx.expresion()]

    def visitTrigonometrica(self, ctx: lde_parser.TrigonometricaContext):
        operador = ctx.getChild(0).getText()
        argumento = self.visit(ctx.expresion())
        funciones_trigonometricas = {
            'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
            'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
            'sinh': math.sinh, 'cosh': math.cosh, 'tanh': math.tanh
        }
        if operador in funciones_trigonometricas:
            return round(funciones_trigonometricas[operador](math.radians(argumento)), 4)
        else:
            raise ValueError(f"Error: Función trigonométrica no reconocida '{operador}'.")

    def sumar_o_restaurar(self, a, b, operacion):
        if isinstance(a, list) and isinstance(b, list):
            if operacion == 'sumar':
                # Sumar matrices elemento por elemento
                return [ [x + y for x, y in zip(fila_a, fila_b)] for fila_a, fila_b in zip(a, b)]
            elif operacion == 'restar':
                # Restar matrices elemento por elemento
                return [ [x - y for x, y in zip(fila_a, fila_b)] for fila_a, fila_b in zip(a, b)]
        else:
            return a + b if operacion == 'sumar' else a - b

    def multiplicar_matrices(self, a, b):
        # Verifica que el número de columnas de 'a' sea igual al número de filas de 'b'
        if len(a[0]) != len(b):
            raise ValueError("Error: El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz para multiplicarlas.")
        
        # Multiplica las matrices utilizando el producto punto entre filas de 'a' y columnas de 'b'
        resultado = []
        for fila_a in a:
            fila_resultado = []
            for col_b in zip(*b):
                fila_resultado.append(sum(x * y for x, y in zip(fila_a, col_b)))
            resultado.append(fila_resultado)
        return resultado


    def multiplicar(self, a, b):
        if self.es_matriz(a) and isinstance(b, (int, float)):
            return self.multiplicar_por_escalar(a, b)
        elif self.es_vector(a) and isinstance(b, (int, float)):
            return self.multiplicar_por_escalar(a, b)
        elif self.es_matriz(a) and self.es_matriz(b):
            return self.multiplicar_matrices(a, b)  # Calls the newly added matrix multiplication method
        elif isinstance(a, list) and isinstance(b, list):  # Element-wise list multiplication
            if len(a) != len(b):
                raise ValueError("Error: Las listas deben tener la misma longitud para multiplicarlas elemento por elemento.")
            return [x * y for x, y in zip(a, b)]  # Element-wise multiplication of lists
        else:
            return a * b  # For scalar multiplication



    def dividir(self, a, b):
        if isinstance(a, list) or isinstance(b, list):
            raise ValueError("Error: No se puede dividir listas o matrices.")
        return a / b

    def modulo(self, a, b):
        if isinstance(a, list) or isinstance(b, list):
            raise ValueError("Error: No se puede aplicar módulo a listas o matrices.")
        return a % b

    def transponer_o_invertir(self, a, b):
        if b == 0:
            return self.calcular_transpuesta(a)
        elif b == -1:
            return self.calcular_inversa(a)
        else:
            raise ValueError("El operador ^ solo soporta -1 (inversa) y 0 (transpuesta).")

    def producto_punto(self, A, B):
        if len(A) != len(B):
            raise ValueError("Los vectores deben tener el mismo tamaño para calcular el producto punto.")
        return sum(x * y for x, y in zip(A, B))

    def calcular_transpuesta(self, matriz):
        if not self.es_matriz(matriz):
            raise ValueError("Solo se puede calcular la transpuesta de matrices.")
        return [list(fila) for fila in zip(*matriz)]

    def calcular_inversa(self, matriz):
        if not self.es_matriz(matriz) or len(matriz) != len(matriz[0]):
            raise ValueError("Solo las matrices cuadradas tienen inversa.")
        n = len(matriz)
        identidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        matriz = [fila + identidad[i] for i, fila in enumerate(matriz)]
        for i in range(n):
            pivote = matriz[i][i]
            if pivote == 0:
                raise ValueError("La matriz no es invertible.")
            for j in range(2 * n):
                matriz[i][j] /= pivote
            for k in range(n):
                if k != i:
                    factor = matriz[k][i]
                    for j in range(2 * n):
                        matriz[k][j] -= factor * matriz[i][j]
        return [fila[n:] for fila in matriz]
