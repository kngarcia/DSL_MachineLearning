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


    # Visit a parse tree produced by lde_parser#expresion.
    def visitExpresion(self, ctx:lde_parser.ExpresionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#termino.
    def visitTermino(self, ctx:lde_parser.TerminoContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#factor.
    def visitFactor(self, ctx:lde_parser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#trigonometrica.
    def visitTrigonometrica(self, ctx:lde_parser.TrigonometricaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#lista.
    def visitLista(self, ctx:lde_parser.ListaContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by lde_parser#matriz.
    def visitMatriz(self, ctx:lde_parser.MatrizContext):
        return self.visitChildren(ctx)



del lde_parser