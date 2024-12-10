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
        4,1,70,377,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,2,22,7,22,2,23,7,23,2,24,7,24,2,25,7,25,2,26,7,26,
        2,27,7,27,2,28,7,28,2,29,7,29,2,30,7,30,1,0,1,0,1,0,1,0,1,0,3,0,
        68,8,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0,5,0,79,8,0,10,0,12,0,
        82,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,97,
        8,1,1,2,1,2,3,2,101,8,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,1,2,3,2,111,
        8,2,1,3,1,3,1,3,5,3,116,8,3,10,3,12,3,119,9,3,1,4,1,4,1,4,1,4,1,
        4,3,4,126,8,4,1,4,1,4,1,5,1,5,1,5,1,5,1,5,1,5,1,5,3,5,137,8,5,1,
        5,1,5,1,6,1,6,1,6,1,6,1,6,1,6,1,6,3,6,148,8,6,1,7,1,7,1,7,1,7,1,
        7,1,8,1,8,1,8,1,8,1,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,166,8,9,1,9,1,
        9,1,9,1,9,3,9,172,8,9,1,10,1,10,1,10,1,10,3,10,178,8,10,1,10,1,10,
        1,10,3,10,183,8,10,1,10,1,10,1,10,1,10,1,10,1,11,1,11,1,11,1,11,
        1,11,3,11,195,8,11,1,11,1,11,1,11,1,12,1,12,1,13,1,13,1,13,1,13,
        1,13,1,13,1,13,1,14,1,14,1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,15,
        1,15,1,15,1,15,1,15,1,15,1,15,1,15,1,16,1,16,1,16,1,16,1,16,1,16,
        1,16,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,17,1,18,1,18,1,18,
        1,18,1,18,1,18,1,18,1,19,1,19,1,19,1,19,1,19,1,19,3,19,255,8,19,
        1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,1,19,5,19,266,8,19,10,19,
        12,19,269,9,19,1,19,1,19,1,20,1,20,1,20,5,20,276,8,20,10,20,12,20,
        279,9,20,1,21,1,21,1,21,1,21,1,21,3,21,286,8,21,1,21,1,21,1,21,1,
        21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,1,21,3,21,301,8,21,1,
        22,1,22,1,22,1,22,3,22,307,8,22,1,22,1,22,3,22,311,8,22,1,23,1,23,
        1,23,1,23,1,23,1,23,1,23,1,23,1,24,1,24,1,24,1,24,1,24,1,24,1,24,
        1,24,1,25,1,25,1,25,1,25,1,25,1,26,1,26,1,26,1,26,1,26,1,27,1,27,
        1,27,1,27,5,27,343,8,27,10,27,12,27,346,9,27,3,27,348,8,27,1,27,
        1,27,1,28,1,28,1,28,1,28,5,28,356,8,28,10,28,12,28,359,9,28,3,28,
        361,8,28,1,28,1,28,1,29,1,29,1,29,1,29,1,30,1,30,1,30,1,30,1,30,
        1,30,3,30,375,8,30,1,30,0,0,31,0,2,4,6,8,10,12,14,16,18,20,22,24,
        26,28,30,32,34,36,38,40,42,44,46,48,50,52,54,56,58,60,0,7,1,0,25,
        26,1,0,15,18,1,0,27,30,1,0,8,9,1,0,32,40,1,0,51,56,1,0,57,58,425,
        0,80,1,0,0,0,2,85,1,0,0,0,4,98,1,0,0,0,6,112,1,0,0,0,8,120,1,0,0,
        0,10,129,1,0,0,0,12,147,1,0,0,0,14,149,1,0,0,0,16,154,1,0,0,0,18,
        161,1,0,0,0,20,173,1,0,0,0,22,189,1,0,0,0,24,199,1,0,0,0,26,201,
        1,0,0,0,28,208,1,0,0,0,30,210,1,0,0,0,32,225,1,0,0,0,34,232,1,0,
        0,0,36,241,1,0,0,0,38,248,1,0,0,0,40,272,1,0,0,0,42,300,1,0,0,0,
        44,302,1,0,0,0,46,312,1,0,0,0,48,320,1,0,0,0,50,328,1,0,0,0,52,333,
        1,0,0,0,54,338,1,0,0,0,56,351,1,0,0,0,58,364,1,0,0,0,60,374,1,0,
        0,0,62,79,3,50,25,0,63,79,3,2,1,0,64,79,3,6,3,0,65,68,3,58,29,0,
        66,68,3,60,30,0,67,65,1,0,0,0,67,66,1,0,0,0,68,79,1,0,0,0,69,79,
        3,8,4,0,70,79,3,10,5,0,71,79,3,16,8,0,72,79,3,4,2,0,73,79,3,18,9,
        0,74,79,3,20,10,0,75,79,3,22,11,0,76,79,3,24,12,0,77,79,3,26,13,
        0,78,62,1,0,0,0,78,63,1,0,0,0,78,64,1,0,0,0,78,67,1,0,0,0,78,69,
        1,0,0,0,78,70,1,0,0,0,78,71,1,0,0,0,78,72,1,0,0,0,78,73,1,0,0,0,
        78,74,1,0,0,0,78,75,1,0,0,0,78,76,1,0,0,0,78,77,1,0,0,0,79,82,1,
        0,0,0,80,78,1,0,0,0,80,81,1,0,0,0,81,83,1,0,0,0,82,80,1,0,0,0,83,
        84,5,0,0,1,84,1,1,0,0,0,85,86,5,1,0,0,86,87,5,67,0,0,87,96,5,31,
        0,0,88,97,3,6,3,0,89,97,3,14,7,0,90,97,3,26,13,0,91,97,3,28,14,0,
        92,97,3,30,15,0,93,97,3,32,16,0,94,97,3,36,18,0,95,97,3,34,17,0,
        96,88,1,0,0,0,96,89,1,0,0,0,96,90,1,0,0,0,96,91,1,0,0,0,96,92,1,
        0,0,0,96,93,1,0,0,0,96,94,1,0,0,0,96,95,1,0,0,0,97,3,1,0,0,0,98,
        100,5,67,0,0,99,101,3,44,22,0,100,99,1,0,0,0,100,101,1,0,0,0,101,
        102,1,0,0,0,102,110,5,31,0,0,103,111,3,6,3,0,104,111,3,14,7,0,105,
        111,3,26,13,0,106,111,3,28,14,0,107,111,3,30,15,0,108,111,3,32,16,
        0,109,111,3,36,18,0,110,103,1,0,0,0,110,104,1,0,0,0,110,105,1,0,
        0,0,110,106,1,0,0,0,110,107,1,0,0,0,110,108,1,0,0,0,110,109,1,0,
        0,0,111,5,1,0,0,0,112,117,3,40,20,0,113,114,7,0,0,0,114,116,3,40,
        20,0,115,113,1,0,0,0,116,119,1,0,0,0,117,115,1,0,0,0,117,118,1,0,
        0,0,118,7,1,0,0,0,119,117,1,0,0,0,120,121,5,2,0,0,121,125,5,41,0,
        0,122,126,3,6,3,0,123,126,3,58,29,0,124,126,3,60,30,0,125,122,1,
        0,0,0,125,123,1,0,0,0,125,124,1,0,0,0,126,127,1,0,0,0,127,128,5,
        42,0,0,128,9,1,0,0,0,129,130,5,3,0,0,130,131,5,41,0,0,131,132,3,
        12,6,0,132,133,5,65,0,0,133,136,3,6,3,0,134,135,5,65,0,0,135,137,
        3,6,3,0,136,134,1,0,0,0,136,137,1,0,0,0,137,138,1,0,0,0,138,139,
        5,42,0,0,139,11,1,0,0,0,140,148,5,19,0,0,141,148,5,20,0,0,142,148,
        5,21,0,0,143,148,5,22,0,0,144,148,5,23,0,0,145,148,5,24,0,0,146,
        148,3,6,3,0,147,140,1,0,0,0,147,141,1,0,0,0,147,142,1,0,0,0,147,
        143,1,0,0,0,147,144,1,0,0,0,147,145,1,0,0,0,147,146,1,0,0,0,148,
        13,1,0,0,0,149,150,5,4,0,0,150,151,5,41,0,0,151,152,5,6,0,0,152,
        153,5,42,0,0,153,15,1,0,0,0,154,155,5,5,0,0,155,156,5,41,0,0,156,
        157,3,6,3,0,157,158,5,65,0,0,158,159,5,6,0,0,159,160,5,42,0,0,160,
        17,1,0,0,0,161,162,5,47,0,0,162,165,5,41,0,0,163,166,3,58,29,0,164,
        166,3,60,30,0,165,163,1,0,0,0,165,164,1,0,0,0,166,167,1,0,0,0,167,
        168,5,42,0,0,168,171,3,38,19,0,169,170,5,48,0,0,170,172,3,38,19,
        0,171,169,1,0,0,0,171,172,1,0,0,0,172,19,1,0,0,0,173,174,5,62,0,
        0,174,177,5,41,0,0,175,178,3,2,1,0,176,178,5,67,0,0,177,175,1,0,
        0,0,177,176,1,0,0,0,178,179,1,0,0,0,179,182,5,65,0,0,180,183,3,58,
        29,0,181,183,3,60,30,0,182,180,1,0,0,0,182,181,1,0,0,0,183,184,1,
        0,0,0,184,185,5,65,0,0,185,186,3,4,2,0,186,187,5,42,0,0,187,188,
        3,38,19,0,188,21,1,0,0,0,189,190,5,63,0,0,190,194,5,41,0,0,191,195,
        5,49,0,0,192,195,3,58,29,0,193,195,3,60,30,0,194,191,1,0,0,0,194,
        192,1,0,0,0,194,193,1,0,0,0,195,196,1,0,0,0,196,197,5,42,0,0,197,
        198,3,38,19,0,198,23,1,0,0,0,199,200,5,64,0,0,200,25,1,0,0,0,201,
        202,5,7,0,0,202,203,5,41,0,0,203,204,3,6,3,0,204,205,5,65,0,0,205,
        206,3,6,3,0,206,207,5,42,0,0,207,27,1,0,0,0,208,209,7,1,0,0,209,
        29,1,0,0,0,210,211,5,11,0,0,211,212,5,41,0,0,212,213,3,6,3,0,213,
        214,5,65,0,0,214,215,3,6,3,0,215,216,5,65,0,0,216,217,3,6,3,0,217,
        218,5,65,0,0,218,219,3,28,14,0,219,220,5,65,0,0,220,221,3,6,3,0,
        221,222,5,65,0,0,222,223,3,6,3,0,223,224,5,42,0,0,224,31,1,0,0,0,
        225,226,5,67,0,0,226,227,5,66,0,0,227,228,5,13,0,0,228,229,5,41,
        0,0,229,230,3,6,3,0,230,231,5,42,0,0,231,33,1,0,0,0,232,233,5,67,
        0,0,233,234,5,66,0,0,234,235,5,12,0,0,235,236,5,41,0,0,236,237,3,
        6,3,0,237,238,5,65,0,0,238,239,3,6,3,0,239,240,5,42,0,0,240,35,1,
        0,0,0,241,242,5,14,0,0,242,243,5,41,0,0,243,244,3,6,3,0,244,245,
        5,65,0,0,245,246,3,6,3,0,246,247,5,42,0,0,247,37,1,0,0,0,248,267,
        5,60,0,0,249,266,3,50,25,0,250,266,3,2,1,0,251,266,3,6,3,0,252,255,
        3,58,29,0,253,255,3,60,30,0,254,252,1,0,0,0,254,253,1,0,0,0,255,
        266,1,0,0,0,256,266,3,8,4,0,257,266,3,10,5,0,258,266,3,16,8,0,259,
        266,3,4,2,0,260,266,3,18,9,0,261,266,3,20,10,0,262,266,3,22,11,0,
        263,266,3,24,12,0,264,266,3,26,13,0,265,249,1,0,0,0,265,250,1,0,
        0,0,265,251,1,0,0,0,265,254,1,0,0,0,265,256,1,0,0,0,265,257,1,0,
        0,0,265,258,1,0,0,0,265,259,1,0,0,0,265,260,1,0,0,0,265,261,1,0,
        0,0,265,262,1,0,0,0,265,263,1,0,0,0,265,264,1,0,0,0,266,269,1,0,
        0,0,267,265,1,0,0,0,267,268,1,0,0,0,268,270,1,0,0,0,269,267,1,0,
        0,0,270,271,5,61,0,0,271,39,1,0,0,0,272,277,3,42,21,0,273,274,7,
        2,0,0,274,276,3,42,21,0,275,273,1,0,0,0,276,279,1,0,0,0,277,275,
        1,0,0,0,277,278,1,0,0,0,278,41,1,0,0,0,279,277,1,0,0,0,280,301,5,
        68,0,0,281,285,5,67,0,0,282,286,3,44,22,0,283,286,3,46,23,0,284,
        286,3,48,24,0,285,282,1,0,0,0,285,283,1,0,0,0,285,284,1,0,0,0,285,
        286,1,0,0,0,286,301,1,0,0,0,287,301,3,50,25,0,288,289,5,41,0,0,289,
        290,3,6,3,0,290,291,5,42,0,0,291,301,1,0,0,0,292,293,5,26,0,0,293,
        301,3,42,21,0,294,301,3,52,26,0,295,301,3,54,27,0,296,301,3,56,28,
        0,297,301,5,69,0,0,298,301,5,49,0,0,299,301,5,50,0,0,300,280,1,0,
        0,0,300,281,1,0,0,0,300,287,1,0,0,0,300,288,1,0,0,0,300,292,1,0,
        0,0,300,294,1,0,0,0,300,295,1,0,0,0,300,296,1,0,0,0,300,297,1,0,
        0,0,300,298,1,0,0,0,300,299,1,0,0,0,301,43,1,0,0,0,302,306,5,43,
        0,0,303,307,3,6,3,0,304,307,5,8,0,0,305,307,5,9,0,0,306,303,1,0,
        0,0,306,304,1,0,0,0,306,305,1,0,0,0,307,308,1,0,0,0,308,310,5,44,
        0,0,309,311,3,44,22,0,310,309,1,0,0,0,310,311,1,0,0,0,311,45,1,0,
        0,0,312,313,5,66,0,0,313,314,5,45,0,0,314,315,5,41,0,0,315,316,7,
        3,0,0,316,317,5,65,0,0,317,318,3,6,3,0,318,319,5,42,0,0,319,47,1,
        0,0,0,320,321,5,66,0,0,321,322,5,46,0,0,322,323,5,41,0,0,323,324,
        7,3,0,0,324,325,5,65,0,0,325,326,3,6,3,0,326,327,5,42,0,0,327,49,
        1,0,0,0,328,329,5,10,0,0,329,330,5,41,0,0,330,331,3,42,21,0,331,
        332,5,42,0,0,332,51,1,0,0,0,333,334,7,4,0,0,334,335,5,41,0,0,335,
        336,3,6,3,0,336,337,5,42,0,0,337,53,1,0,0,0,338,347,5,43,0,0,339,
        344,3,6,3,0,340,341,5,65,0,0,341,343,3,6,3,0,342,340,1,0,0,0,343,
        346,1,0,0,0,344,342,1,0,0,0,344,345,1,0,0,0,345,348,1,0,0,0,346,
        344,1,0,0,0,347,339,1,0,0,0,347,348,1,0,0,0,348,349,1,0,0,0,349,
        350,5,44,0,0,350,55,1,0,0,0,351,360,5,43,0,0,352,357,3,54,27,0,353,
        354,5,65,0,0,354,356,3,54,27,0,355,353,1,0,0,0,356,359,1,0,0,0,357,
        355,1,0,0,0,357,358,1,0,0,0,358,361,1,0,0,0,359,357,1,0,0,0,360,
        352,1,0,0,0,360,361,1,0,0,0,361,362,1,0,0,0,362,363,5,44,0,0,363,
        57,1,0,0,0,364,365,3,6,3,0,365,366,7,5,0,0,366,367,3,6,3,0,367,59,
        1,0,0,0,368,369,3,6,3,0,369,370,7,6,0,0,370,371,3,6,3,0,371,375,
        1,0,0,0,372,373,5,59,0,0,373,375,3,6,3,0,374,368,1,0,0,0,374,372,
        1,0,0,0,375,61,1,0,0,0,28,67,78,80,96,100,110,117,125,136,147,165,
        171,177,182,194,254,265,267,277,285,300,306,310,344,347,357,360,
        374
    ]

