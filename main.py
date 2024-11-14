import antlr4
from lde_lexer import lde_lexer
from lde_parser import lde_parser
from evalVisitor import evalVisitor

def main():
    # Expresión de ejemplo
    expresion = " 1 + ( 1 ) "
    input_stream = antlr4.InputStream(expresion)

    # Crear el lexer y el parser
    lexer = lde_lexer(input_stream)
    token_stream = antlr4.CommonTokenStream(lexer)
    parser = lde_parser(token_stream)

    # Obtener el árbol de parseo
    tree = parser.expresion()  # Ajusta aquí si la regla inicial es diferente
    print("Árbol de sintaxis:", tree.toStringTree(recog=parser))  # Depuración

    # Evaluar la expresión usando el visitor
    visitor = evalVisitor()
    resultado = visitor.visit(tree)

    print("Resultado:", resultado)

if __name__ == "__main__":
    main()