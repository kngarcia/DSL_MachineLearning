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
        4,1,63,310,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,1,0,1,0,1,
        0,1,0,1,0,3,0,58,8,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,69,
        8,0,10,0,12,0,72,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,3,1,82,8,1,
        1,2,1,2,3,2,86,8,2,1,2,1,2,1,2,1,2,3,2,92,8,2,1,3,1,3,1,3,5,3,97,
        8,3,10,3,12,3,100,9,3,1,4,1,4,1,4,1,4,1,4,3,4,107,8,4,1,4,1,4,1,
        5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,118,8,5,1,5,1,5,1,6,1,6,1,7,1,7,1,
        7,1,7,1,7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,140,8,
        9,1,9,1,9,1,9,1,9,3,9,146,8,9,1,10,1,10,1,10,1,10,3,10,152,8,10,
        1,10,1,10,1,10,3,10,157,8,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,
        1,11,1,11,1,11,3,11,169,8,11,1,11,1,11,1,11,1,12,1,12,1,13,1,13,
        1,13,1,13,1,13,1,13,1,13,1,14,1,14,1,14,1,14,1,14,1,14,3,14,189,
        8,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,1,14,5,14,200,8,14,
        10,14,12,14,203,9,14,1,14,1,14,1,15,1,15,1,15,5,15,210,8,15,10,15,
        12,15,213,9,15,1,16,1,16,1,16,1,16,1,16,3,16,220,8,16,1,16,1,16,
        1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,1,16,3,16,234,8,16,
        1,17,1,17,1,17,1,17,3,17,240,8,17,1,17,1,17,3,17,244,8,17,1,18,1,
        18,1,18,1,18,1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,1,
        19,1,19,1,20,1,20,1,20,1,20,1,20,1,21,1,21,1,21,1,21,1,21,1,22,1,
        22,1,22,1,22,5,22,276,8,22,10,22,12,22,279,9,22,3,22,281,8,22,1,
        22,1,22,1,23,1,23,1,23,1,23,5,23,289,8,23,10,23,12,23,292,9,23,3,
        23,294,8,23,1,23,1,23,1,24,1,24,1,24,1,24,1,25,1,25,1,25,1,25,1,
        25,1,25,3,25,308,8,25,1,25,0,0,26,0,2,4,6,8,10,12,14,16,18,20,22,
        24,26,28,30,32,34,36,38,40,42,44,46,48,50,0,7,1,0,18,19,1,0,12,17,
        1,0,20,23,1,0,9,10,1,0,25,33,1,0,44,49,1,0,50,51,347,0,70,1,0,0,
        0,2,75,1,0,0,0,4,83,1,0,0,0,6,93,1,0,0,0,8,101,1,0,0,0,10,110,1,
        0,0,0,12,121,1,0,0,0,14,123,1,0,0,0,16,128,1,0,0,0,18,135,1,0,0,
        0,20,147,1,0,0,0,22,163,1,0,0,0,24,173,1,0,0,0,26,175,1,0,0,0,28,
        182,1,0,0,0,30,206,1,0,0,0,32,233,1,0,0,0,34,235,1,0,0,0,36,245,
        1,0,0,0,38,253,1,0,0,0,40,261,1,0,0,0,42,266,1,0,0,0,44,271,1,0,
        0,0,46,284,1,0,0,0,48,297,1,0,0,0,50,307,1,0,0,0,52,69,3,40,20,0,
        53,69,3,2,1,0,54,69,3,6,3,0,55,58,3,48,24,0,56,58,3,50,25,0,57,55,
        1,0,0,0,57,56,1,0,0,0,58,69,1,0,0,0,59,69,3,8,4,0,60,69,3,10,5,0,
        61,69,3,16,8,0,62,69,3,4,2,0,63,69,3,18,9,0,64,69,3,20,10,0,65,69,
        3,22,11,0,66,69,3,24,12,0,67,69,3,26,13,0,68,52,1,0,0,0,68,53,1,
        0,0,0,68,54,1,0,0,0,68,57,1,0,0,0,68,59,1,0,0,0,68,60,1,0,0,0,68,
        61,1,0,0,0,68,62,1,0,0,0,68,63,1,0,0,0,68,64,1,0,0,0,68,65,1,0,0,
        0,68,66,1,0,0,0,68,67,1,0,0,0,69,72,1,0,0,0,70,68,1,0,0,0,70,71,
        1,0,0,0,71,73,1,0,0,0,72,70,1,0,0,0,73,74,5,0,0,1,74,1,1,0,0,0,75,
        76,5,1,0,0,76,77,5,60,0,0,77,81,5,24,0,0,78,82,3,6,3,0,79,82,3,14,
        7,0,80,82,3,26,13,0,81,78,1,0,0,0,81,79,1,0,0,0,81,80,1,0,0,0,82,
        3,1,0,0,0,83,85,5,60,0,0,84,86,3,34,17,0,85,84,1,0,0,0,85,86,1,0,
        0,0,86,87,1,0,0,0,87,91,5,24,0,0,88,92,3,6,3,0,89,92,3,14,7,0,90,
        92,3,26,13,0,91,88,1,0,0,0,91,89,1,0,0,0,91,90,1,0,0,0,92,5,1,0,
        0,0,93,98,3,30,15,0,94,95,7,0,0,0,95,97,3,30,15,0,96,94,1,0,0,0,
        97,100,1,0,0,0,98,96,1,0,0,0,98,99,1,0,0,0,99,7,1,0,0,0,100,98,1,
        0,0,0,101,102,5,2,0,0,102,106,5,34,0,0,103,107,3,6,3,0,104,107,3,
        48,24,0,105,107,3,50,25,0,106,103,1,0,0,0,106,104,1,0,0,0,106,105,
        1,0,0,0,107,108,1,0,0,0,108,109,5,35,0,0,109,9,1,0,0,0,110,111,5,
        3,0,0,111,112,5,34,0,0,112,113,3,12,6,0,113,114,5,58,0,0,114,117,
        3,6,3,0,115,116,5,58,0,0,116,118,3,6,3,0,117,115,1,0,0,0,117,118,
        1,0,0,0,118,119,1,0,0,0,119,120,5,35,0,0,120,11,1,0,0,0,121,122,
        7,1,0,0,122,13,1,0,0,0,123,124,5,4,0,0,124,125,5,34,0,0,125,126,
        5,6,0,0,126,127,5,35,0,0,127,15,1,0,0,0,128,129,5,5,0,0,129,130,
        5,34,0,0,130,131,3,6,3,0,131,132,5,58,0,0,132,133,5,6,0,0,133,134,
        5,35,0,0,134,17,1,0,0,0,135,136,5,40,0,0,136,139,5,34,0,0,137,140,
        3,48,24,0,138,140,3,50,25,0,139,137,1,0,0,0,139,138,1,0,0,0,140,
        141,1,0,0,0,141,142,5,35,0,0,142,145,3,28,14,0,143,144,5,41,0,0,
        144,146,3,28,14,0,145,143,1,0,0,0,145,146,1,0,0,0,146,19,1,0,0,0,
        147,148,5,55,0,0,148,151,5,34,0,0,149,152,3,2,1,0,150,152,5,60,0,
        0,151,149,1,0,0,0,151,150,1,0,0,0,152,153,1,0,0,0,153,156,5,58,0,
        0,154,157,3,48,24,0,155,157,3,50,25,0,156,154,1,0,0,0,156,155,1,
        0,0,0,157,158,1,0,0,0,158,159,5,58,0,0,159,160,3,4,2,0,160,161,5,
        35,0,0,161,162,3,28,14,0,162,21,1,0,0,0,163,164,5,56,0,0,164,168,
        5,34,0,0,165,169,5,42,0,0,166,169,3,48,24,0,167,169,3,50,25,0,168,
        165,1,0,0,0,168,166,1,0,0,0,168,167,1,0,0,0,169,170,1,0,0,0,170,
        171,5,35,0,0,171,172,3,28,14,0,172,23,1,0,0,0,173,174,5,57,0,0,174,
        25,1,0,0,0,175,176,5,7,0,0,176,177,5,34,0,0,177,178,3,6,3,0,178,
        179,5,58,0,0,179,180,3,6,3,0,180,181,5,35,0,0,181,27,1,0,0,0,182,
        201,5,53,0,0,183,200,3,40,20,0,184,200,3,2,1,0,185,200,3,6,3,0,186,
        189,3,48,24,0,187,189,3,50,25,0,188,186,1,0,0,0,188,187,1,0,0,0,
        189,200,1,0,0,0,190,200,3,8,4,0,191,200,3,10,5,0,192,200,3,16,8,
        0,193,200,3,4,2,0,194,200,3,18,9,0,195,200,3,20,10,0,196,200,3,22,
        11,0,197,200,3,24,12,0,198,200,3,26,13,0,199,183,1,0,0,0,199,184,
        1,0,0,0,199,185,1,0,0,0,199,188,1,0,0,0,199,190,1,0,0,0,199,191,
        1,0,0,0,199,192,1,0,0,0,199,193,1,0,0,0,199,194,1,0,0,0,199,195,
        1,0,0,0,199,196,1,0,0,0,199,197,1,0,0,0,199,198,1,0,0,0,200,203,
        1,0,0,0,201,199,1,0,0,0,201,202,1,0,0,0,202,204,1,0,0,0,203,201,
        1,0,0,0,204,205,5,54,0,0,205,29,1,0,0,0,206,211,3,32,16,0,207,208,
        7,2,0,0,208,210,3,32,16,0,209,207,1,0,0,0,210,213,1,0,0,0,211,209,
        1,0,0,0,211,212,1,0,0,0,212,31,1,0,0,0,213,211,1,0,0,0,214,234,5,
        61,0,0,215,219,5,60,0,0,216,220,3,34,17,0,217,220,3,36,18,0,218,
        220,3,38,19,0,219,216,1,0,0,0,219,217,1,0,0,0,219,218,1,0,0,0,219,
        220,1,0,0,0,220,234,1,0,0,0,221,222,5,34,0,0,222,223,3,6,3,0,223,
        224,5,35,0,0,224,234,1,0,0,0,225,226,5,19,0,0,226,234,3,32,16,0,
        227,234,3,42,21,0,228,234,3,44,22,0,229,234,3,46,23,0,230,234,5,
        62,0,0,231,234,5,42,0,0,232,234,5,43,0,0,233,214,1,0,0,0,233,215,
        1,0,0,0,233,221,1,0,0,0,233,225,1,0,0,0,233,227,1,0,0,0,233,228,
        1,0,0,0,233,229,1,0,0,0,233,230,1,0,0,0,233,231,1,0,0,0,233,232,
        1,0,0,0,234,33,1,0,0,0,235,239,5,36,0,0,236,240,3,6,3,0,237,240,
        5,9,0,0,238,240,5,10,0,0,239,236,1,0,0,0,239,237,1,0,0,0,239,238,
        1,0,0,0,240,241,1,0,0,0,241,243,5,37,0,0,242,244,3,34,17,0,243,242,
        1,0,0,0,243,244,1,0,0,0,244,35,1,0,0,0,245,246,5,59,0,0,246,247,
        5,38,0,0,247,248,5,34,0,0,248,249,7,3,0,0,249,250,5,58,0,0,250,251,
        3,6,3,0,251,252,5,35,0,0,252,37,1,0,0,0,253,254,5,59,0,0,254,255,
        5,39,0,0,255,256,5,34,0,0,256,257,7,3,0,0,257,258,5,58,0,0,258,259,
        3,6,3,0,259,260,5,35,0,0,260,39,1,0,0,0,261,262,5,11,0,0,262,263,
        5,34,0,0,263,264,3,32,16,0,264,265,5,35,0,0,265,41,1,0,0,0,266,267,
        7,4,0,0,267,268,5,34,0,0,268,269,3,6,3,0,269,270,5,35,0,0,270,43,
        1,0,0,0,271,280,5,36,0,0,272,277,3,6,3,0,273,274,5,58,0,0,274,276,
        3,6,3,0,275,273,1,0,0,0,276,279,1,0,0,0,277,275,1,0,0,0,277,278,
        1,0,0,0,278,281,1,0,0,0,279,277,1,0,0,0,280,272,1,0,0,0,280,281,
        1,0,0,0,281,282,1,0,0,0,282,283,5,37,0,0,283,45,1,0,0,0,284,293,
        5,36,0,0,285,290,3,44,22,0,286,287,5,58,0,0,287,289,3,44,22,0,288,
        286,1,0,0,0,289,292,1,0,0,0,290,288,1,0,0,0,290,291,1,0,0,0,291,
        294,1,0,0,0,292,290,1,0,0,0,293,285,1,0,0,0,293,294,1,0,0,0,294,
        295,1,0,0,0,295,296,5,37,0,0,296,47,1,0,0,0,297,298,3,6,3,0,298,
        299,7,5,0,0,299,300,3,6,3,0,300,49,1,0,0,0,301,302,3,6,3,0,302,303,
        7,6,0,0,303,304,3,6,3,0,304,308,1,0,0,0,305,306,5,52,0,0,306,308,
        3,6,3,0,307,301,1,0,0,0,307,305,1,0,0,0,308,51,1,0,0,0,27,57,68,
        70,81,85,91,98,106,117,139,145,151,156,168,188,199,201,211,219,233,
        239,243,277,280,290,293,307
    ]