class lde_parser ( Parser ):

    grammarFileName = "lde_parser.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'var'", "'write'", "'plot'", "'extract'", 
                     "'export'", "<INVALID>", "'regression'", "'R'", "'C'", 
                     "'size'", "'classifier'", "'evaluate'", "'predict'", 
                     "'cluster'", "'sigmoid'", "'relu'", "'tanh_act'", "'softmax'", 
                     "'bar_plot'", "'histogram'", "'scatter_plot'", "'scatter_density'", 
                     "'line_plot'", "'heatmap'", "'+'", "'-'", "'*'", "'/'", 
                     "'%'", "'^'", "'='", "'sin'", "'cos'", "'tan'", "'asin'", 
                     "'acos'", "'atan'", "'sinh'", "'cosh'", "'tanh'", "'('", 
                     "')'", "'['", "']'", "'add'", "'del'", "'if'", "'else'", 
                     "'true'", "'false'", "'>'", "'<'", "'>='", "'<='", 
                     "'=='", "'!='", "'and'", "'or'", "'not'", "'{'", "'}'", 
                     "'for'", "'while'", "'break'", "','", "'.'" ]

    symbolicNames = [ "<INVALID>", "VAR", "WRITE", "GRAFICAR", "EXTRAER", 
                      "EXPORTAR", "ARCHIVO", "REGRESION", "ROWS", "COLUMNS", 
                      "TAMANO", "CLASIFICADOR", "EVALUAR", "PREDECIR", "AGRUPAR", 
                      "SIGMOID", "RELU", "TAHACT", "SOFTMAX", "BARRASPLOT", 
                      "HISTOGRAMA", "SCATTERPLOT", "SCATTERDENS", "LINEASPLOT", 
                      "HEATMAP", "SUMA", "RESTA", "MULT", "DIV", "MOD", 
                      "EXP", "IGUAL", "SIN", "COS", "TAN", "ASIN", "ACOS", 
                      "ATAN", "SINH", "COSH", "TANH", "LPAREN", "RPAREN", 
                      "LBRACKET", "RBRACKET", "ADD", "DEL", "IF", "ELSE", 
                      "TRUE", "FALSE", "MAYOR", "MENOR", "MAYOR_IGUAL", 
                      "MENOR_IGUAL", "IGUALDAD", "DIFERENTE", "AND", "OR", 
                      "NOT", "INBLOCK", "ENBLOCK", "FOR", "WHILE", "BREAK", 
                      "COMA", "PUNTO", "ID", "NUMERO", "STRING", "ESPACIO" ]

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
    RULE_funcionAct = 14
    RULE_classificadorStmt = 15
    RULE_predecirStmt = 16
    RULE_evaluarStmt = 17
    RULE_agruparStmt = 18
    RULE_bloque = 19
    RULE_termino = 20
    RULE_factor = 21
    RULE_acceso = 22
    RULE_addStmt = 23
    RULE_delStmt = 24
    RULE_sizeStmt = 25
    RULE_trigonometrica = 26
    RULE_lista = 27
    RULE_matriz = 28
    RULE_relacional = 29
    RULE_logico = 30

    ruleNames =  [ "programa", "declaracion", "modificacion", "expresion", 
                   "writeStmt", "graficarStmt", "tipoGrafico", "extraerStmt", 
                   "exportarStmt", "ifStmt", "forStmt", "whileStmt", "breakStmt", 
                   "regresionLinealStmt", "funcionAct", "classificadorStmt", 
                   "predecirStmt", "evaluarStmt", "agruparStmt", "bloque", 
                   "termino", "factor", "acceso", "addStmt", "delStmt", 
                   "sizeStmt", "trigonometrica", "lista", "matriz", "relacional", 
                   "logico" ]

    EOF = Token.EOF
    VAR=1
    WRITE=2
    GRAFICAR=3
    EXTRAER=4
    EXPORTAR=5
    ARCHIVO=6
    REGRESION=7
    ROWS=8
    COLUMNS=9
    TAMANO=10
    CLASIFICADOR=11
    EVALUAR=12
    PREDECIR=13
    AGRUPAR=14
    SIGMOID=15
    RELU=16
    TAHACT=17
    SOFTMAX=18
    BARRASPLOT=19
    HISTOGRAMA=20
    SCATTERPLOT=21
    SCATTERDENS=22
    LINEASPLOT=23
    HEATMAP=24
    SUMA=25
    RESTA=26
    MULT=27
    DIV=28
    MOD=29
    EXP=30
    IGUAL=31
    SIN=32
    COS=33
    TAN=34
    ASIN=35
    ACOS=36
    ATAN=37
    SINH=38
    COSH=39
    TANH=40
    LPAREN=41
    RPAREN=42
    LBRACKET=43
    RBRACKET=44
    ADD=45
    DEL=46
    IF=47
    ELSE=48
    TRUE=49
    FALSE=50
    MAYOR=51
    MENOR=52
    MAYOR_IGUAL=53
    MENOR_IGUAL=54
    IGUALDAD=55
    DIFERENTE=56
    AND=57
    OR=58
    NOT=59
    INBLOCK=60
    ENBLOCK=61
    FOR=62
    WHILE=63
    BREAK=64
    COMA=65
    PUNTO=66
    ID=67
    NUMERO=68
    STRING=69
    ESPACIO=70

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
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4033382488863669074) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 57) != 0):
                self.state = 78
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
                if la_ == 1:
                    self.state = 62
                    self.sizeStmt()
                    pass

                elif la_ == 2:
                    self.state = 63
                    self.declaracion()
                    pass

                elif la_ == 3:
                    self.state = 64
                    self.expresion()
                    pass

                elif la_ == 4:
                    self.state = 67
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,0,self._ctx)
                    if la_ == 1:
                        self.state = 65
                        self.relacional()
                        pass

                    elif la_ == 2:
                        self.state = 66
                        self.logico()
                        pass


                    pass

                elif la_ == 5:
                    self.state = 69
                    self.writeStmt()
                    pass

                elif la_ == 6:
                    self.state = 70
                    self.graficarStmt()
                    pass

                elif la_ == 7:
                    self.state = 71
                    self.exportarStmt()
                    pass

                elif la_ == 8:
                    self.state = 72
                    self.modificacion()
                    pass

                elif la_ == 9:
                    self.state = 73
                    self.ifStmt()
                    pass

                elif la_ == 10:
                    self.state = 74
                    self.forStmt()
                    pass

                elif la_ == 11:
                    self.state = 75
                    self.whileStmt()
                    pass

                elif la_ == 12:
                    self.state = 76
                    self.breakStmt()
                    pass

                elif la_ == 13:
                    self.state = 77
                    self.regresionLinealStmt()
                    pass


                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 83
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


        def funcionAct(self):
            return self.getTypedRuleContext(lde_parser.FuncionActContext,0)


        def classificadorStmt(self):
            return self.getTypedRuleContext(lde_parser.ClassificadorStmtContext,0)


        def predecirStmt(self):
            return self.getTypedRuleContext(lde_parser.PredecirStmtContext,0)


        def agruparStmt(self):
            return self.getTypedRuleContext(lde_parser.AgruparStmtContext,0)


        def evaluarStmt(self):
            return self.getTypedRuleContext(lde_parser.EvaluarStmtContext,0)


        def getRuleIndex(self):
            return lde_parser.RULE_declaracion

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
            self.state = 85
            self.match(lde_parser.VAR)
            self.state = 86
            self.match(lde_parser.ID)
            self.state = 87
            self.match(lde_parser.IGUAL)
            self.state = 96
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                self.state = 88
                self.expresion()
                pass

            elif la_ == 2:
                self.state = 89
                self.extraerStmt()
                pass

            elif la_ == 3:
                self.state = 90
                self.regresionLinealStmt()
                pass

            elif la_ == 4:
                self.state = 91
                self.funcionAct()
                pass

            elif la_ == 5:
                self.state = 92
                self.classificadorStmt()
                pass

            elif la_ == 6:
                self.state = 93
                self.predecirStmt()
                pass

            elif la_ == 7:
                self.state = 94
                self.agruparStmt()
                pass

            elif la_ == 8:
                self.state = 95
                self.evaluarStmt()
                pass


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


        def funcionAct(self):
            return self.getTypedRuleContext(lde_parser.FuncionActContext,0)


        def classificadorStmt(self):
            return self.getTypedRuleContext(lde_parser.ClassificadorStmtContext,0)


        def predecirStmt(self):
            return self.getTypedRuleContext(lde_parser.PredecirStmtContext,0)


        def agruparStmt(self):
            return self.getTypedRuleContext(lde_parser.AgruparStmtContext,0)


        def acceso(self):
            return self.getTypedRuleContext(lde_parser.AccesoContext,0)


        def getRuleIndex(self):
            return lde_parser.RULE_modificacion

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
            self.state = 98
            self.match(lde_parser.ID)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 99
                self.acceso()


            self.state = 102
            self.match(lde_parser.IGUAL)
            self.state = 110
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 103
                self.expresion()
                pass

            elif la_ == 2:
                self.state = 104
                self.extraerStmt()
                pass

            elif la_ == 3:
                self.state = 105
                self.regresionLinealStmt()
                pass

            elif la_ == 4:
                self.state = 106
                self.funcionAct()
                pass

            elif la_ == 5:
                self.state = 107
                self.classificadorStmt()
                pass

            elif la_ == 6:
                self.state = 108
                self.predecirStmt()
                pass

            elif la_ == 7:
                self.state = 109
                self.agruparStmt()
                pass


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
            self.state = 112
            self.termino()
            self.state = 117
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,6,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 113
                    _la = self._input.LA(1)
                    if not(_la==25 or _la==26):
                        self._errHandler.recoverInline(self)
                    else:
                        self._errHandler.reportMatch(self)
                        self.consume()
                    self.state = 114
                    self.termino() 
                self.state = 119
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
            self.state = 120
            self.match(lde_parser.WRITE)
            self.state = 121
            self.match(lde_parser.LPAREN)
            self.state = 125
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                self.state = 122
                self.expresion()
                pass

            elif la_ == 2:
                self.state = 123
                self.relacional()
                pass

            elif la_ == 3:
                self.state = 124
                self.logico()
                pass


            self.state = 127
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
            self.state = 129
            self.match(lde_parser.GRAFICAR)
            self.state = 130
            self.match(lde_parser.LPAREN)
            self.state = 131
            self.tipoGrafico()
            self.state = 132
            self.match(lde_parser.COMA)
            self.state = 133
            self.expresion()
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==65:
                self.state = 134
                self.match(lde_parser.COMA)
                self.state = 135
                self.expresion()


            self.state = 138
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

        def expresion(self):
            return self.getTypedRuleContext(lde_parser.ExpresionContext,0)


        def getRuleIndex(self):
            return lde_parser.RULE_tipoGrafico

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTipoGrafico" ):
                return visitor.visitTipoGrafico(self)
            else:
                return visitor.visitChildren(self)




    def tipoGrafico(self):

        localctx = lde_parser.TipoGraficoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_tipoGrafico)
        try:
            self.state = 147
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [19]:
                self.enterOuterAlt(localctx, 1)
                self.state = 140
                self.match(lde_parser.BARRASPLOT)
                pass
            elif token in [20]:
                self.enterOuterAlt(localctx, 2)
                self.state = 141
                self.match(lde_parser.HISTOGRAMA)
                pass
            elif token in [21]:
                self.enterOuterAlt(localctx, 3)
                self.state = 142
                self.match(lde_parser.SCATTERPLOT)
                pass
            elif token in [22]:
                self.enterOuterAlt(localctx, 4)
                self.state = 143
                self.match(lde_parser.SCATTERDENS)
                pass
            elif token in [23]:
                self.enterOuterAlt(localctx, 5)
                self.state = 144
                self.match(lde_parser.LINEASPLOT)
                pass
            elif token in [24]:
                self.enterOuterAlt(localctx, 6)
                self.state = 145
                self.match(lde_parser.HEATMAP)
                pass
            elif token in [10, 26, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 49, 50, 67, 68, 69]:
                self.enterOuterAlt(localctx, 7)
                self.state = 146
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
            self.state = 149
            self.match(lde_parser.EXTRAER)
            self.state = 150
            self.match(lde_parser.LPAREN)
            self.state = 151
            self.match(lde_parser.ARCHIVO)
            self.state = 152
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
            self.state = 154
            self.match(lde_parser.EXPORTAR)
            self.state = 155
            self.match(lde_parser.LPAREN)
            self.state = 156
            self.expresion()
            self.state = 157
            self.match(lde_parser.COMA)
            self.state = 158
            self.match(lde_parser.ARCHIVO)
            self.state = 159
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
            self.state = 161
            self.match(lde_parser.IF)
            self.state = 162
            self.match(lde_parser.LPAREN)
            self.state = 165
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                self.state = 163
                self.relacional()
                pass

            elif la_ == 2:
                self.state = 164
                self.logico()
                pass


            self.state = 167
            self.match(lde_parser.RPAREN)
            self.state = 168
            self.bloque()
            self.state = 171
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==48:
                self.state = 169
                self.match(lde_parser.ELSE)
                self.state = 170
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
            self.state = 173
            self.match(lde_parser.FOR)
            self.state = 174
            self.match(lde_parser.LPAREN)
            self.state = 177
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [1]:
                self.state = 175
                self.declaracion()
                pass
            elif token in [67]:
                self.state = 176
                self.match(lde_parser.ID)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 179
            self.match(lde_parser.COMA)
            self.state = 182
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 180
                self.relacional()
                pass

            elif la_ == 2:
                self.state = 181
                self.logico()
                pass


            self.state = 184
            self.match(lde_parser.COMA)
            self.state = 185
            self.modificacion()
            self.state = 186
            self.match(lde_parser.RPAREN)
            self.state = 187
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
            self.state = 189
            self.match(lde_parser.WHILE)
            self.state = 190
            self.match(lde_parser.LPAREN)
            self.state = 194
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,14,self._ctx)
            if la_ == 1:
                self.state = 191
                self.match(lde_parser.TRUE)
                pass

            elif la_ == 2:
                self.state = 192
                self.relacional()
                pass

            elif la_ == 3:
                self.state = 193
                self.logico()
                pass


            self.state = 196
            self.match(lde_parser.RPAREN)
            self.state = 197
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
            self.state = 199
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
            self.state = 201
            self.match(lde_parser.REGRESION)
            self.state = 202
            self.match(lde_parser.LPAREN)
            self.state = 203
            self.expresion()
            self.state = 204
            self.match(lde_parser.COMA)
            self.state = 205
            self.expresion()
            self.state = 206
            self.match(lde_parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FuncionActContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def SIGMOID(self):
            return self.getToken(lde_parser.SIGMOID, 0)

        def RELU(self):
            return self.getToken(lde_parser.RELU, 0)

        def TAHACT(self):
            return self.getToken(lde_parser.TAHACT, 0)

        def SOFTMAX(self):
            return self.getToken(lde_parser.SOFTMAX, 0)

        def getRuleIndex(self):
            return lde_parser.RULE_funcionAct

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFuncionAct" ):
                return visitor.visitFuncionAct(self)
            else:
                return visitor.visitChildren(self)




    def funcionAct(self):

        localctx = lde_parser.FuncionActContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_funcionAct)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 491520) != 0)):
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


    class ClassificadorStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def CLASIFICADOR(self):
            return self.getToken(lde_parser.CLASIFICADOR, 0)

        def LPAREN(self):
            return self.getToken(lde_parser.LPAREN, 0)

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

        def funcionAct(self):
            return self.getTypedRuleContext(lde_parser.FuncionActContext,0)


        def RPAREN(self):
            return self.getToken(lde_parser.RPAREN, 0)

        def getRuleIndex(self):
            return lde_parser.RULE_classificadorStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitClassificadorStmt" ):
                return visitor.visitClassificadorStmt(self)
            else:
                return visitor.visitChildren(self)




    def classificadorStmt(self):

        localctx = lde_parser.ClassificadorStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_classificadorStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 210
            self.match(lde_parser.CLASIFICADOR)
            self.state = 211
            self.match(lde_parser.LPAREN)
            self.state = 212
            self.expresion()
            self.state = 213
            self.match(lde_parser.COMA)
            self.state = 214
            self.expresion()
            self.state = 215
            self.match(lde_parser.COMA)
            self.state = 216
            self.expresion()
            self.state = 217
            self.match(lde_parser.COMA)
            self.state = 218
            self.funcionAct()
            self.state = 219
            self.match(lde_parser.COMA)
            self.state = 220
            self.expresion()
            self.state = 221
            self.match(lde_parser.COMA)
            self.state = 222
            self.expresion()
            self.state = 223
            self.match(lde_parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class PredecirStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(lde_parser.ID, 0)

        def PUNTO(self):
            return self.getToken(lde_parser.PUNTO, 0)

        def PREDECIR(self):
            return self.getToken(lde_parser.PREDECIR, 0)

        def LPAREN(self):
            return self.getToken(lde_parser.LPAREN, 0)

        def expresion(self):
            return self.getTypedRuleContext(lde_parser.ExpresionContext,0)


        def RPAREN(self):
            return self.getToken(lde_parser.RPAREN, 0)

        def getRuleIndex(self):
            return lde_parser.RULE_predecirStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitPredecirStmt" ):
                return visitor.visitPredecirStmt(self)
            else:
                return visitor.visitChildren(self)




    def predecirStmt(self):

        localctx = lde_parser.PredecirStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_predecirStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 225
            self.match(lde_parser.ID)
            self.state = 226
            self.match(lde_parser.PUNTO)
            self.state = 227
            self.match(lde_parser.PREDECIR)
            self.state = 228
            self.match(lde_parser.LPAREN)
            self.state = 229
            self.expresion()
            self.state = 230
            self.match(lde_parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class EvaluarStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(lde_parser.ID, 0)

        def PUNTO(self):
            return self.getToken(lde_parser.PUNTO, 0)

        def EVALUAR(self):
            return self.getToken(lde_parser.EVALUAR, 0)

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
            return lde_parser.RULE_evaluarStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitEvaluarStmt" ):
                return visitor.visitEvaluarStmt(self)
            else:
                return visitor.visitChildren(self)




    def evaluarStmt(self):

        localctx = lde_parser.EvaluarStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_evaluarStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 232
            self.match(lde_parser.ID)
            self.state = 233
            self.match(lde_parser.PUNTO)
            self.state = 234
            self.match(lde_parser.EVALUAR)
            self.state = 235
            self.match(lde_parser.LPAREN)
            self.state = 236
            self.expresion()
            self.state = 237
            self.match(lde_parser.COMA)
            self.state = 238
            self.expresion()
            self.state = 239
            self.match(lde_parser.RPAREN)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AgruparStmtContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def AGRUPAR(self):
            return self.getToken(lde_parser.AGRUPAR, 0)

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
            return lde_parser.RULE_agruparStmt

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAgruparStmt" ):
                return visitor.visitAgruparStmt(self)
            else:
                return visitor.visitChildren(self)




    def agruparStmt(self):

        localctx = lde_parser.AgruparStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_agruparStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 241
            self.match(lde_parser.AGRUPAR)
            self.state = 242
            self.match(lde_parser.LPAREN)
            self.state = 243
            self.expresion()
            self.state = 244
            self.match(lde_parser.COMA)
            self.state = 245
            self.expresion()
            self.state = 246
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBloque" ):
                return visitor.visitBloque(self)
            else:
                return visitor.visitChildren(self)




    def bloque(self):

        localctx = lde_parser.BloqueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_bloque)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 248
            self.match(lde_parser.INBLOCK)
            self.state = 267
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & -4033382488863669074) != 0) or ((((_la - 64)) & ~0x3f) == 0 and ((1 << (_la - 64)) & 57) != 0):
                self.state = 265
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
                if la_ == 1:
                    self.state = 249
                    self.sizeStmt()
                    pass

                elif la_ == 2:
                    self.state = 250
                    self.declaracion()
                    pass

                elif la_ == 3:
                    self.state = 251
                    self.expresion()
                    pass

                elif la_ == 4:
                    self.state = 254
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,15,self._ctx)
                    if la_ == 1:
                        self.state = 252
                        self.relacional()
                        pass

                    elif la_ == 2:
                        self.state = 253
                        self.logico()
                        pass


                    pass

                elif la_ == 5:
                    self.state = 256
                    self.writeStmt()
                    pass

                elif la_ == 6:
                    self.state = 257
                    self.graficarStmt()
                    pass

                elif la_ == 7:
                    self.state = 258
                    self.exportarStmt()
                    pass

                elif la_ == 8:
                    self.state = 259
                    self.modificacion()
                    pass

                elif la_ == 9:
                    self.state = 260
                    self.ifStmt()
                    pass

                elif la_ == 10:
                    self.state = 261
                    self.forStmt()
                    pass

                elif la_ == 11:
                    self.state = 262
                    self.whileStmt()
                    pass

                elif la_ == 12:
                    self.state = 263
                    self.breakStmt()
                    pass

                elif la_ == 13:
                    self.state = 264
                    self.regresionLinealStmt()
                    pass


                self.state = 269
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 270
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTermino" ):
                return visitor.visitTermino(self)
            else:
                return visitor.visitChildren(self)




    def termino(self):

        localctx = lde_parser.TerminoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_termino)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 272
            self.factor()
            self.state = 277
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & 2013265920) != 0):
                self.state = 273
                _la = self._input.LA(1)
                if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2013265920) != 0)):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 274
                self.factor()
                self.state = 279
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


        def sizeStmt(self):
            return self.getTypedRuleContext(lde_parser.SizeStmtContext,0)


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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFactor" ):
                return visitor.visitFactor(self)
            else:
                return visitor.visitChildren(self)




    def factor(self):

        localctx = lde_parser.FactorContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_factor)
        try:
            self.state = 300
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,20,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 280
                self.match(lde_parser.NUMERO)
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 281
                self.match(lde_parser.ID)
                self.state = 285
                self._errHandler.sync(self)
                la_ = self._interp.adaptivePredict(self._input,19,self._ctx)
                if la_ == 1:
                    self.state = 282
                    self.acceso()

                elif la_ == 2:
                    self.state = 283
                    self.addStmt()

                elif la_ == 3:
                    self.state = 284
                    self.delStmt()


                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 287
                self.sizeStmt()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 288
                self.match(lde_parser.LPAREN)
                self.state = 289
                self.expresion()
                self.state = 290
                self.match(lde_parser.RPAREN)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 292
                self.match(lde_parser.RESTA)
                self.state = 293
                self.factor()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 294
                self.trigonometrica()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 295
                self.lista()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 296
                self.matriz()
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 297
                self.match(lde_parser.STRING)
                pass

            elif la_ == 10:
                self.enterOuterAlt(localctx, 10)
                self.state = 298
                self.match(lde_parser.TRUE)
                pass

            elif la_ == 11:
                self.enterOuterAlt(localctx, 11)
                self.state = 299
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAcceso" ):
                return visitor.visitAcceso(self)
            else:
                return visitor.visitChildren(self)




    def acceso(self):

        localctx = lde_parser.AccesoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 44, self.RULE_acceso)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 302
            self.match(lde_parser.LBRACKET)
            self.state = 306
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 26, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 49, 50, 67, 68, 69]:
                self.state = 303
                self.expresion()
                pass
            elif token in [8]:
                self.state = 304
                self.match(lde_parser.ROWS)
                pass
            elif token in [9]:
                self.state = 305
                self.match(lde_parser.COLUMNS)
                pass
            else:
                raise NoViableAltException(self)

            self.state = 308
            self.match(lde_parser.RBRACKET)
            self.state = 310
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,22,self._ctx)
            if la_ == 1:
                self.state = 309
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddStmt" ):
                return visitor.visitAddStmt(self)
            else:
                return visitor.visitChildren(self)




    def addStmt(self):

        localctx = lde_parser.AddStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 46, self.RULE_addStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 312
            self.match(lde_parser.PUNTO)
            self.state = 313
            self.match(lde_parser.ADD)
            self.state = 314
            self.match(lde_parser.LPAREN)
            self.state = 315
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 316
            self.match(lde_parser.COMA)
            self.state = 317
            self.expresion()
            self.state = 318
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitDelStmt" ):
                return visitor.visitDelStmt(self)
            else:
                return visitor.visitChildren(self)




    def delStmt(self):

        localctx = lde_parser.DelStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 48, self.RULE_delStmt)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 320
            self.match(lde_parser.PUNTO)
            self.state = 321
            self.match(lde_parser.DEL)
            self.state = 322
            self.match(lde_parser.LPAREN)
            self.state = 323
            _la = self._input.LA(1)
            if not(_la==8 or _la==9):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 324
            self.match(lde_parser.COMA)
            self.state = 325
            self.expresion()
            self.state = 326
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitSizeStmt" ):
                return visitor.visitSizeStmt(self)
            else:
                return visitor.visitChildren(self)




    def sizeStmt(self):

        localctx = lde_parser.SizeStmtContext(self, self._ctx, self.state)
        self.enterRule(localctx, 50, self.RULE_sizeStmt)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 328
            self.match(lde_parser.TAMANO)
            self.state = 329
            self.match(lde_parser.LPAREN)
            self.state = 330
            self.factor()
            self.state = 331
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitTrigonometrica" ):
                return visitor.visitTrigonometrica(self)
            else:
                return visitor.visitChildren(self)




    def trigonometrica(self):

        localctx = lde_parser.TrigonometricaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 52, self.RULE_trigonometrica)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 333
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 2194728288256) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 334
            self.match(lde_parser.LPAREN)
            self.state = 335
            self.expresion()
            self.state = 336
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLista" ):
                return visitor.visitLista(self)
            else:
                return visitor.visitChildren(self)




    def lista(self):

        localctx = lde_parser.ListaContext(self, self._ctx, self.state)
        self.enterRule(localctx, 54, self.RULE_lista)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 338
            self.match(lde_parser.LBRACKET)
            self.state = 347
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if ((((_la - 10)) & ~0x3f) == 0 and ((1 << (_la - 10)) & 1008807978679205889) != 0):
                self.state = 339
                self.expresion()
                self.state = 344
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==65:
                    self.state = 340
                    self.match(lde_parser.COMA)
                    self.state = 341
                    self.expresion()
                    self.state = 346
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 349
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMatriz" ):
                return visitor.visitMatriz(self)
            else:
                return visitor.visitChildren(self)




    def matriz(self):

        localctx = lde_parser.MatrizContext(self, self._ctx, self.state)
        self.enterRule(localctx, 56, self.RULE_matriz)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 351
            self.match(lde_parser.LBRACKET)
            self.state = 360
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==43:
                self.state = 352
                self.lista()
                self.state = 357
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==65:
                    self.state = 353
                    self.match(lde_parser.COMA)
                    self.state = 354
                    self.lista()
                    self.state = 359
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 362
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitRelacional" ):
                return visitor.visitRelacional(self)
            else:
                return visitor.visitChildren(self)




    def relacional(self):

        localctx = lde_parser.RelacionalContext(self, self._ctx, self.state)
        self.enterRule(localctx, 58, self.RULE_relacional)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 364
            self.expresion()
            self.state = 365
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & 141863388262170624) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
            self.state = 366
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

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLogico" ):
                return visitor.visitLogico(self)
            else:
                return visitor.visitChildren(self)




    def logico(self):

        localctx = lde_parser.LogicoContext(self, self._ctx, self.state)
        self.enterRule(localctx, 60, self.RULE_logico)
        self._la = 0 # Token type
        try:
            self.state = 374
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [10, 26, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 43, 49, 50, 67, 68, 69]:
                self.enterOuterAlt(localctx, 1)
                self.state = 368
                self.expresion()
                self.state = 369
                _la = self._input.LA(1)
                if not(_la==57 or _la==58):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                self.state = 370
                self.expresion()
                pass
            elif token in [59]:
                self.enterOuterAlt(localctx, 2)
                self.state = 372
                self.match(lde_parser.NOT)
                self.state = 373
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





