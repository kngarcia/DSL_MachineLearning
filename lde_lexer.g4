lexer grammar lde_lexer;

// Operadores aritméticos
SUMA: '+';
RESTA: '-';
MULT: '*';
DIV: '/';
MOD: '%';
EXP: '^';
PROD: '@';   // Operador para producto punto

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

// Números (enteros y decimales)
NUMERO: [0-9]+ ('.' [0-9]+)?;

// Ignorar espacios en blanco
ESPACIO: [ \t\r\n] -> skip;
