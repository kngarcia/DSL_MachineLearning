from lde_parserVisitor import lde_parserVisitor
from lde_parser import lde_parser

class evalVisitor(lde_parserVisitor):

    def visitExpresion(self, ctx: lde_parser.ExpresionContext):
        # Si hay operaciones de suma o resta
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
        # Si hay operaciones de multiplicación o división
        izquierda = self.visit(ctx.factor(0))  # Inicia con el primer factor
        for i in range(1, len(ctx.factor())):
            operador = ctx.getChild(i * 2 - 1).getText()  # Detectar el operador (* o /)
            derecha = self.visit(ctx.factor(i))  # Visitar el siguiente factor
            if operador == '*':
                izquierda *= derecha
            elif operador == '/':
                if derecha != 0:
                    izquierda /= derecha  # Evitar división por cero
                else:
                    raise ZeroDivisionError("Error: División por cero")
        return izquierda

    def visitFactor(self, ctx: lde_parser.FactorContext):
        # Manejo de factores: números, expresiones entre paréntesis o negativos
        if ctx.NUMERO():
            return float(ctx.NUMERO().getText())  # Cambiar a float para manejar decimales
        elif ctx.expresion():
            return self.visit(ctx.expresion())  # Si es una expresión entre paréntesis
        elif ctx.RESTA():
            return -self.visit(ctx.factor())  # Si es un operador negativo, aplicar recursión
        else:
            raise ValueError("Error: Factor no válido.")
