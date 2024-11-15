import math
from lde_parserVisitor import lde_parserVisitor
from lde_parser import lde_parser

class evalVisitor(lde_parserVisitor):

    def visitExpresion(self, ctx: lde_parser.ExpresionContext):
        izquierda = self.visit(ctx.termino(0))  # Inicia con el primer término
        for i in range(1, len(ctx.termino())):
            operador = ctx.getChild(i * 2 - 1).getText()  # Detectar el operador (+ o -)
            derecha = self.visit(ctx.termino(i))  # Visitar el siguiente término
            if operador == '+':
                izquierda += derecha
            elif operador == '-':
                izquierda -= derecha
        return round(izquierda, 4)  # Redondear a 4 decimales

    def visitTermino(self, ctx: lde_parser.TerminoContext):
        izquierda = self.visit(ctx.factor(0))  # Inicia con el primer factor
        for i in range(1, len(ctx.factor())):
            operador = ctx.getChild(i * 2 - 1).getText()  # Detectar el operador (*, /, % o ^)
            derecha = self.visit(ctx.factor(i))  # Visitar el siguiente factor
            if operador == '*':
                izquierda *= derecha
            elif operador == '/':
                if derecha != 0:
                    izquierda /= derecha  # Evitar división por cero
                else:
                    raise ZeroDivisionError("Error: División por cero")
            elif operador == '%':
                izquierda %= derecha  # Realizar la operación de módulo
            elif operador == '^':  # Exponenciación
                izquierda **= derecha
        return round(izquierda, 4)  # Redondear a 4 decimales

    def visitFactor(self, ctx: lde_parser.FactorContext):
        if ctx.NUMERO():
            return float(ctx.NUMERO().getText())  # Convertir a float para manejar decimales
        elif ctx.expresion():
            return self.visit(ctx.expresion())  # Si es una expresión entre paréntesis
        elif ctx.RESTA():
            return -self.visit(ctx.factor())  # Si es un operador negativo, aplicar recursión
        elif ctx.trigonometrica():
            return self.visit(ctx.trigonometrica())  # Si es una función trigonométrica
        else:
            raise ValueError("Error: Factor no válido.")

    def visitTrigonometrica(self, ctx: lde_parser.TrigonometricaContext):
        operador = ctx.getChild(0).getText()  # Obtener la función trigonométrica (sin, cos, tan, asin, etc.)
        argumento = self.visit(ctx.expresion())  # Evaluar el argumento de la función trigonométrica
        if operador == 'sin':
            return round(math.sin(math.radians(argumento)), 4)  # Convertir a radianes y redondear
        elif operador == 'cos':
            return round(math.cos(math.radians(argumento)), 4)  # Convertir a radianes y redondear
        elif operador == 'tan':
            return round(math.tan(math.radians(argumento)), 4)  # Convertir a radianes y redondear
        elif operador == 'asin':
            return round(math.degrees(math.asin(argumento)), 4)  # Convertir de radianes a grados y redondear
        elif operador == 'acos':
            return round(math.degrees(math.acos(argumento)), 4)  # Convertir de radianes a grados y redondear
        elif operador == 'atan':
            return round(math.degrees(math.atan(argumento)), 4)  # Convertir de radianes a grados y redondear
        elif operador == 'sinh':
            return round(math.sinh(argumento), 4)
        elif operador == 'cosh':
            return round(math.cosh(argumento), 4)
        elif operador == 'tanh':
            return round(math.tanh(argumento), 4)
        else:
            raise ValueError("Error: Función trigonométrica no reconocida.")
