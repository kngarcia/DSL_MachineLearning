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
        return izquierda

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
        return izquierda

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
        operador = ctx.getChild(0).getText()  # Obtener la función trigonométrica (sin, cos, tan)
        argumento = self.visit(ctx.expresion())  # Evaluar el argumento de la función trigonométrica
        if operador == 'sin':
            return math.sin(math.radians(argumento))  # Convertir a radianes
        elif operador == 'cos':
            return math.cos(math.radians(argumento))  # Convertir a radianes
        elif operador == 'tan':
            return math.tan(math.radians(argumento))  # Convertir a radianes
        else:
            raise ValueError("Error: Función trigonométrica no reconocida.")
