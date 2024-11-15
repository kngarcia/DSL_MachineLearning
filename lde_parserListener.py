# Generated from lde_parser.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .lde_parser import lde_parser
else:
    from lde_parser import lde_parser

# This class defines a complete listener for a parse tree produced by lde_parser.
class lde_parserListener(ParseTreeListener):

    # Enter a parse tree produced by lde_parser#programa.
    def enterPrograma(self, ctx:lde_parser.ProgramaContext):
        pass

    # Exit a parse tree produced by lde_parser#programa.
    def exitPrograma(self, ctx:lde_parser.ProgramaContext):
        pass


    # Enter a parse tree produced by lde_parser#suma.
    def enterSuma(self, ctx:lde_parser.SumaContext):
        pass

    # Exit a parse tree produced by lde_parser#suma.
    def exitSuma(self, ctx:lde_parser.SumaContext):
        pass


    # Enter a parse tree produced by lde_parser#division.
    def enterDivision(self, ctx:lde_parser.DivisionContext):
        pass

    # Exit a parse tree produced by lde_parser#division.
    def exitDivision(self, ctx:lde_parser.DivisionContext):
        pass


    # Enter a parse tree produced by lde_parser#multiplicacion.
    def enterMultiplicacion(self, ctx:lde_parser.MultiplicacionContext):
        pass

    # Exit a parse tree produced by lde_parser#multiplicacion.
    def exitMultiplicacion(self, ctx:lde_parser.MultiplicacionContext):
        pass


    # Enter a parse tree produced by lde_parser#numero.
    def enterNumero(self, ctx:lde_parser.NumeroContext):
        pass

    # Exit a parse tree produced by lde_parser#numero.
    def exitNumero(self, ctx:lde_parser.NumeroContext):
        pass


    # Enter a parse tree produced by lde_parser#negativo.
    def enterNegativo(self, ctx:lde_parser.NegativoContext):
        pass

    # Exit a parse tree produced by lde_parser#negativo.
    def exitNegativo(self, ctx:lde_parser.NegativoContext):
        pass


    # Enter a parse tree produced by lde_parser#resta.
    def enterResta(self, ctx:lde_parser.RestaContext):
        pass

    # Exit a parse tree produced by lde_parser#resta.
    def exitResta(self, ctx:lde_parser.RestaContext):
        pass


    # Enter a parse tree produced by lde_parser#parenExpr.
    def enterParenExpr(self, ctx:lde_parser.ParenExprContext):
        pass

    # Exit a parse tree produced by lde_parser#parenExpr.
    def exitParenExpr(self, ctx:lde_parser.ParenExprContext):
        pass



del lde_parser