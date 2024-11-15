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
        4,1,13,40,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,5,0,12,8,0,
        10,0,12,0,15,9,0,1,1,1,1,1,1,5,1,20,8,1,10,1,12,1,23,9,1,1,2,1,2,
        1,2,1,2,1,2,1,2,1,2,1,2,3,2,33,8,2,1,3,1,3,1,3,1,3,1,3,1,3,0,0,4,
        0,2,4,6,0,3,1,0,1,2,1,0,3,6,1,0,7,9,40,0,8,1,0,0,0,2,16,1,0,0,0,
        4,32,1,0,0,0,6,34,1,0,0,0,8,13,3,2,1,0,9,10,7,0,0,0,10,12,3,2,1,
        0,11,9,1,0,0,0,12,15,1,0,0,0,13,11,1,0,0,0,13,14,1,0,0,0,14,1,1,
        0,0,0,15,13,1,0,0,0,16,21,3,4,2,0,17,18,7,1,0,0,18,20,3,4,2,0,19,
        17,1,0,0,0,20,23,1,0,0,0,21,19,1,0,0,0,21,22,1,0,0,0,22,3,1,0,0,
        0,23,21,1,0,0,0,24,33,5,12,0,0,25,26,5,10,0,0,26,27,3,0,0,0,27,28,
        5,11,0,0,28,33,1,0,0,0,29,30,5,2,0,0,30,33,3,4,2,0,31,33,3,6,3,0,
        32,24,1,0,0,0,32,25,1,0,0,0,32,29,1,0,0,0,32,31,1,0,0,0,33,5,1,0,
        0,0,34,35,7,2,0,0,35,36,5,10,0,0,36,37,3,0,0,0,37,38,5,11,0,0,38,
        7,1,0,0,0,3,13,21,32
    ]

class lde_parser ( Parser ):

    grammarFileName = "lde_parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'%'", "'^'", 
                     "'sin'", "'cos'", "'tan'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "SUMA", "RESTA", "MULT", "DIV", "MOD", 
                      "EXP", "SIN", "COS", "TAN", "LPAREN", "RPAREN", "NUMERO", 
                      "ESPACIO" ]

    RULE_expresion = 0
    RULE_termino = 1
    RULE_factor = 2
    RULE_trigonometrica = 3

    ruleNames =  [ "expresion", "termino", "factor", "trigonometrica" ]

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
    LPAREN=10
    RPAREN=11
    NUMERO=12
    ESPACIO=13

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




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
        self.enterRule(localctx, 0, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 8
            self.termino()
            self.state = 13
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 9
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 10
                self.termino()
                self.state = 15
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
        self.enterRule(localctx, 2, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.factor()
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 120) != 0):
                self.state = 17
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 120) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 18
                self.factor()
                self.state = 23
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
        self.enterRule(localctx, 4, self.RULE_factor)
        try:
            self.state = 32
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [12]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                self.match(lde_parser.NUMERO)
                pass
            elif token in [10]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                self.match(lde_parser.LPAREN)
                self.state = 26
                self.expresion()
                self.state = 27
                self.match(lde_parser.RPAREN)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 29
                self.match(lde_parser.RESTA)
                self.state = 30
                self.factor()
                pass
            elif token in [7, 8, 9]:
                self.enterOuterAlt(localctx, 4)
                self.state = 31
                self.trigonometrica()
                pass
            else:
                raise NoViableAltException(self)

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
        self.enterRule(localctx, 6, self.RULE_trigonometrica)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 896) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 35
            self.match(lde_parser.LPAREN)
            self.state = 36
            self.expresion()
            self.state = 37
            self.match(lde_parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





