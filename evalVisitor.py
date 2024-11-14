from lde_parserVisitor import lde_parserVisitor
from lde_parser import lde_parser

class evalVisitor(lde_parserVisitor):

    def visitSuma(self, ctx: lde_parser.SumaContext):
        izquierda = self.visit(ctx.expresion(0))
        derecha = self.visit(ctx.expresion(1))
        return izquierda + derecha

    def visitResta(self, ctx: lde_parser.RestaContext):
        izquierda = self.visit(ctx.expresion(0))
        derecha = self.visit(ctx.expresion(1))
        return izquierda - derecha

    def visitMultiplicacion(self, ctx: lde_parser.MultiplicacionContext):
        izquierda = self.visit(ctx.expresion(0))
        derecha = self.visit(ctx.expresion(1))
        return izquierda * derecha

    def visitDivision(self, ctx: lde_parser.DivisionContext):
        izquierda = self.visit(ctx.expresion(0))
        derecha = self.visit(ctx.expresion(1))
        return izquierda / derecha

    def visitNegativo(self, ctx: lde_parser.NegativoContext):
        valor = self.visit(ctx.expresion())
        return -valor

    def visitNumero(self, ctx: lde_parser.NumeroContext):
        return int(ctx.getText())
