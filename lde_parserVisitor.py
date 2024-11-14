# Generated from lde_parser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .lde_parser import lde_parser
else:
    from lde_parser import lde_parser

# This class defines a complete generic visitor for a parse tree produced by lde_parser.

class lde_parserVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by lde_parser#programa.
    def visitPrograma(self, ctx:lde_parser.ProgramaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#division.
    def visitDivision(self, ctx:lde_parser.DivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#suma.
    def visitSuma(self, ctx:lde_parser.SumaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#multiplicacion.
    def visitMultiplicacion(self, ctx:lde_parser.MultiplicacionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#numero.
    def visitNumero(self, ctx:lde_parser.NumeroContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#negativo.
    def visitNegativo(self, ctx:lde_parser.NegativoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#resta.
    def visitResta(self, ctx:lde_parser.RestaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#parenExpr.
    def visitParenExpr(self, ctx:lde_parser.ParenExprContext):
        return self.visitChildren(ctx)



del lde_parser