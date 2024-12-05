import csv
import math
from lde_parserVisitor import lde_parserVisitor
from lde_parser import lde_parser
import matplotlib.pyplot as plt

class BreakException(Exception):
    """Excepción personalizada para manejar 'break'."""
    pass

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
        if ctx.extraerStmt():
            valor = self.visit(ctx.extraerStmt())
        else:
            valor = self.visit(ctx.expresion())
        self.variables[nombre] = valor
        return f"Variable '{nombre}' asignada con el valor {valor}."
    
    def visitModificacion(self, ctx: lde_parser.ModificacionContext):
        nombre = ctx.ID().getText()
        if nombre in self.variables:
            nuevo_valor = self.visit(ctx.expresion())
            self.variables[nombre] = nuevo_valor
            return nuevo_valor
        else:
            raise ValueError(f"Error: La variable '{nombre}' no está definida.")
    
    def visitWriteStmt(self, ctx: lde_parser.WriteStmtContext):
        if ctx.expresion():
            valor = self.visit(ctx.expresion())
        elif ctx.relacional():
            valor = self.visit(ctx.relacional())
        elif ctx.logico():
            valor = self.visit(ctx.logico())
        else:
            raise ValueError("Error: Tipo de expresión no reconocido en writeStmt.")
        
        print(valor)
        return valor
    def visitGraficarStmt(self, ctx: lde_parser.GraficarStmtContext):
        data = self.visit(ctx.expresion())
        if self.es_vector(data):
            plt.plot(data)
            plt.title("Vector")
            plt.xlabel("Índice")
            plt.ylabel("Valor")
        elif self.es_matriz(data):
            plt.imshow(data, cmap='viridis', aspect='auto')
            plt.colorbar()
            plt.title("Matriz")
        else:
            raise ValueError("Error: Solo se pueden graficar vectores y matrices.")
        plt.show()
    def visitExtraerStmt(self, ctx: lde_parser.ExtraerStmtContext):
        archivo = ctx.ARCHIVO().getText()[1:-1]  # Eliminar las comillas alrededor del nombre del archivo
        matriz = []

        with open(archivo, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                fila = []
                for val in row:
                    try:
                        if '.' in val:
                            fila.append(float(val))
                        else:
                            fila.append(int(val))
                    except ValueError:
                        fila.append(val)  # Dejar el valor como cadena si no se puede convertir a número
                matriz.append(fila)

        # Si la matriz tiene solo una fila, devolverla como una lista
        if len(matriz) == 1:
            return matriz[0]
        return matriz
    def visitExportarStmt(self, ctx: lde_parser.ExportarStmtContext):
        data = self.visit(ctx.expresion())
        archivo = ctx.ARCHIVO().getText()[1:-1]  # Eliminar las comillas alrededor del nombre del archivo

        with open(archivo, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if self.es_matriz(data):
                writer.writerows(data)
            elif self.es_vector(data):
                writer.writerow(data)
            else:
                raise ValueError("Error: Solo se pueden exportar vectores y matrices.")
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
            elif operador == '^':
                izquierda = self.transponer_o_invertir(izquierda, derecha)
            elif operador == '/':
                izquierda = self.dividir(izquierda, derecha)
            elif operador == '%':
                izquierda = self.modulo(izquierda, derecha)
        return izquierda
    
    def visitIfStmt(self, ctx: lde_parser.IfStmtContext):
        if ctx.relacional():
            condicion = self.visit(ctx.relacional())
        elif ctx.logico():
            condicion = self.visit(ctx.logico())
        else:
            raise ValueError("Error: Tipo de expresión no reconocido en ifStmt.")
        
        if condicion:
            self.visit(ctx.bloque(0))
        elif ctx.bloque(1):
            self.visit(ctx.bloque(1))
    def visitRelacional(self, ctx: lde_parser.RelacionalContext):
        izquierda = self.visit(ctx.expresion(0))
        operador = ctx.getChild(1).getText()
        derecha = self.visit(ctx.expresion(1))

        if operador == '>':
            return izquierda > derecha
        elif operador == '<':
            return izquierda < derecha
        elif operador == '>=':
            return izquierda >= derecha
        elif operador == '<=':
            return izquierda <= derecha
        elif operador == '==':
            return izquierda == derecha
        elif operador == '!=':
            return izquierda != derecha
        else:
            raise ValueError(f"Operador relacional no reconocido: {operador}")
    def visitLogico(self, ctx: lde_parser.LogicoContext):
        if ctx.NOT():
            return not self.visit(ctx.expresion(0))
        else:
            izquierda = self.visit(ctx.expresion(0))
            operador = ctx.getChild(1).getText()
            derecha = self.visit(ctx.expresion(1))

            if operador == 'and':
                return izquierda and derecha
            elif operador == 'or':
                return izquierda or derecha
            else:
                raise ValueError(f"Operador lógico no reconocido: {operador}")
            
    def visitForStmt(self, ctx: lde_parser.ForStmtContext):
        # Paso 1: Inicialización (opcional)
        if ctx.declaracion():
            self.visit(ctx.declaracion())  # Inicializar el iterador
        elif ctx.ID():
            iterador = ctx.ID().getText()
            if iterador not in self.variables:
                raise ValueError(f"Error: La variable '{iterador}' no está definida.")
        else:
            raise ValueError("Error: Falta la inicialización del iterador en forStmt.")
        
        # Paso 2: Definir funciones auxiliares
        def evaluar_condicion():
            if ctx.relacional():
                return self.visit(ctx.relacional())
            elif ctx.logico():
                return self.visit(ctx.logico())
            else:
                raise ValueError("Error: Tipo de condición no reconocido en forStmt.")

        def realizar_incremento():
            if ctx.modificacion():
                self.visit(ctx.modificacion())
            else:
                raise ValueError("Error: Incremento no especificado en forStmt.")

        # Paso 3: Ejecutar el bucle
        try:
            while evaluar_condicion():
                try:
                    self.visit(ctx.bloque())  # Ejecutar el cuerpo del bucle
                except BreakException:
                    break  # Rompe el bucle
                realizar_incremento()  # Realizar la modificación al final de cada iteración
        except BreakException:
            pass  # Capturar el 'break' si se lanza desde el cuerpo del bucle

    def visitWhileStmt(self, ctx: lde_parser.WhileStmtContext):
        def evaluar_condicion():
            if ctx.relacional():
                return self.visit(ctx.relacional())
            elif ctx.logico():
                return self.visit(ctx.logico())
            else:
                raise ValueError("Error: Tipo de condición no reconocido en whileStmt.")

        try:
            while evaluar_condicion():
                try:
                    self.visit(ctx.bloque())  # Ejecutar el cuerpo del bucle
                except BreakException:
                    break  # Rompe el bucle
        except BreakException:
            pass  # Capturar el 'break' si se lanza desde el cuerpo del bucle

    def visitBreakStmt(self, ctx: lde_parser.BreakStmtContext):
        """Lanza la excepción para romper un bucle."""
        raise BreakException()
    
    def visitFactor(self, ctx: lde_parser.FactorContext):
        if ctx.NUMERO():
            return float(ctx.NUMERO().getText()) if '.' in ctx.NUMERO().getText() else int(ctx.NUMERO().getText())
        elif ctx.ID():
            nombre = ctx.ID().getText()
            if nombre in self.variables:
                valor = self.variables[nombre]
                if ctx.acceso():
                    return self.visitAcceso(ctx.acceso(), valor)
                return valor
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
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]  # Eliminar las comillas alrededor del string
        elif ctx.TRUE():
            return True
        elif ctx.FALSE():
            return False
        else:
            raise ValueError("Error: Factor no válido.")

    def visitAcceso(self, ctx: lde_parser.AccesoContext, valor):
        if isinstance(valor, list):
            indice1 = self.visit(ctx.expresion(0))
            if not isinstance(indice1, int):
                raise ValueError("Error: El índice debe ser un número entero.")
            if ctx.expresion(1):
                if not isinstance(valor[indice1], list):
                    raise ValueError("Error: El valor no es una matriz.")
                indice2 = self.visit(ctx.expresion(1))
                if not isinstance(indice2, int):
                    raise ValueError("Error: El índice debe ser un número entero.")
                return valor[indice1][indice2]
            return valor[indice1]
        else:
            raise ValueError("Error: El valor no es una lista o matriz.")

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
        if self.es_matriz(a) and self.es_matriz(b):
            return self.multiplicar_matrices(a, b)
        elif self.es_vector(a) and self.es_vector(b):
            if len(a) != len(b):
                raise ValueError("Error: Los vectores deben tener el mismo tamaño para calcular el producto punto.")
            return self.producto_punto(a, b)
        elif self.es_matriz(a) and isinstance(b, (int, float)):
            return self.multiplicar_por_escalar(a, b)
        elif self.es_vector(a) and isinstance(b, (int, float)):
            return self.multiplicar_por_escalar(a, b)
        elif isinstance(a, list) and isinstance(b, list):
            # Multiplicación elemento a elemento
            if len(a) != len(b):
                raise ValueError("Error: Las listas deben tener la misma longitud para multiplicarlas elemento por elemento.")
            return [x * y for x, y in zip(a, b)]
        else:
            # Producto normal para escalares
            return a * b


    def multiplicar_por_escalar(self, estructura, escalar):
        if self.es_vector(estructura):
            # Multiplica cada elemento del vector por el escalar
            return [x * escalar for x in estructura]
        elif self.es_matriz(estructura):
            # Multiplica cada elemento de la matriz por el escalar
            return [[x * escalar for x in fila] for fila in estructura]
        else:
            raise ValueError("Error: Solo se pueden multiplicar vectores o matrices por un escalar.")


    def dividir(self, a, b):
        if isinstance(a, list) or isinstance(b, list):
            raise ValueError("Error: No se puede dividir listas o matrices.")
        return a / b

    def modulo(self, a, b):
        if isinstance(a, list) or isinstance(b, list):
            raise ValueError("Error: No se puede aplicar módulo a listas o matrices.")
        return a % b

    def transponer_o_invertir(self, a, b):
        if self.es_matriz(a):
            if b == 0:
                return self.calcular_transpuesta(a)
            elif b == -1:
                return self.calcular_inversa(a)
            else:
                raise ValueError("El operador ^ solo soporta -1 (inversa) y 0 (transpuesta) para matrices.")
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a ** b
        else:
            raise ValueError("Operación no válida para los operandos dados.")

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
