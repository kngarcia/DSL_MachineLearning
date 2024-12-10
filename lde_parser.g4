parser grammar lde_parser;

options { tokenVocab=lde_lexer; }

programa: (sizeStmt | declaracion | expresion | (relacional | logico) | writeStmt | graficarStmt | exportarStmt | modificacion | ifStmt | forStmt | whileStmt | breakStmt | regresionLinealStmt)* EOF;

declaracion: VAR ID IGUAL (expresion | extraerStmt | regresionLinealStmt | funcionAct | classificadorStmt | predecirStmt | agruparStmt | evaluarStmt );

modificacion: ID acceso? IGUAL (expresion | extraerStmt | regresionLinealStmt | funcionAct | classificadorStmt | predecirStmt | agruparStmt);

expresion: termino ((SUMA | RESTA) termino)*;

writeStmt: 'write' LPAREN (expresion | relacional | logico) RPAREN;

graficarStmt: 'plot' LPAREN tipoGrafico COMA expresion (COMA expresion)? RPAREN;

tipoGrafico: BARRASPLOT | HISTOGRAMA | SCATTERPLOT | SCATTERDENS | LINEASPLOT | HEATMAP | expresion;

extraerStmt: 'extract' LPAREN ARCHIVO RPAREN;

exportarStmt: 'export' LPAREN expresion COMA ARCHIVO RPAREN;

ifStmt: IF LPAREN (relacional | logico) RPAREN bloque (ELSE bloque)?;

forStmt: 'for' LPAREN (declaracion | ID) COMA (relacional | logico) COMA modificacion RPAREN bloque;

whileStmt: 'while' LPAREN (TRUE | relacional | logico) RPAREN bloque;

breakStmt: BREAK;

regresionLinealStmt: 'regression' LPAREN expresion COMA expresion RPAREN;

funcionAct: SIGMOID | RELU | TAHACT | SOFTMAX;

classificadorStmt: 'classifier' LPAREN expresion COMA expresion COMA expresion COMA funcionAct COMA expresion COMA expresion RPAREN;

predecirStmt: ID PUNTO 'predict' LPAREN expresion RPAREN;

evaluarStmt: ID PUNTO 'evaluate' LPAREN expresion COMA expresion RPAREN;


agruparStmt: 'cluster' LPAREN expresion COMA expresion RPAREN;

bloque: INBLOCK ( sizeStmt | declaracion | expresion | (relacional | logico) | writeStmt | graficarStmt | exportarStmt | modificacion | ifStmt | forStmt | whileStmt | breakStmt | regresionLinealStmt)* ENBLOCK;

termino: factor ((MULT | DIV | MOD | EXP) factor)*;

factor: NUMERO
      | ID (acceso | addStmt | delStmt)?                // Referencias a variables con acceso opcional a elementos
      | LPAREN expresion RPAREN
      | RESTA factor
      | trigonometrica
      | lista
      | matriz
      | STRING
      | TRUE
      | FALSE
      ;

acceso: LBRACKET (expresion | ROWS | COLUMNS) RBRACKET acceso?;

addStmt: PUNTO 'add' LPAREN (ROWS | COLUMNS) COMA expresion RPAREN;

delStmt: PUNTO 'del' LPAREN (ROWS | COLUMNS) COMA expresion RPAREN;

sizeStmt: 'size' LPAREN factor RPAREN;

trigonometrica: (SIN | COS | TAN | ASIN | ACOS | ATAN | SINH | COSH | TANH) LPAREN expresion RPAREN;

lista: LBRACKET (expresion (COMA expresion)*)? RBRACKET;

matriz: LBRACKET (lista (COMA lista)*)? RBRACKET;

relacional: expresion (MAYOR | MENOR | MAYOR_IGUAL | MENOR_IGUAL | IGUALDAD | DIFERENTE) expresion;

logico: expresion (AND | OR) expresion
      | NOT expresion;
