lexer grammar lde_lexer;

// Palabras reservadas
VAR: 'var';
WRITE: 'write';
GRAFICAR: 'plot';
EXTRAER: 'extract';
EXPORTAR: 'export';
ARCHIVO: '\'' [a-zA-Z0-9_/]+ '.' [a-zA-Z0-9]+ '\'';
REGRESION: 'regression';
CLASIFICADOR: 'classifier';

// Operadores aritméticos
SUMA: '+';
RESTA: '-';
MULT: '*';
DIV: '/';
MOD: '%';
EXP: '^';

// Operadores de asignación
IGUAL: '=';

// Funciones trigonométricas básicas
SIN: 'sin';
COS: 'cos';
TAN: 'tan';

// Funciones trigonométricas avanzadas
ASIN: 'asin';
ACOS: 'acos';
ATAN: 'atan';
SINH: 'sinh';
COSH: 'cosh';
TANH: 'tanh';

// Paréntesis y corchetes
LPAREN: '(';
RPAREN: ')';
LBRACKET: '[';
RBRACKET: ']';
//CONDICIONALES
IF: 'if';
ELSE: 'else';
// Operadores relacionales y lógicos
TRUE: 'true';
FALSE: 'false';
MAYOR: '>';
MENOR: '<';
MAYOR_IGUAL: '>=';
MENOR_IGUAL: '<=';
IGUALDAD: '==';
DIFERENTE: '!=';
AND: 'and';
OR: 'or';
NOT: 'not';

//bucles Y bloques
INBLOCK: '{';
ENBLOCK: '}';
FOR: 'for';
WHILE: 'while';
BREAK: 'break';
// Separadores
COMA: ','; 
// Identificadores para variables
ID: [a-zA-Z][a-zA-Z0-9]*;

// Números (enteros y decimales)
NUMERO: [0-9]+ ('.' [0-9]+)?;
//strings
STRING: '"' ( ~["\\] | '\\' . )* '"';
// Ignorar espacios en blanco
ESPACIO: [ \t\r\n] -> skip;
