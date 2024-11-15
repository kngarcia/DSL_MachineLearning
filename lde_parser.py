# Generated from lde_parser.g4 by ANTLR 4.13.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,22,77,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,1,0,1,0,1,0,1,1,1,1,1,1,5,1,21,8,1,10,1,12,1,24,9,1,1,2,1,2,1,
        2,5,2,29,8,2,10,2,12,2,32,9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,3,1,
        3,1,3,3,3,44,8,3,1,4,1,4,1,4,1,4,1,4,1,5,1,5,1,5,1,5,5,5,55,8,5,
        10,5,12,5,58,9,5,3,5,60,8,5,1,5,1,5,1,6,1,6,1,6,1,6,5,6,68,8,6,10,
        6,12,6,71,9,6,3,6,73,8,6,1,6,1,6,1,6,0,0,7,0,2,4,6,8,10,12,0,3,1,
        0,1,2,1,0,3,6,1,0,7,15,80,0,14,1,0,0,0,2,17,1,0,0,0,4,25,1,0,0,0,
        6,43,1,0,0,0,8,45,1,0,0,0,10,50,1,0,0,0,12,63,1,0,0,0,14,15,3,2,
        1,0,15,16,5,0,0,1,16,1,1,0,0,0,17,22,3,4,2,0,18,19,7,0,0,0,19,21,
        3,4,2,0,20,18,1,0,0,0,21,24,1,0,0,0,22,20,1,0,0,0,22,23,1,0,0,0,
        23,3,1,0,0,0,24,22,1,0,0,0,25,30,3,6,3,0,26,27,7,1,0,0,27,29,3,6,
        3,0,28,26,1,0,0,0,29,32,1,0,0,0,30,28,1,0,0,0,30,31,1,0,0,0,31,5,
        1,0,0,0,32,30,1,0,0,0,33,44,5,21,0,0,34,35,5,16,0,0,35,36,3,2,1,
        0,36,37,5,17,0,0,37,44,1,0,0,0,38,39,5,2,0,0,39,44,3,6,3,0,40,44,
        3,8,4,0,41,44,3,10,5,0,42,44,3,12,6,0,43,33,1,0,0,0,43,34,1,0,0,
        0,43,38,1,0,0,0,43,40,1,0,0,0,43,41,1,0,0,0,43,42,1,0,0,0,44,7,1,
        0,0,0,45,46,7,2,0,0,46,47,5,16,0,0,47,48,3,2,1,0,48,49,5,17,0,0,
        49,9,1,0,0,0,50,59,5,18,0,0,51,56,3,2,1,0,52,53,5,20,0,0,53,55,3,
        2,1,0,54,52,1,0,0,0,55,58,1,0,0,0,56,54,1,0,0,0,56,57,1,0,0,0,57,
        60,1,0,0,0,58,56,1,0,0,0,59,51,1,0,0,0,59,60,1,0,0,0,60,61,1,0,0,
        0,61,62,5,19,0,0,62,11,1,0,0,0,63,72,5,18,0,0,64,69,3,10,5,0,65,
        66,5,20,0,0,66,68,3,10,5,0,67,65,1,0,0,0,68,71,1,0,0,0,69,67,1,0,
        0,0,69,70,1,0,0,0,70,73,1,0,0,0,71,69,1,0,0,0,72,64,1,0,0,0,72,73,
        1,0,0,0,73,74,1,0,0,0,74,75,5,19,0,0,75,13,1,0,0,0,7,22,30,43,56,
        59,69,72
    ]

