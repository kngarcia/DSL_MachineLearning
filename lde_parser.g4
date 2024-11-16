parser grammar lde_parser;

options { tokenVocab=lde_lexer; }

programa: expresion EOF;

expresion: termino ((SUMA | RESTA) termino)*;

termino: factor ((MULT | DIV | MOD | EXP | PROD) factor)*; // Agregar PROD para producto punto

factor: NUMERO
      | LPAREN expresion RPAREN
      | RESTA factor
      | trigonometrica
      | lista
      | matriz
      ;

trigonometrica: (SIN | COS | TAN | ASIN | ACOS | ATAN | SINH | COSH | TANH) LPAREN expresion RPAREN;

lista: LBRACKET (expresion (COMA expresion)*)? RBRACKET;

matriz: LBRACKET (lista (COMA lista)*)? RBRACKET;
