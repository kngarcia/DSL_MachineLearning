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
        4,1,27,99,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,1,0,1,0,1,0,5,0,22,8,0,10,0,12,0,25,9,0,1,0,1,
        0,1,1,1,1,1,1,1,1,1,1,1,2,1,2,1,2,5,2,37,8,2,10,2,12,2,40,9,2,1,
        3,1,3,1,3,1,3,1,3,1,4,1,4,1,4,5,4,50,8,4,10,4,12,4,53,9,4,1,5,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,66,8,5,1,6,1,6,1,6,1,6,
        1,6,1,7,1,7,1,7,1,7,5,7,77,8,7,10,7,12,7,80,9,7,3,7,82,8,7,1,7,1,
        7,1,8,1,8,1,8,1,8,5,8,90,8,8,10,8,12,8,93,9,8,3,8,95,8,8,1,8,1,8,
        1,8,0,0,9,0,2,4,6,8,10,12,14,16,0,3,1,0,3,4,1,0,5,9,1,0,11,19,104,
        0,23,1,0,0,0,2,28,1,0,0,0,4,33,1,0,0,0,6,41,1,0,0,0,8,46,1,0,0,0,
        10,65,1,0,0,0,12,67,1,0,0,0,14,72,1,0,0,0,16,85,1,0,0,0,18,22,3,
        2,1,0,19,22,3,4,2,0,20,22,3,6,3,0,21,18,1,0,0,0,21,19,1,0,0,0,21,
        20,1,0,0,0,22,25,1,0,0,0,23,21,1,0,0,0,23,24,1,0,0,0,24,26,1,0,0,
        0,25,23,1,0,0,0,26,27,5,0,0,1,27,1,1,0,0,0,28,29,5,1,0,0,29,30,5,
        25,0,0,30,31,5,10,0,0,31,32,3,4,2,0,32,3,1,0,0,0,33,38,3,8,4,0,34,
        35,7,0,0,0,35,37,3,8,4,0,36,34,1,0,0,0,37,40,1,0,0,0,38,36,1,0,0,
        0,38,39,1,0,0,0,39,5,1,0,0,0,40,38,1,0,0,0,41,42,5,2,0,0,42,43,5,
        20,0,0,43,44,3,4,2,0,44,45,5,21,0,0,45,7,1,0,0,0,46,51,3,10,5,0,
        47,48,7,1,0,0,48,50,3,10,5,0,49,47,1,0,0,0,50,53,1,0,0,0,51,49,1,
        0,0,0,51,52,1,0,0,0,52,9,1,0,0,0,53,51,1,0,0,0,54,66,5,26,0,0,55,
        66,5,25,0,0,56,57,5,20,0,0,57,58,3,4,2,0,58,59,5,21,0,0,59,66,1,
        0,0,0,60,61,5,4,0,0,61,66,3,10,5,0,62,66,3,12,6,0,63,66,3,14,7,0,
        64,66,3,16,8,0,65,54,1,0,0,0,65,55,1,0,0,0,65,56,1,0,0,0,65,60,1,
        0,0,0,65,62,1,0,0,0,65,63,1,0,0,0,65,64,1,0,0,0,66,11,1,0,0,0,67,
        68,7,2,0,0,68,69,5,20,0,0,69,70,3,4,2,0,70,71,5,21,0,0,71,13,1,0,
        0,0,72,81,5,22,0,0,73,78,3,4,2,0,74,75,5,24,0,0,75,77,3,4,2,0,76,
        74,1,0,0,0,77,80,1,0,0,0,78,76,1,0,0,0,78,79,1,0,0,0,79,82,1,0,0,
        0,80,78,1,0,0,0,81,73,1,0,0,0,81,82,1,0,0,0,82,83,1,0,0,0,83,84,
        5,23,0,0,84,15,1,0,0,0,85,94,5,22,0,0,86,91,3,14,7,0,87,88,5,24,
        0,0,88,90,3,14,7,0,89,87,1,0,0,0,90,93,1,0,0,0,91,89,1,0,0,0,91,
        92,1,0,0,0,92,95,1,0,0,0,93,91,1,0,0,0,94,86,1,0,0,0,94,95,1,0,0,
        0,95,96,1,0,0,0,96,97,5,23,0,0,97,17,1,0,0,0,9,21,23,38,51,65,78,
        81,91,94
    ]