class lde_parser ( Parser ):

    grammarFileName = "lde_parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'write'", "'plot'", "'extract'", 
                     "'export'", "<INVALID>", "'regression'", "'classifier'", 
                     "'R'", "'C'", "'size'", "'bar_plot'", "'histogram'", 
                     "'scatter_plot'", "'scatter_density'", "'line_plot'", 
                     "'heatmap'", "'+'", "'-'", "'*'", "'/'", "'%'", "'^'", 
                     "'='", "'sin'", "'cos'", "'tan'", "'asin'", "'acos'", 
                     "'atan'", "'sinh'", "'cosh'", "'tanh'", "'('", "')'", 
                     "'['", "']'", "'add'", "'del'", "'if'", "'else'", "'true'", 
                     "'false'", "'>'", "'<'", "'>='", "'<='", "'=='", "'!='", 
                     "'and'", "'or'", "'not'", "'{'", "'}'", "'for'", "'while'", 
                     "'break'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "VAR", "WRITE", "GRAFICAR", "EXTRAER", 
                      "EXPORTAR", "ARCHIVO", "REGRESION", "CLASIFICADOR", 
                      "ROWS", "COLUMNS", "TAMANO", "BARRASPLOT", "HISTOGRAMA", 
                      "SCATTERPLOT", "SCATTERDENS", "LINEASPLOT", "HEATMAP", 
                      "SUMA", "RESTA", "MULT", "DIV", "MOD", "EXP", "IGUAL", 
                      "SIN", "COS", "TAN", "ASIN", "ACOS", "ATAN", "SINH", 
                      "COSH", "TANH", "LPAREN", "RPAREN", "LBRACKET", "RBRACKET", 
                      "ADD", "DEL", "IF", "ELSE", "TRUE", "FALSE", "MAYOR", 
                      "MENOR", "MAYOR_IGUAL", "MENOR_IGUAL", "IGUALDAD", 
                      "DIFERENTE", "AND", "OR", "NOT", "INBLOCK", "ENBLOCK", 
                      "FOR", "WHILE", "BREAK", "COMA", "PUNTO", "ID", "NUMERO", 
                      "STRING", "ESPACIO" ]

    RULE_programa = 0
    RULE_declaracion = 1
    RULE_modificacion = 2
    RULE_expresion = 3
    RULE_writeStmt = 4
    RULE_graficarStmt = 5
    RULE_tipoGrafico = 6
    RULE_extraerStmt = 7
    RULE_exportarStmt = 8
    RULE_ifStmt = 9
    RULE_forStmt = 10
    RULE_whileStmt = 11
    RULE_breakStmt = 12
    RULE_regresionLinealStmt = 13
    RULE_bloque = 14
    RULE_termino = 15
    RULE_factor = 16
    RULE_acceso = 17
    RULE_addStmt = 18
    RULE_delStmt = 19
    RULE_sizeStmt = 20
    RULE_trigonometrica = 21
    RULE_lista = 22
    RULE_matriz = 23
    RULE_relacional = 24
    RULE_logico = 25

    ruleNames =  [ "programa", "declaracion", "modificacion", "expresion", 
                   "writeStmt", "graficarStmt", "tipoGrafico", "extraerStmt", 
                   "exportarStmt", "ifStmt", "forStmt", "whileStmt", "breakStmt", 
                   "regresionLinealStmt", "bloque", "termino", "factor", 
                   "acceso", "addStmt", "delStmt", "sizeStmt", "trigonometrica", 
                   "lista", "matriz", "relacional", "logico" ]

    EOF = Token.EOF
    VAR=1
    WRITE=2
    GRAFICAR=3
    EXTRAER=4
    EXPORTAR=5
    ARCHIVO=6
    REGRESION=7
    CLASIFICADOR=8
    ROWS=9
    COLUMNS=10
    TAMANO=11
    BARRASPLOT=12
    HISTOGRAMA=13
    SCATTERPLOT=14
    SCATTERDENS=15
    LINEASPLOT=16
    HEATMAP=17
    SUMA=18
    RESTA=19
    MULT=20
    DIV=21
    MOD=22
    EXP=23
    IGUAL=24
    SIN=25
    COS=26
    TAN=27
    ASIN=28
    ACOS=29
    ATAN=30
    SINH=31
    COSH=32
    TANH=33
    LPAREN=34
    RPAREN=35
    LBRACKET=36
    RBRACKET=37
    ADD=38
    DEL=39
    IF=40
    ELSE=41
    TRUE=42
    FALSE=43
    MAYOR=44
    MENOR=45
    MAYOR_IGUAL=46
    MENOR_IGUAL=47
    IGUALDAD=48
    DIFERENTE=49
    AND=50
    OR=51
    NOT=52
    INBLOCK=53
    ENBLOCK=54
    FOR=55
    WHILE=56
    BREAK=57
    COMA=58
    PUNTO=59
    ID=60
    NUMERO=61
    STRING=62
    ESPACIO=63

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

        def sizeStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.SizeStmtContext)
            else:
                return self.getTypedRuleContext(lde_parser.SizeStmtContext,i)


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


        def graficarStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.GraficarStmtContext)
            else:
                return self.getTypedRuleContext(lde_parser.GraficarStmtContext,i)


        def exportarStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.ExportarStmtContext)
            else:
                return self.getTypedRuleContext(lde_parser.ExportarStmtContext,i)


        def modificacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.ModificacionContext)
            else:
                return self.getTypedRuleContext(lde_parser.ModificacionContext,i)


        def ifStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.IfStmtContext)
            else:
                return self.getTypedRuleContext(lde_parser.IfStmtContext,i)


        def forStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.ForStmtContext)
            else:
                return self.getTypedRuleContext(lde_parser.ForStmtContext,i)


        def whileStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.WhileStmtContext)
            else:
                return self.getTypedRuleContext(lde_parser.WhileStmtContext,i)


        def breakStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.BreakStmtContext)
            else:
                return self.getTypedRuleContext(lde_parser.BreakStmtContext,i)


        def regresionLinealStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.RegresionLinealStmtContext)
            else:
                return self.getTypedRuleContext(lde_parser.RegresionLinealStmtContext,i)


        def relacional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.RelacionalContext)
            else:
                return self.getTypedRuleContext(lde_parser.RelacionalContext,i)


        def logico(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.LogicoContext)
            else:
                return self.getTypedRuleContext(lde_parser.LogicoContext,i)


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
            self.state = 70
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8327170107705395374) != 0):
                self.state = 68
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 52
                    self.sizeStmt()
                    pass

                elif la_ == 2:
                    self.state = 53
                    self.declaracion()
                    pass

                elif la_ == 3:
                    self.state = 54
                    self.expresion()
                    pass

                elif la_ == 4:
                    self.state = 57
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        self.state = 55
                        self.relacional()
                        pass

                    elif la_ == 2:
                        self.state = 56
                        self.logico()
                        pass


                    pass

                elif la_ == 5:
                    self.state = 59
                    self.writeStmt()
                    pass

                elif la_ == 6:
                    self.state = 60
                    self.graficarStmt()
                    pass

                elif la_ == 7:
                    self.state = 61
                    self.exportarStmt()
                    pass

                elif la_ == 8:
                    self.state = 62
                    self.modificacion()
                    pass

                elif la_ == 9:
                    self.state = 63
                    self.ifStmt()
                    pass

                elif la_ == 10:
                    self.state = 64
                    self.forStmt()
                    pass

                elif la_ == 11:
                    self.state = 65
                    self.whileStmt()
                    pass

                elif la_ == 12:
                    self.state = 66
                    self.breakStmt()
                    pass

                elif la_ == 13:
                    self.state = 67
                    self.regresionLinealStmt()
                    pass


                self.state = 72
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 73
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


        def extraerStmt(self):
            return self.getTypedRuleContext(lde_parser.ExtraerStmtContext,0)


        def regresionLinealStmt(self):
            return self.getTypedRuleContext(lde_parser.RegresionLinealStmtContext,0)


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
            self.state = 75
            self.match(lde_parser.VAR)
            self.state = 76
            self.match(lde_parser.ID)
            self.state = 77
            self.match(lde_parser.IGUAL)
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 42, 43, 60, 61, 62]:
                self.state = 78
                self.expresion()
                pass
            elif token in [4]:
                self.state = 79
                self.extraerStmt()
                pass
            elif token in [7]:
                self.state = 80
                self.regresionLinealStmt()
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


    class ModificacionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(lde_parser.ID, 0)

        def IGUAL(self):
            return self.getToken(lde_parser.IGUAL, 0)

        def expresion(self):
            return self.getTypedRuleContext(lde_parser.ExpresionContext,0)


        def extraerStmt(self):
            return self.getTypedRuleContext(lde_parser.ExtraerStmtContext,0)


        def regresionLinealStmt(self):
            return self.getTypedRuleContext(lde_parser.RegresionLinealStmtContext,0)


        def acceso(self):
            return self.getTypedRuleContext(lde_parser.AccesoContext,0)


        def getRuleIndex(self):
            return lde_parser.RULE_modificacion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterModificacion" ):
                listener.enterModificacion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitModificacion" ):
                listener.exitModificacion(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitModificacion" ):
                return visitor.visitModificacion(self)
            else:
                return visitor.visitChildren(self)




    def modificacion(self):

        localctx = lde_parser.ModificacionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_modificacion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 83
            self.match(lde_parser.ID)
            self.state = 85
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 84
                self.acceso()


            self.state = 87
            self.match(lde_parser.IGUAL)
            self.state = 91
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 42, 43, 60, 61, 62]:
                self.state = 88
                self.expresion()
                pass
            elif token in [4]:
                self.state = 89
                self.extraerStmt()
                pass
            elif token in [7]:
                self.state = 90
                self.regresionLinealStmt()
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
        self.enterRule(localctx, 6, self.RULE_expresion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 93
            self.termino()
            self.state = 98
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 94
                    _la = self._input.LA(1)
                    if not(_la==18 or _la==19):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 95
                    self.termino() 
                self.state = 100
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,6,self._ctx)

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

        def RPAREN(self):
            return self.getToken(lde_parser.RPAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(lde_parser.ExpresionContext,0)


        def relacional(self):
            return self.getTypedRuleContext(lde_parser.RelacionalContext,0)


        def logico(self):
            return self.getTypedRuleContext(lde_parser.LogicoContext,0)


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
        self.enterRule(localctx, 8, self.RULE_writeStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 101
            self.match(lde_parser.WRITE)
            self.state = 102
            self.match(lde_parser.LPAREN)
            self.state = 106
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 103
                self.expresion()
                pass

            elif la_ == 2:
                self.state = 104
                self.relacional()
                pass

            elif la_ == 3:
                self.state = 105
                self.logico()
                pass


            self.state = 108
            self.match(lde_parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class GraficarStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def GRAFICAR(self):
            return self.getToken(lde_parser.GRAFICAR, 0)

        def LPAREN(self):
            return self.getToken(lde_parser.LPAREN, 0)

        def tipoGrafico(self):
            return self.getTypedRuleContext(lde_parser.TipoGraficoContext,0)


        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(lde_parser.COMA)
            else:
                return self.getToken(lde_parser.COMA, i)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(lde_parser.ExpresionContext,i)


        def RPAREN(self):
            return self.getToken(lde_parser.RPAREN, 0)

        def getRuleIndex(self):
            return lde_parser.RULE_graficarStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGraficarStmt" ):
                listener.enterGraficarStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGraficarStmt" ):
                listener.exitGraficarStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitGraficarStmt" ):
                return visitor.visitGraficarStmt(self)
            else:
                return visitor.visitChildren(self)




    def graficarStmt(self):

        localctx = lde_parser.GraficarStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_graficarStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 110
            self.match(lde_parser.GRAFICAR)
            self.state = 111
            self.match(lde_parser.LPAREN)
            self.state = 112
            self.tipoGrafico()
            self.state = 113
            self.match(lde_parser.COMA)
            self.state = 114
            self.expresion()
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==58:
                self.state = 115
                self.match(lde_parser.COMA)
                self.state = 116
                self.expresion()


            self.state = 119
            self.match(lde_parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class TipoGraficoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BARRASPLOT(self):
            return self.getToken(lde_parser.BARRASPLOT, 0)

        def HISTOGRAMA(self):
            return self.getToken(lde_parser.HISTOGRAMA, 0)

        def SCATTERPLOT(self):
            return self.getToken(lde_parser.SCATTERPLOT, 0)

        def SCATTERDENS(self):
            return self.getToken(lde_parser.SCATTERDENS, 0)

        def LINEASPLOT(self):
            return self.getToken(lde_parser.LINEASPLOT, 0)

        def HEATMAP(self):
            return self.getToken(lde_parser.HEATMAP, 0)

        def getRuleIndex(self):
            return lde_parser.RULE_tipoGrafico

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTipoGrafico" ):
                listener.enterTipoGrafico(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTipoGrafico" ):
                listener.exitTipoGrafico(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoGrafico" ):
                return visitor.visitTipoGrafico(self)
            else:
                return visitor.visitChildren(self)




    def tipoGrafico(self):

        localctx = lde_parser.TipoGraficoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tipoGrafico)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 121
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 258048) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExtraerStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXTRAER(self):
            return self.getToken(lde_parser.EXTRAER, 0)

        def LPAREN(self):
            return self.getToken(lde_parser.LPAREN, 0)

        def ARCHIVO(self):
            return self.getToken(lde_parser.ARCHIVO, 0)

        def RPAREN(self):
            return self.getToken(lde_parser.RPAREN, 0)

        def getRuleIndex(self):
            return lde_parser.RULE_extraerStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExtraerStmt" ):
                listener.enterExtraerStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExtraerStmt" ):
                listener.exitExtraerStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExtraerStmt" ):
                return visitor.visitExtraerStmt(self)
            else:
                return visitor.visitChildren(self)




    def extraerStmt(self):

        localctx = lde_parser.ExtraerStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_extraerStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.match(lde_parser.EXTRAER)
            self.state = 124
            self.match(lde_parser.LPAREN)
            self.state = 125
            self.match(lde_parser.ARCHIVO)
            self.state = 126
            self.match(lde_parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExportarStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXPORTAR(self):
            return self.getToken(lde_parser.EXPORTAR, 0)

        def LPAREN(self):
            return self.getToken(lde_parser.LPAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(lde_parser.ExpresionContext,0)


        def COMA(self):
            return self.getToken(lde_parser.COMA, 0)

        def ARCHIVO(self):
            return self.getToken(lde_parser.ARCHIVO, 0)

        def RPAREN(self):
            return self.getToken(lde_parser.RPAREN, 0)

        def getRuleIndex(self):
            return lde_parser.RULE_exportarStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExportarStmt" ):
                listener.enterExportarStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExportarStmt" ):
                listener.exitExportarStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExportarStmt" ):
                return visitor.visitExportarStmt(self)
            else:
                return visitor.visitChildren(self)




    def exportarStmt(self):

        localctx = lde_parser.ExportarStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_exportarStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 128
            self.match(lde_parser.EXPORTAR)
            self.state = 129
            self.match(lde_parser.LPAREN)
            self.state = 130
            self.expresion()
            self.state = 131
            self.match(lde_parser.COMA)
            self.state = 132
            self.match(lde_parser.ARCHIVO)
            self.state = 133
            self.match(lde_parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self):
            return self.getToken(lde_parser.IF, 0)

        def LPAREN(self):
            return self.getToken(lde_parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(lde_parser.RPAREN, 0)

        def bloque(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.BloqueContext)
            else:
                return self.getTypedRuleContext(lde_parser.BloqueContext,i)


        def relacional(self):
            return self.getTypedRuleContext(lde_parser.RelacionalContext,0)


        def logico(self):
            return self.getTypedRuleContext(lde_parser.LogicoContext,0)


        def ELSE(self):
            return self.getToken(lde_parser.ELSE, 0)

        def getRuleIndex(self):
            return lde_parser.RULE_ifStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfStmt" ):
                listener.enterIfStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfStmt" ):
                listener.exitIfStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfStmt" ):
                return visitor.visitIfStmt(self)
            else:
                return visitor.visitChildren(self)




    def ifStmt(self):

        localctx = lde_parser.IfStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_ifStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.match(lde_parser.IF)
            self.state = 136
            self.match(lde_parser.LPAREN)
            self.state = 139
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 137
                self.relacional()
                pass

            elif la_ == 2:
                self.state = 138
                self.logico()
                pass


            self.state = 141
            self.match(lde_parser.RPAREN)
            self.state = 142
            self.bloque()
            self.state = 145
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==41:
                self.state = 143
                self.match(lde_parser.ELSE)
                self.state = 144
                self.bloque()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ForStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FOR(self):
            return self.getToken(lde_parser.FOR, 0)

        def LPAREN(self):
            return self.getToken(lde_parser.LPAREN, 0)

        def COMA(self, i:int=None):
            if i is None:
                return self.getTokens(lde_parser.COMA)
            else:
                return self.getToken(lde_parser.COMA, i)

        def modificacion(self):
            return self.getTypedRuleContext(lde_parser.ModificacionContext,0)


        def RPAREN(self):
            return self.getToken(lde_parser.RPAREN, 0)

        def bloque(self):
            return self.getTypedRuleContext(lde_parser.BloqueContext,0)


        def declaracion(self):
            return self.getTypedRuleContext(lde_parser.DeclaracionContext,0)


        def ID(self):
            return self.getToken(lde_parser.ID, 0)

        def relacional(self):
            return self.getTypedRuleContext(lde_parser.RelacionalContext,0)


        def logico(self):
            return self.getTypedRuleContext(lde_parser.LogicoContext,0)


        def getRuleIndex(self):
            return lde_parser.RULE_forStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterForStmt" ):
                listener.enterForStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitForStmt" ):
                listener.exitForStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitForStmt" ):
                return visitor.visitForStmt(self)
            else:
                return visitor.visitChildren(self)




    def forStmt(self):

        localctx = lde_parser.ForStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_forStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 147
            self.match(lde_parser.FOR)
            self.state = 148
            self.match(lde_parser.LPAREN)
            self.state = 151
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 149
                self.declaracion()
                pass
            elif token in [60]:
                self.state = 150
                self.match(lde_parser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 153
            self.match(lde_parser.COMA)
            self.state = 156
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                self.state = 154
                self.relacional()
                pass

            elif la_ == 2:
                self.state = 155
                self.logico()
                pass


            self.state = 158
            self.match(lde_parser.COMA)
            self.state = 159
            self.modificacion()
            self.state = 160
            self.match(lde_parser.RPAREN)
            self.state = 161
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(lde_parser.WHILE, 0)

        def LPAREN(self):
            return self.getToken(lde_parser.LPAREN, 0)

        def RPAREN(self):
            return self.getToken(lde_parser.RPAREN, 0)

        def bloque(self):
            return self.getTypedRuleContext(lde_parser.BloqueContext,0)


        def TRUE(self):
            return self.getToken(lde_parser.TRUE, 0)

        def relacional(self):
            return self.getTypedRuleContext(lde_parser.RelacionalContext,0)


        def logico(self):
            return self.getTypedRuleContext(lde_parser.LogicoContext,0)


        def getRuleIndex(self):
            return lde_parser.RULE_whileStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileStmt" ):
                listener.enterWhileStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileStmt" ):
                listener.exitWhileStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileStmt" ):
                return visitor.visitWhileStmt(self)
            else:
                return visitor.visitChildren(self)




    def whileStmt(self):

        localctx = lde_parser.WhileStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_whileStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            self.match(lde_parser.WHILE)
            self.state = 164
            self.match(lde_parser.LPAREN)
            self.state = 168
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 165
                self.match(lde_parser.TRUE)
                pass

            elif la_ == 2:
                self.state = 166
                self.relacional()
                pass

            elif la_ == 3:
                self.state = 167
                self.logico()
                pass


            self.state = 170
            self.match(lde_parser.RPAREN)
            self.state = 171
            self.bloque()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def BREAK(self):
            return self.getToken(lde_parser.BREAK, 0)

        def getRuleIndex(self):
            return lde_parser.RULE_breakStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreakStmt" ):
                listener.enterBreakStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreakStmt" ):
                listener.exitBreakStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreakStmt" ):
                return visitor.visitBreakStmt(self)
            else:
                return visitor.visitChildren(self)




    def breakStmt(self):

        localctx = lde_parser.BreakStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_breakStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(lde_parser.BREAK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RegresionLinealStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REGRESION(self):
            return self.getToken(lde_parser.REGRESION, 0)

        def LPAREN(self):
            return self.getToken(lde_parser.LPAREN, 0)

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(lde_parser.ExpresionContext,i)


        def COMA(self):
            return self.getToken(lde_parser.COMA, 0)

        def RPAREN(self):
            return self.getToken(lde_parser.RPAREN, 0)

        def getRuleIndex(self):
            return lde_parser.RULE_regresionLinealStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRegresionLinealStmt" ):
                listener.enterRegresionLinealStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRegresionLinealStmt" ):
                listener.exitRegresionLinealStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRegresionLinealStmt" ):
                return visitor.visitRegresionLinealStmt(self)
            else:
                return visitor.visitChildren(self)




    def regresionLinealStmt(self):

        localctx = lde_parser.RegresionLinealStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_regresionLinealStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 175
            self.match(lde_parser.REGRESION)
            self.state = 176
            self.match(lde_parser.LPAREN)
            self.state = 177
            self.expresion()
            self.state = 178
            self.match(lde_parser.COMA)
            self.state = 179
            self.expresion()
            self.state = 180
            self.match(lde_parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BloqueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INBLOCK(self):
            return self.getToken(lde_parser.INBLOCK, 0)

        def ENBLOCK(self):
            return self.getToken(lde_parser.ENBLOCK, 0)

        def sizeStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.SizeStmtContext)
            else:
                return self.getTypedRuleContext(lde_parser.SizeStmtContext,i)


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


        def graficarStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.GraficarStmtContext)
            else:
                return self.getTypedRuleContext(lde_parser.GraficarStmtContext,i)


        def exportarStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.ExportarStmtContext)
            else:
                return self.getTypedRuleContext(lde_parser.ExportarStmtContext,i)


        def modificacion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.ModificacionContext)
            else:
                return self.getTypedRuleContext(lde_parser.ModificacionContext,i)


        def ifStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.IfStmtContext)
            else:
                return self.getTypedRuleContext(lde_parser.IfStmtContext,i)


        def forStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.ForStmtContext)
            else:
                return self.getTypedRuleContext(lde_parser.ForStmtContext,i)


        def whileStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.WhileStmtContext)
            else:
                return self.getTypedRuleContext(lde_parser.WhileStmtContext,i)


        def breakStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.BreakStmtContext)
            else:
                return self.getTypedRuleContext(lde_parser.BreakStmtContext,i)


        def regresionLinealStmt(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.RegresionLinealStmtContext)
            else:
                return self.getTypedRuleContext(lde_parser.RegresionLinealStmtContext,i)


        def relacional(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.RelacionalContext)
            else:
                return self.getTypedRuleContext(lde_parser.RelacionalContext,i)


        def logico(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.LogicoContext)
            else:
                return self.getTypedRuleContext(lde_parser.LogicoContext,i)


        def getRuleIndex(self):
            return lde_parser.RULE_bloque

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBloque" ):
                listener.enterBloque(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBloque" ):
                listener.exitBloque(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = lde_parser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(lde_parser.INBLOCK)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 8327170107705395374) != 0):
                self.state = 199
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                if la_ == 1:
                    self.state = 183
                    self.sizeStmt()
                    pass

                elif la_ == 2:
                    self.state = 184
                    self.declaracion()
                    pass

                elif la_ == 3:
                    self.state = 185
                    self.expresion()
                    pass

                elif la_ == 4:
                    self.state = 188
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
                    if la_ == 1:
                        self.state = 186
                        self.relacional()
                        pass

                    elif la_ == 2:
                        self.state = 187
                        self.logico()
                        pass


                    pass

                elif la_ == 5:
                    self.state = 190
                    self.writeStmt()
                    pass

                elif la_ == 6:
                    self.state = 191
                    self.graficarStmt()
                    pass

                elif la_ == 7:
                    self.state = 192
                    self.exportarStmt()
                    pass

                elif la_ == 8:
                    self.state = 193
                    self.modificacion()
                    pass

                elif la_ == 9:
                    self.state = 194
                    self.ifStmt()
                    pass

                elif la_ == 10:
                    self.state = 195
                    self.forStmt()
                    pass

                elif la_ == 11:
                    self.state = 196
                    self.whileStmt()
                    pass

                elif la_ == 12:
                    self.state = 197
                    self.breakStmt()
                    pass

                elif la_ == 13:
                    self.state = 198
                    self.regresionLinealStmt()
                    pass


                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 204
            self.match(lde_parser.ENBLOCK)
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
        self.enterRule(localctx, 30, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.factor()
            self.state = 211
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 15728640) != 0):
                self.state = 207
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 15728640) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 208
                self.factor()
                self.state = 213
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

        def acceso(self):
            return self.getTypedRuleContext(lde_parser.AccesoContext,0)


        def addStmt(self):
            return self.getTypedRuleContext(lde_parser.AddStmtContext,0)


        def delStmt(self):
            return self.getTypedRuleContext(lde_parser.DelStmtContext,0)


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


        def STRING(self):
            return self.getToken(lde_parser.STRING, 0)

        def TRUE(self):
            return self.getToken(lde_parser.TRUE, 0)

        def FALSE(self):
            return self.getToken(lde_parser.FALSE, 0)

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
        self.enterRule(localctx, 32, self.RULE_factor)
        try:
            self.state = 233
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 214
                self.match(lde_parser.NUMERO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 215
                self.match(lde_parser.ID)
                self.state = 219
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,18,self._ctx)
                if la_ == 1:
                    self.state = 216
                    self.acceso()

                elif la_ == 2:
                    self.state = 217
                    self.addStmt()

                elif la_ == 3:
                    self.state = 218
                    self.delStmt()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 221
                self.match(lde_parser.LPAREN)
                self.state = 222
                self.expresion()
                self.state = 223
                self.match(lde_parser.RPAREN)
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 225
                self.match(lde_parser.RESTA)
                self.state = 226
                self.factor()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 227
                self.trigonometrica()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 228
                self.lista()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 229
                self.matriz()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 230
                self.match(lde_parser.STRING)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 231
                self.match(lde_parser.TRUE)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 232
                self.match(lde_parser.FALSE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AccesoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def LBRACKET(self):
            return self.getToken(lde_parser.LBRACKET, 0)

        def RBRACKET(self):
            return self.getToken(lde_parser.RBRACKET, 0)

        def expresion(self):
            return self.getTypedRuleContext(lde_parser.ExpresionContext,0)


        def ROWS(self):
            return self.getToken(lde_parser.ROWS, 0)

        def COLUMNS(self):
            return self.getToken(lde_parser.COLUMNS, 0)

        def acceso(self):
            return self.getTypedRuleContext(lde_parser.AccesoContext,0)


        def getRuleIndex(self):
            return lde_parser.RULE_acceso

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAcceso" ):
                listener.enterAcceso(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAcceso" ):
                listener.exitAcceso(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAcceso" ):
                return visitor.visitAcceso(self)
            else:
                return visitor.visitChildren(self)




    def acceso(self):

        localctx = lde_parser.AccesoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_acceso)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 235
            self.match(lde_parser.LBRACKET)
            self.state = 239
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 42, 43, 60, 61, 62]:
                self.state = 236
                self.expresion()
                pass
            elif token in [9]:
                self.state = 237
                self.match(lde_parser.ROWS)
                pass
            elif token in [10]:
                self.state = 238
                self.match(lde_parser.COLUMNS)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 241
            self.match(lde_parser.RBRACKET)
            self.state = 243
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                self.state = 242
                self.acceso()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUNTO(self):
            return self.getToken(lde_parser.PUNTO, 0)

        def ADD(self):
            return self.getToken(lde_parser.ADD, 0)

        def LPAREN(self):
            return self.getToken(lde_parser.LPAREN, 0)

        def COMA(self):
            return self.getToken(lde_parser.COMA, 0)

        def expresion(self):
            return self.getTypedRuleContext(lde_parser.ExpresionContext,0)


        def RPAREN(self):
            return self.getToken(lde_parser.RPAREN, 0)

        def ROWS(self):
            return self.getToken(lde_parser.ROWS, 0)

        def COLUMNS(self):
            return self.getToken(lde_parser.COLUMNS, 0)

        def getRuleIndex(self):
            return lde_parser.RULE_addStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddStmt" ):
                listener.enterAddStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddStmt" ):
                listener.exitAddStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddStmt" ):
                return visitor.visitAddStmt(self)
            else:
                return visitor.visitChildren(self)




    def addStmt(self):

        localctx = lde_parser.AddStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_addStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 245
            self.match(lde_parser.PUNTO)
            self.state = 246
            self.match(lde_parser.ADD)
            self.state = 247
            self.match(lde_parser.LPAREN)
            self.state = 248
            _la = self._input.LA(1)
            if not(_la==9 or _la==10):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 249
            self.match(lde_parser.COMA)
            self.state = 250
            self.expresion()
            self.state = 251
            self.match(lde_parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class DelStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def PUNTO(self):
            return self.getToken(lde_parser.PUNTO, 0)

        def DEL(self):
            return self.getToken(lde_parser.DEL, 0)

        def LPAREN(self):
            return self.getToken(lde_parser.LPAREN, 0)

        def COMA(self):
            return self.getToken(lde_parser.COMA, 0)

        def expresion(self):
            return self.getTypedRuleContext(lde_parser.ExpresionContext,0)


        def RPAREN(self):
            return self.getToken(lde_parser.RPAREN, 0)

        def ROWS(self):
            return self.getToken(lde_parser.ROWS, 0)

        def COLUMNS(self):
            return self.getToken(lde_parser.COLUMNS, 0)

        def getRuleIndex(self):
            return lde_parser.RULE_delStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDelStmt" ):
                listener.enterDelStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDelStmt" ):
                listener.exitDelStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDelStmt" ):
                return visitor.visitDelStmt(self)
            else:
                return visitor.visitChildren(self)




    def delStmt(self):

        localctx = lde_parser.DelStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_delStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 253
            self.match(lde_parser.PUNTO)
            self.state = 254
            self.match(lde_parser.DEL)
            self.state = 255
            self.match(lde_parser.LPAREN)
            self.state = 256
            _la = self._input.LA(1)
            if not(_la==9 or _la==10):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 257
            self.match(lde_parser.COMA)
            self.state = 258
            self.expresion()
            self.state = 259
            self.match(lde_parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class SizeStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TAMANO(self):
            return self.getToken(lde_parser.TAMANO, 0)

        def LPAREN(self):
            return self.getToken(lde_parser.LPAREN, 0)

        def factor(self):
            return self.getTypedRuleContext(lde_parser.FactorContext,0)


        def RPAREN(self):
            return self.getToken(lde_parser.RPAREN, 0)

        def getRuleIndex(self):
            return lde_parser.RULE_sizeStmt

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSizeStmt" ):
                listener.enterSizeStmt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSizeStmt" ):
                listener.exitSizeStmt(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSizeStmt" ):
                return visitor.visitSizeStmt(self)
            else:
                return visitor.visitChildren(self)




    def sizeStmt(self):

        localctx = lde_parser.SizeStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_sizeStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 261
            self.match(lde_parser.TAMANO)
            self.state = 262
            self.match(lde_parser.LPAREN)
            self.state = 263
            self.factor()
            self.state = 264
            self.match(lde_parser.RPAREN)
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
        self.enterRule(localctx, 42, self.RULE_trigonometrica)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 266
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 17146314752) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 267
            self.match(lde_parser.LPAREN)
            self.state = 268
            self.expresion()
            self.state = 269
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
        self.enterRule(localctx, 44, self.RULE_lista)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 271
            self.match(lde_parser.LBRACKET)
            self.state = 280
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & 8070463829433647104) != 0):
                self.state = 272
                self.expresion()
                self.state = 277
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==58:
                    self.state = 273
                    self.match(lde_parser.COMA)
                    self.state = 274
                    self.expresion()
                    self.state = 279
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 282
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
        self.enterRule(localctx, 46, self.RULE_matriz)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 284
            self.match(lde_parser.LBRACKET)
            self.state = 293
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==36:
                self.state = 285
                self.lista()
                self.state = 290
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==58:
                    self.state = 286
                    self.match(lde_parser.COMA)
                    self.state = 287
                    self.lista()
                    self.state = 292
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 295
            self.match(lde_parser.RBRACKET)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RelacionalContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(lde_parser.ExpresionContext,i)


        def MAYOR(self):
            return self.getToken(lde_parser.MAYOR, 0)

        def MENOR(self):
            return self.getToken(lde_parser.MENOR, 0)

        def MAYOR_IGUAL(self):
            return self.getToken(lde_parser.MAYOR_IGUAL, 0)

        def MENOR_IGUAL(self):
            return self.getToken(lde_parser.MENOR_IGUAL, 0)

        def IGUALDAD(self):
            return self.getToken(lde_parser.IGUALDAD, 0)

        def DIFERENTE(self):
            return self.getToken(lde_parser.DIFERENTE, 0)

        def getRuleIndex(self):
            return lde_parser.RULE_relacional

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelacional" ):
                listener.enterRelacional(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelacional" ):
                listener.exitRelacional(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelacional" ):
                return visitor.visitRelacional(self)
            else:
                return visitor.visitChildren(self)




    def relacional(self):

        localctx = lde_parser.RelacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_relacional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 297
            self.expresion()
            self.state = 298
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 1108307720798208) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 299
            self.expresion()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LogicoContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expresion(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(lde_parser.ExpresionContext)
            else:
                return self.getTypedRuleContext(lde_parser.ExpresionContext,i)


        def AND(self):
            return self.getToken(lde_parser.AND, 0)

        def OR(self):
            return self.getToken(lde_parser.OR, 0)

        def NOT(self):
            return self.getToken(lde_parser.NOT, 0)

        def getRuleIndex(self):
            return lde_parser.RULE_logico

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLogico" ):
                listener.enterLogico(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLogico" ):
                listener.exitLogico(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogico" ):
                return visitor.visitLogico(self)
            else:
                return visitor.visitChildren(self)




    def logico(self):

        localctx = lde_parser.LogicoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_logico)
        self._la = 0 # Token type
        try:
            self.state = 307
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 36, 42, 43, 60, 61, 62]:
                self.enterOuterAlt(localctx, 1)
                self.state = 301
                self.expresion()
                self.state = 302
                _la = self._input.LA(1)
                if not(_la==50 or _la==51):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 303
                self.expresion()
                pass
            elif token in [52]:
                self.enterOuterAlt(localctx, 2)
                self.state = 305
                self.match(lde_parser.NOT)
                self.state = 306
                self.expresion()
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





