import math
from lde_parserVisitor import lde_parserVisitor
from lde_parser import lde_parser

class evalVisitor(lde_parserVisitor):
    # Manejo de listas
    def visitLista(self, ctx: lde_parser.ListaContext):
        # Procesar cada expresión dentro de la lista y devolver una lista de valores
        elementos = [self.visit(exp) for exp in ctx.expresion()]
        return elementos

    # Manejo de matrices
    def visitMatriz(self, ctx: lde_parser.MatrizContext):
        # Procesar cada lista dentro de la matriz y devolver una lista de listas
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
                    izquierda = izquierda + derecha  # Concatenar listas
                else:
                    izquierda += derecha
            elif operador == '-':
                if isinstance(izquierda, list) or isinstance(derecha, list):
                    raise ValueError("Error: No se puede restar listas.")
                izquierda -= derecha
        return izquierda

    # Manejo de términos
    def visitTermino(self, ctx: lde_parser.TerminoContext):
        izquierda = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            operador = ctx.getChild(i * 2 - 1).getText()
            derecha = self.visit(ctx.factor(i))
            if operador == '*':
                if isinstance(izquierda, list) and isinstance(derecha, int):
                    izquierda = izquierda * derecha  # Repetir lista
                elif isinstance(derecha, list) and isinstance(izquierda, int):
                    izquierda = derecha * izquierda  # Repetir lista
                else:
                    izquierda *= derecha
            elif operador == '/':
                if isinstance(izquierda, list) or isinstance(derecha, list):
                    raise ValueError("Error: No se puede dividir listas.")
                izquierda /= derecha
            elif operador == '%':
                if isinstance(izquierda, list) or isinstance(derecha, list):
                    raise ValueError("Error: No se puede aplicar módulo a listas.")
                izquierda %= derecha
            elif operador == '^':
                if isinstance(izquierda, list) or isinstance(derecha, list):
                    raise ValueError("Error: No se puede aplicar exponenciación a listas.")
                izquierda **= derecha
        return izquierda

    # Manejo de factores
    def visitFactor(self, ctx: lde_parser.FactorContext):
        if ctx.NUMERO():
            return float(ctx.NUMERO().getText())
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
