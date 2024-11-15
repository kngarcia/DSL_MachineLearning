parser grammar lde_parser;

options { tokenVocab=lde_lexer; }

programa: expresion EOF;

expresion
    : termino ((SUMA | RESTA) termino)*  // Ahora expresion maneja suma y resta después de termino
    ;

termino
    : factor ((MULT | DIV) factor)*     // termino maneja multiplicación y división
    ;

factor
    : NUMERO                          // número literal
    | LPAREN expresion RPAREN          // expresión entre paréntesis
    | RESTA factor                     // operador unario negativo
    ;

