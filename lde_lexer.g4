lexer grammar lde_lexer;

// Operadores aritméticos
SUMA: '+';
RESTA: '-';   // Este es el operador de resta tanto binario como unario
MULT: '*';
DIV: '/';

// Paréntesis
LPAREN: '(';
RPAREN: ')';

// Números (enteros y decimales)
NUMERO: [0-9]+ ('.' [0-9]+)?;

// Ignorar espacios en blanco
ESPACIO: [ \t\r\n] -> skip;
