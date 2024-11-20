parser grammar lde_parser;

options { tokenVocab=lde_lexer; }

programa: (declaracion | expresion | writeStmt | modificacion)* EOF;

declaracion: VAR ID IGUAL expresion;

modificacion: ID IGUAL expresion;

expresion: termino ((SUMA | RESTA) termino)*;

writeStmt: 'write' LPAREN expresion RPAREN;

termino: factor ((MULT | DIV | MOD | EXP) factor)*;

factor: NUMERO
      | ID                // Referencias a variables
      | LPAREN expresion RPAREN
      | RESTA factor
      | trigonometrica
      | lista
      | matriz
      ;

trigonometrica: (SIN | COS | TAN | ASIN | ACOS | ATAN | SINH | COSH | TANH) LPAREN expresion RPAREN;

lista: LBRACKET (expresion (COMA expresion)*)? RBRACKET;

matriz: LBRACKET (lista (COMA lista)*)? RBRACKET;
