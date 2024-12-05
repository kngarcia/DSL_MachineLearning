lexer grammar lde_lexer;


IF: 'if';
ELSE: 'else';
ELSE_IF: 'else if'; // Alternativamente, podrías usar ELSEIF o manejar 'else if' como una regla en el parser

// Operadores relacionales y lógicos
MAYOR: '>';
MENOR: '<';
MAYOR_IGUAL: '>=';
MENOR_IGUAL: '<=';
IGUALDAD: '==';
DIFERENTE: '!=';
AND: 'and';
OR: 'or';
NOT: 'not';


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
LBRACE: '{';
RBRACE: '}';


// Separadores
COMA: ','; 

// Identificadores para variables
ID: [a-zA-Z][a-zA-Z0-9]*;

// Números (enteros y decimales)
NUMERO: [0-9]+ ('.' [0-9]+)?;

// Ignorar espacios en blanco
ESPACIO: [ \t\r\n] -> skip;
