# Generated from lde_lexer.g4 by ANTLR 4.13.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    return [
        4,0,8,49,6,-1,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,
        6,7,6,2,7,7,7,1,0,1,0,1,1,1,1,1,2,1,2,1,3,1,3,1,4,1,4,1,5,1,5,1,
        6,3,6,31,8,6,1,6,4,6,34,8,6,11,6,12,6,35,1,6,1,6,4,6,40,8,6,11,6,
        12,6,41,3,6,44,8,6,1,7,1,7,1,7,1,7,0,0,8,1,1,3,2,5,3,7,4,9,5,11,
        6,13,7,15,8,1,0,2,1,0,48,57,3,0,9,10,13,13,32,32,52,0,1,1,0,0,0,
        0,3,1,0,0,0,0,5,1,0,0,0,0,7,1,0,0,0,0,9,1,0,0,0,0,11,1,0,0,0,0,13,
        1,0,0,0,0,15,1,0,0,0,1,17,1,0,0,0,3,19,1,0,0,0,5,21,1,0,0,0,7,23,
        1,0,0,0,9,25,1,0,0,0,11,27,1,0,0,0,13,30,1,0,0,0,15,45,1,0,0,0,17,
        18,5,43,0,0,18,2,1,0,0,0,19,20,5,45,0,0,20,4,1,0,0,0,21,22,5,42,
        0,0,22,6,1,0,0,0,23,24,5,47,0,0,24,8,1,0,0,0,25,26,5,40,0,0,26,10,
        1,0,0,0,27,28,5,41,0,0,28,12,1,0,0,0,29,31,5,45,0,0,30,29,1,0,0,
        0,30,31,1,0,0,0,31,33,1,0,0,0,32,34,7,0,0,0,33,32,1,0,0,0,34,35,
        1,0,0,0,35,33,1,0,0,0,35,36,1,0,0,0,36,43,1,0,0,0,37,39,5,46,0,0,
        38,40,7,0,0,0,39,38,1,0,0,0,40,41,1,0,0,0,41,39,1,0,0,0,41,42,1,
        0,0,0,42,44,1,0,0,0,43,37,1,0,0,0,43,44,1,0,0,0,44,14,1,0,0,0,45,
        46,7,1,0,0,46,47,1,0,0,0,47,48,6,7,0,0,48,16,1,0,0,0,5,0,30,35,41,
        43,1,6,0,0
    ]

class lde_lexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    SUMA = 1
    RESTA = 2
    MULT = 3
    DIV = 4
    LPAREN = 5
    RPAREN = 6
    NUMERO = 7
    ESPACIO = 8

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "SUMA", "RESTA", "MULT", "DIV", "LPAREN", "RPAREN", "NUMERO", 
            "ESPACIO" ]

    ruleNames = [ "SUMA", "RESTA", "MULT", "DIV", "LPAREN", "RPAREN", "NUMERO", 
                  "ESPACIO" ]

    grammarFileName = "lde_lexer.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.13.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None

