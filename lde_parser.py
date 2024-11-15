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
        4,1,8,37,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,1,0,1,0,1,0,1,1,1,1,1,1,
        5,1,15,8,1,10,1,12,1,18,9,1,1,2,1,2,1,2,5,2,23,8,2,10,2,12,2,26,
        9,2,1,3,1,3,1,3,1,3,1,3,1,3,1,3,3,3,35,8,3,1,3,0,0,4,0,2,4,6,0,2,
        1,0,1,2,1,0,3,4,36,0,8,1,0,0,0,2,11,1,0,0,0,4,19,1,0,0,0,6,34,1,
        0,0,0,8,9,3,2,1,0,9,10,5,0,0,1,10,1,1,0,0,0,11,16,3,4,2,0,12,13,
        7,0,0,0,13,15,3,4,2,0,14,12,1,0,0,0,15,18,1,0,0,0,16,14,1,0,0,0,
        16,17,1,0,0,0,17,3,1,0,0,0,18,16,1,0,0,0,19,24,3,6,3,0,20,21,7,1,
        0,0,21,23,3,6,3,0,22,20,1,0,0,0,23,26,1,0,0,0,24,22,1,0,0,0,24,25,
        1,0,0,0,25,5,1,0,0,0,26,24,1,0,0,0,27,35,5,7,0,0,28,29,5,5,0,0,29,
        30,3,2,1,0,30,31,5,6,0,0,31,35,1,0,0,0,32,33,5,2,0,0,33,35,3,6,3,
        0,34,27,1,0,0,0,34,28,1,0,0,0,34,32,1,0,0,0,35,7,1,0,0,0,3,16,24,
        34
    ]

class lde_parser ( Parser ):

    grammarFileName = "lde_parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>", "SUMA", "RESTA", "MULT", "DIV", "LPAREN", 
                      "RPAREN", "NUMERO", "ESPACIO" ]

    RULE_programa = 0
    RULE_expresion = 1
    RULE_termino = 2
    RULE_factor = 3

    ruleNames =  [ "programa", "expresion", "termino", "factor" ]

    EOF = Token.EOF
    SUMA=1
    RESTA=2
    MULT=3
    DIV=4
    LPAREN=5
    RPAREN=6
    NUMERO=7
    ESPACIO=8

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
            self.state = 8
            self.expresion()
            self.state = 9
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
            self.state = 11
            self.termino()
            self.state = 16
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==1 or _la==2:
                self.state = 12
                _la = self._input.LA(1)
                if not(_la==1 or _la==2):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 13
                self.termino()
                self.state = 18
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
            self.state = 19
            self.factor()
            self.state = 24
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==3 or _la==4:
                self.state = 20
                _la = self._input.LA(1)
                if not(_la==3 or _la==4):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 21
                self.factor()
                self.state = 26
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
            self.state = 34
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 27
                self.match(lde_parser.NUMERO)
                pass
            elif token in [5]:
                self.enterOuterAlt(localctx, 2)
                self.state = 28
                self.match(lde_parser.LPAREN)
                self.state = 29
                self.expresion()
                self.state = 30
                self.match(lde_parser.RPAREN)
                pass
            elif token in [2]:
                self.enterOuterAlt(localctx, 3)
                self.state = 32
                self.match(lde_parser.RESTA)
                self.state = 33
                self.factor()
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





