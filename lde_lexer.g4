lexer grammar lde_lexer;

// Palabras reservadas
VAR: 'var';
WRITE: 'write';

// Operadores aritméticos
SUMA: '+';
RESTA: '-';
MULT: '*';
DIV: '/';
MOD: '%';
EXP: '^';
PROD: '@';   // Operador para producto punto

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

// Separadores
COMA: ','; 

// Identificadores para variables
ID: [a-zA-Z][a-zA-Z0-9]*;

// Números (enteros y decimales)
NUMERO: [0-9]+ ('.' [0-9]+)?;

// Ignorar espacios en blanco
ESPACIO: [ \t\r\n] -> skip;
