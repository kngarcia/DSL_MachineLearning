parser grammar lde_parser;

options { tokenVocab=lde_lexer; }  // Importar los tokens del lexer

// Punto de entrada del parser
programa: expresion EOF;

// Reglas para las expresiones aritméticas con niveles de precedencia
expresion
    : RESTA expresion                  # negativo        // Signo negativo unario, alta precedencia
    | expresion MULT expresion         # multiplicacion  // Multiplicación
    | expresion DIV expresion          # division        // División
    | expresion SUMA expresion         # suma            // Suma binaria
    | expresion RESTA expresion        # resta           // Resta binaria
    | LPAREN expresion RPAREN          # parenExpr       // Expresiones entre paréntesis
    | NUMERO                           # numero         // Números
    ;
