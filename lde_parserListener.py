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


    # Enter a parse tree produced by lde_parser#expresion.
    def enterExpresion(self, ctx:lde_parser.ExpresionContext):
        pass

    # Exit a parse tree produced by lde_parser#expresion.
    def exitExpresion(self, ctx:lde_parser.ExpresionContext):
        pass


    # Enter a parse tree produced by lde_parser#termino.
    def enterTermino(self, ctx:lde_parser.TerminoContext):
        pass

    # Exit a parse tree produced by lde_parser#termino.
    def exitTermino(self, ctx:lde_parser.TerminoContext):
        pass


    # Enter a parse tree produced by lde_parser#factor.
    def enterFactor(self, ctx:lde_parser.FactorContext):
        pass

    # Exit a parse tree produced by lde_parser#factor.
    def exitFactor(self, ctx:lde_parser.FactorContext):
        pass



del lde_parser