class lde_parser ( Parser ):

    grammarFileName = "lde_parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'write'", "'+'", "'-'", "'*'", 
                     "'/'", "'%'", "'^'", "'@'", "'='", "'sin'", "'cos'", 
                     "'tan'", "'asin'", "'acos'", "'atan'", "'sinh'", "'cosh'", 
                     "'tanh'", "'('", "')'", "'['", "']'", "','" ]

    symbolicNames = [ "<INVALID>", "VAR", "WRITE", "SUMA", "RESTA", "MULT", 
                      "DIV", "MOD", "EXP", "PROD", "IGUAL", "SIN", "COS", 
                      "TAN", "ASIN", "ACOS", "ATAN", "SINH", "COSH", "TANH", 
                      "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", "COMA", 
                      "ID", "NUMERO", "ESPACIO" ]

    RULE_programa = 0
    RULE_declaracion = 1
    RULE_expresion = 2
    RULE_writeStmt = 3
    RULE_termino = 4
    RULE_factor = 5
    RULE_trigonometrica = 6
    RULE_lista = 7
    RULE_matriz = 8

    ruleNames =  [ "programa", "declaracion", "expresion", "writeStmt", 
                   "termino", "factor", "trigonometrica", "lista", "matriz" ]

    EOF = Token.EOF
    VAR=1
    WRITE=2
    SUMA=3
    RESTA=4
    MULT=5
    DIV=6
    MOD=7
    EXP=8
    PROD=9
    IGUAL=10
    SIN=11
    COS=12
    TAN=13
    ASIN=14
    ACOS=15
    ATAN=16
    SINH=17
    COSH=18
    TANH=19
    LPAREN=20
    RPAREN=21
    LBRACKET=22
    RBRACKET=23
    COMA=24
    ID=25
    NUMERO=26
    ESPACIO=27

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

        def EOF(self):
            return self.getToken(lde_parser.EOF, 0)

        def declaracion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.DeclaracionContext)
            else:
                return self.getTypedRuleContext(lde_parser.DeclaracionContext,i)


        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(lde_parser.ExpresionContext,i)


        def writeStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.WriteStmtContext)
            else:
                return self.getTypedRuleContext(lde_parser.WriteStmtContext,i)


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
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 23
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 106952726) != 0):
                self.state = 21
                self._errHandler.sync(self)
                token = self._input.LA(1)
                if token in [1]:
                    self.state = 18
                    self.declaracion()
                    pass
                elif token in [4, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 22, 25, 26]:
                    self.state = 19
                    self.expresion()
                    pass
                elif token in [2]:
                    self.state = 20
                    self.writeStmt()
                    pass
                else:
                    raise NoViableAltException(self)

                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 26
            self.match(lde_parser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DeclaracionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR(self):
            return self.getToken(lde_parser.VAR, 0)

        def ID(self):
            return self.getToken(lde_parser.ID, 0)

        def IGUAL(self):
            return self.getToken(lde_parser.IGUAL, 0)

        def expresion(self):
            return self.getTypedRuleContext(lde_parser.ExpresionContext,0)


        def getRuleIndex(self):
            return lde_parser.RULE_declaracion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaracion" ):
                listener.enterDeclaracion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaracion" ):
                listener.exitDeclaracion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDeclaracion" ):
                return visitor.visitDeclaracion(self)
            else:
                return visitor.visitChildren(self)




    def declaracion(self):

        localctx = lde_parser.DeclaracionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_declaracion)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 28
            self.match(lde_parser.VAR)
            self.state = 29
            self.match(lde_parser.ID)
            self.state = 30
            self.match(lde_parser.IGUAL)
            self.state = 31
            self.expresion()
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
        self.enterRule(localctx, 4, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 33
            self.termino()
            self.state = 38
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,2,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 34
                    _la = self._input.LA(1)
                    if not(_la==3 or _la==4):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 35
                    self.termino() 
                self.state = 40
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,2,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WriteStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WRITE(self):
            return self.getToken(lde_parser.WRITE, 0)

        def LPAREN(self):
            return self.getToken(lde_parser.LPAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(lde_parser.ExpresionContext,0)


        def RPAREN(self):
            return self.getToken(lde_parser.RPAREN, 0)

        def getRuleIndex(self):
            return lde_parser.RULE_writeStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWriteStmt" ):
                listener.enterWriteStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWriteStmt" ):
                listener.exitWriteStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWriteStmt" ):
                return visitor.visitWriteStmt(self)
            else:
                return visitor.visitChildren(self)




    def writeStmt(self):

        localctx = lde_parser.WriteStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_writeStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(lde_parser.WRITE)
            self.state = 42
            self.match(lde_parser.LPAREN)
            self.state = 43
            self.expresion()
            self.state = 44
            self.match(lde_parser.RPAREN)
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

        def PROD(self, i:int=None):
            if i is None:
                return self.getTokens(lde_parser.PROD)
            else:
                return self.getToken(lde_parser.PROD, i)

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
        self.enterRule(localctx, 8, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 46
            self.factor()
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 992) != 0):
                self.state = 47
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 992) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 48
                self.factor()
                self.state = 53
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

        def ID(self):
            return self.getToken(lde_parser.ID, 0)

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
        self.enterRule(localctx, 10, self.RULE_factor)
        try:
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 54
                self.match(lde_parser.NUMERO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 55
                self.match(lde_parser.ID)
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 56
                self.match(lde_parser.LPAREN)
                self.state = 57
                self.expresion()
                self.state = 58
                self.match(lde_parser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 60
                self.match(lde_parser.RESTA)
                self.state = 61
                self.factor()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 62
                self.trigonometrica()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 63
                self.lista()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 64
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
        self.enterRule(localctx, 12, self.RULE_trigonometrica)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1046528) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 68
            self.match(lde_parser.LPAREN)
            self.state = 69
            self.expresion()
            self.state = 70
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
        self.enterRule(localctx, 14, self.RULE_lista)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 72
            self.match(lde_parser.LBRACKET)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 106952720) != 0):
                self.state = 73
                self.expresion()
                self.state = 78
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==24:
                    self.state = 74
                    self.match(lde_parser.COMA)
                    self.state = 75
                    self.expresion()
                    self.state = 80
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 83
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
        self.enterRule(localctx, 16, self.RULE_matriz)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 85
            self.match(lde_parser.LBRACKET)
            self.state = 94
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==22:
                self.state = 86
                self.lista()
                self.state = 91
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==24:
                    self.state = 87
                    self.match(lde_parser.COMA)
                    self.state = 88
                    self.lista()
                    self.state = 93
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 96
            self.match(lde_parser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





