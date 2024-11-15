parser grammar lde_parser;

options { tokenVocab=lde_lexer; }

programa: expresion EOF;

expresion: termino ((SUMA | RESTA) termino)*;

termino: factor ((MULT | DIV | MOD | EXP) factor)*;  // Agregar EXP para exponenciación

factor: NUMERO
      | LPAREN expresion RPAREN
      | RESTA factor
      | trigonometrica
      | lista          // Añadir listas como posibles factores
      | matriz         // Añadir matrices como posibles factores
      ;

trigonometrica: (SIN | COS | TAN | ASIN | ACOS | ATAN | SINH | COSH | TANH) LPAREN expresion RPAREN;

// Regla para listas
lista: LBRACKET (expresion (COMA expresion)*)? RBRACKET; // Lista de expresiones separadas por comas

// Regla para matrices
matriz: LBRACKET (lista (COMA lista)*)? RBRACKET; // Lista de listas separadas por comas