class lde_parser ( Parser ):

    grammarFileName = "lde_parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'^'", 
                     "'sin'", "'cos'", "'tan'", "'asin'", "'acos'", "'atan'", 
                     "'sinh'", "'cosh'", "'tanh'", "'('", "')'", "'['", 
                     "']'", "','" ]

    symbolicNames = [ "<INVALID>", "SUMA", "RESTA", "MULT", "DIV", "MOD", 
                      "EXP", "SIN", "COS", "TAN", "ASIN", "ACOS", "ATAN", 
                      "SINH", "COSH", "TANH", "LPAREN", "RPAREN", "LBRACKET", 
                      "RBRACKET", "COMA", "NUMERO", "ESPACIO" ]

    RULE_programa = 0
    RULE_expresion = 1
    RULE_termino = 2
    RULE_factor = 3
    RULE_trigonometrica = 4
    RULE_lista = 5
    RULE_matriz = 6

    ruleNames =  [ "programa", "expresion", "termino", "factor", "trigonometrica", 
                   "lista", "matriz" ]

    EOF = Token.EOF
    SUMA=1
    RESTA=2
    MULT=3
    DIV=4
    MOD=5
    EXP=6
    SIN=7
    COS=8
    TAN=9
    ASIN=10
    ACOS=11
    ATAN=12
    SINH=13
    COSH=14
    TANH=15
    LPAREN=16
    RPAREN=17
    LBRACKET=18
    RBRACKET=19
    COMA=20
    NUMERO=21
    ESPACIO=22

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self):
            return self.getTypedRuleContext(lde_parser.ExpresionContext,0)


        def EOF(self):
            return self.getToken(lde_parser.EOF, 0)

        def getRuleIndex(self):
            return lde_parser.RULE_programa

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrograma" ):
                listener.enterPrograma(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrograma" ):
                listener.exitPrograma(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPrograma" ):
                return visitor.visitPrograma(self)
            else:
                return visitor.visitChildren(self)




    def programa(self):

        localctx = lde_parser.ProgramaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_programa)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            self.expresion()
            self.state = 15
            self.match(lde_parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpresionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def termino(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.TerminoContext)
            else:
                return self.getTypedRuleContext(lde_parser.TerminoContext,i)


        def SUMA(self, i:int=None):
            if i is None:
                return self.getTokens(lde_parser.SUMA)
            else:
                return self.getToken(lde_parser.SUMA, i)

        def RESTA(self, i:int=None):
            if i is None:
                return self.getTokens(lde_parser.RESTA)
            else:
                return self.getToken(lde_parser.RESTA, i)

        def getRuleIndex(self):
            return lde_parser.RULE_expresion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExpresion" ):
                listener.enterExpresion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExpresion" ):
                listener.exitExpresion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExpresion" ):
                return visitor.visitExpresion(self)
            else:
                return visitor.visitChildren(self)




    def expresion(self):

        localctx = lde_parser.ExpresionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 17
            self.termino()
            self.state = 22
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 18
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 19
                self.termino()
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TerminoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def factor(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.FactorContext)
            else:
                return self.getTypedRuleContext(lde_parser.FactorContext,i)


        def MULT(self, i:int=None):
            if i is None:
                return self.getTokens(lde_parser.MULT)
            else:
                return self.getToken(lde_parser.MULT, i)

        def DIV(self, i:int=None):
            if i is None:
                return self.getTokens(lde_parser.DIV)
            else:
                return self.getToken(lde_parser.DIV, i)

        def MOD(self, i:int=None):
            if i is None:
                return self.getTokens(lde_parser.MOD)
            else:
                return self.getToken(lde_parser.MOD, i)

        def EXP(self, i:int=None):
            if i is None:
                return self.getTokens(lde_parser.EXP)
            else:
                return self.getToken(lde_parser.EXP, i)

        def getRuleIndex(self):
            return lde_parser.RULE_termino

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTermino" ):
                listener.enterTermino(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTermino" ):
                listener.exitTermino(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermino" ):
                return visitor.visitTermino(self)
            else:
                return visitor.visitChildren(self)




    def termino(self):

        localctx = lde_parser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self.factor()
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 120) != 0):
                self.state = 26
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 120) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 27
                self.factor()
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FactorContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def NUMERO(self):
            return self.getToken(lde_parser.NUMERO, 0)

        def LPAREN(self):
            return self.getToken(lde_parser.LPAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(lde_parser.ExpresionContext,0)


        def RPAREN(self):
            return self.getToken(lde_parser.RPAREN, 0)

        def RESTA(self):
            return self.getToken(lde_parser.RESTA, 0)

        def factor(self):
            return self.getTypedRuleContext(lde_parser.FactorContext,0)


        def trigonometrica(self):
            return self.getTypedRuleContext(lde_parser.TrigonometricaContext,0)


        def lista(self):
            return self.getTypedRuleContext(lde_parser.ListaContext,0)


        def matriz(self):
            return self.getTypedRuleContext(lde_parser.MatrizContext,0)


        def getRuleIndex(self):
            return lde_parser.RULE_factor

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFactor" ):
                listener.enterFactor(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFactor" ):
                listener.exitFactor(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = lde_parser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_factor)
        try:
            self.state = 43
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 33
                self.match(lde_parser.NUMERO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 34
                self.match(lde_parser.LPAREN)
                self.state = 35
                self.expresion()
                self.state = 36
                self.match(lde_parser.RPAREN)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 38
                self.match(lde_parser.RESTA)
                self.state = 39
                self.factor()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 40
                self.trigonometrica()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 41
                self.lista()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 42
                self.matriz()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TrigonometricaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LPAREN(self):
            return self.getToken(lde_parser.LPAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(lde_parser.ExpresionContext,0)


        def RPAREN(self):
            return self.getToken(lde_parser.RPAREN, 0)

        def SIN(self):
            return self.getToken(lde_parser.SIN, 0)

        def COS(self):
            return self.getToken(lde_parser.COS, 0)

        def TAN(self):
            return self.getToken(lde_parser.TAN, 0)

        def ASIN(self):
            return self.getToken(lde_parser.ASIN, 0)

        def ACOS(self):
            return self.getToken(lde_parser.ACOS, 0)

        def ATAN(self):
            return self.getToken(lde_parser.ATAN, 0)

        def SINH(self):
            return self.getToken(lde_parser.SINH, 0)

        def COSH(self):
            return self.getToken(lde_parser.COSH, 0)

        def TANH(self):
            return self.getToken(lde_parser.TANH, 0)

        def getRuleIndex(self):
            return lde_parser.RULE_trigonometrica

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTrigonometrica" ):
                listener.enterTrigonometrica(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTrigonometrica" ):
                listener.exitTrigonometrica(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrigonometrica" ):
                return visitor.visitTrigonometrica(self)
            else:
                return visitor.visitChildren(self)




    def trigonometrica(self):

        localctx = lde_parser.TrigonometricaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_trigonometrica)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 65408) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 46
            self.match(lde_parser.LPAREN)
            self.state = 47
            self.expresion()
            self.state = 48
            self.match(lde_parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ListaContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(lde_parser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(lde_parser.RBRACKET, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(lde_parser.ExpresionContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(lde_parser.COMA)
            else:
                return self.getToken(lde_parser.COMA, i)

        def getRuleIndex(self):
            return lde_parser.RULE_lista

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLista" ):
                listener.enterLista(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLista" ):
                listener.exitLista(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista" ):
                return visitor.visitLista(self)
            else:
                return visitor.visitChildren(self)




    def lista(self):

        localctx = lde_parser.ListaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_lista)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 50
            self.match(lde_parser.LBRACKET)
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 2490244) != 0):
                self.state = 51
                self.expresion()
                self.state = 56
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==20:
                    self.state = 52
                    self.match(lde_parser.COMA)
                    self.state = 53
                    self.expresion()
                    self.state = 58
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 61
            self.match(lde_parser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class MatrizContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(lde_parser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(lde_parser.RBRACKET, 0)

        def lista(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.ListaContext)
            else:
                return self.getTypedRuleContext(lde_parser.ListaContext,i)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(lde_parser.COMA)
            else:
                return self.getToken(lde_parser.COMA, i)

        def getRuleIndex(self):
            return lde_parser.RULE_matriz

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMatriz" ):
                listener.enterMatriz(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMatriz" ):
                listener.exitMatriz(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatriz" ):
                return visitor.visitMatriz(self)
            else:
                return visitor.visitChildren(self)




    def matriz(self):

        localctx = lde_parser.MatrizContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_matriz)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(lde_parser.LBRACKET)
            self.state = 72
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==18:
                self.state = 64
                self.lista()
                self.state = 69
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==20:
                    self.state = 65
                    self.match(lde_parser.COMA)
                    self.state = 66
                    self.lista()
                    self.state = 71
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 74
            self.match(lde_parser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





