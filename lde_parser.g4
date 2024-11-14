parser grammar lde_parser;

options { tokenVocab=lde_lexer; }  // Importar los tokens del lexer

// Punto de entrada del parser
programa: expresion EOF;

// Reglas para las expresiones aritméticas con niveles de precedencia
expresion
    : '-' expresion                  # negativo  // Mayor precedencia para unario
    | expresion MULT expresion       # multiplicacion
    | expresion DIV expresion        # division
    | expresion SUMA expresion       # suma
    | expresion RESTA expresion      # resta
    | LPAREN expresion RPAREN        # parenExpr
    | NUMERO                         # numero
    ;
