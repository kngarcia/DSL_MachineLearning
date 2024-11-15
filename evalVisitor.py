from lde_parserVisitor import lde_parserVisitor
from lde_parser import lde_parser

class evalVisitor(lde_parserVisitor):

    def visitExpresion(self, ctx: lde_parser.ExpresionContext):
        # Si hay operaciones de suma o resta
        izquierda = self.visit(ctx.termino(0))
        for i in range(1, len(ctx.termino())):
            operador = ctx.getChild(i * 2 - 1).getText()  # Detectar el operador
            derecha = self.visit(ctx.termino(i))
            if operador == '+':
                izquierda += derecha
            elif operador == '-':
                izquierda -= derecha
        return izquierda

    def visitTermino(self, ctx: lde_parser.TerminoContext):
        # Si hay operaciones de multiplicación o división
        izquierda = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            operador = ctx.getChild(i * 2 - 1).getText()  # Detectar el operador
            derecha = self.visit(ctx.factor(i))
            if operador == '*':
                izquierda *= derecha
            elif operador == '/':
                izquierda /= derecha
        return izquierda

    def visitFactor(self, ctx: lde_parser.FactorContext):
        if ctx.NUMERO():
            return int(ctx.NUMERO().getText())
        elif ctx.expresion():
            return self.visit(ctx.expresion())  # Si es una expresión entre paréntesis
        elif ctx.RESTA():
            return -self.visit(ctx.factor())  # Si es un operador negativo
