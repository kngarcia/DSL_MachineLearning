parser grammar lde_parser;

options { tokenVocab=lde_lexer; }

expresion: termino ((SUMA | RESTA) termino)*;
termino: factor ((MULT | DIV | MOD | EXP) factor)*;  // Agregar EXP para exponenciación
factor: NUMERO
      | LPAREN expresion RPAREN
      | RESTA factor
      | trigonometrica
      ;

trigonometrica: (SIN | COS | TAN | ASIN | ACOS | ATAN | SINH | COSH | TANH) LPAREN expresion RPAREN;  // Nuevas funciones trigonométricas
