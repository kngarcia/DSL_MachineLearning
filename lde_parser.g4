parser grammar lde_parser;

options { tokenVocab=lde_lexer; }

programa: (declaracion | expresion | (relacional | logico) | writeStmt | graficarStmt | exportarStmt | modificacion | ifStmt | forStmt | whileStmt | breakStmt)* EOF;

declaracion: VAR ID IGUAL (expresion | extraerStmt);

modificacion: ID IGUAL expresion;

expresion: termino ((SUMA | RESTA) termino)*;

writeStmt: 'write' LPAREN (expresion | relacional | logico) RPAREN;

graficarStmt: 'plot' LPAREN expresion RPAREN;

extraerStmt: 'extract' LPAREN ARCHIVO RPAREN;

exportarStmt: 'export' LPAREN expresion COMA ARCHIVO RPAREN;

ifStmt: IF LPAREN (relacional | logico) RPAREN bloque (ELSE bloque)?;

forStmt: 'for' LPAREN (declaracion | ID) COMA (relacional | logico) COMA modificacion RPAREN bloque;

whileStmt: 'while' LPAREN (TRUE | FALSE | relacional | logico) RPAREN bloque;

breakStmt: BREAK;

bloque: INBLOCK (declaracion | expresion | (relacional | logico) | writeStmt | graficarStmt | exportarStmt | modificacion | ifStmt | forStmt | whileStmt | breakStmt)* ENBLOCK;

termino: factor ((MULT | DIV | MOD | EXP) factor)*;

factor: NUMERO
      | ID acceso?                // Referencias a variables con acceso opcional a elementos
      | LPAREN expresion RPAREN
      | RESTA factor
      | trigonometrica
      | lista
      | matriz
      | STRING
      | TRUE
      | FALSE
      ;

acceso: LBRACKET expresion RBRACKET (LBRACKET expresion RBRACKET)?;

trigonometrica: (SIN | COS | TAN | ASIN | ACOS | ATAN | SINH | COSH | TANH) LPAREN expresion RPAREN;

lista: LBRACKET (expresion (COMA expresion)*)? RBRACKET;

matriz: LBRACKET (lista (COMA lista)*)? RBRACKET;

relacional: expresion (MAYOR | MENOR | MAYOR_IGUAL | MENOR_IGUAL | IGUALDAD | DIFERENTE) expresion;

logico: expresion (AND | OR) expresion
      | NOT expresion;