import os
import antlr4
import readline  # Para historial de comandos y autocompletado
from colorama import Fore, Style
from lde_lexer import lde_lexer
from lde_parser import lde_parser
from evalVisitor import evalVisitor


# Listener personalizado para errores
class CustomErrorListener(antlr4.error.ErrorListener.ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        raise Exception(f"Error de sintaxis en la línea {line}, columna {column}: {msg}")


# Función de completado para el comando `run` y `clear`
def completer(text, state):
    commands = ["run ", "clear", "exit"]
    if text.startswith("run "):
        prefix = text[4:]  # Eliminar "run "
        options = [f"run {f}" for f in os.listdir('.') if f.startswith(prefix)]
    else:
        options = [cmd for cmd in commands if cmd.startswith(text)]
        options += [f for f in os.listdir('.') if f.startswith(text)]
    return options[state] if state < len(options) else None


# Configurar readline para usar el autocompletador
readline.set_completer(completer)
readline.parse_and_bind("tab: complete")


# Mensaje de bienvenida
WELCOME_MESSAGE = Fore.GREEN + "Bienvenido al intérprete. Escribe 'exit' para salir." + Style.RESET_ALL


def clear_interpreter():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(WELCOME_MESSAGE)


def check_balanced_parentheses(expression):
    """Verifica si los paréntesis están balanceados."""
    balance = 0
    for char in expression:
        if char == '(':
            balance += 1
        elif char == ')':
            balance -= 1
        if balance < 0:
            return False  # Hay un paréntesis de cierre sin apertura
    return balance == 0  # Si al final el balance es 0, los paréntesis están balanceados


def run_repl():
    print(WELCOME_MESSAGE)
    visitor = evalVisitor()

    while True:
        try:
            expresion = input(Fore.BLUE + ">>> " + Style.RESET_ALL)
            if expresion.lower() == "exit":
                print(Fore.YELLOW + "Saliendo del intérprete." + Style.RESET_ALL)
                break

            if expresion.lower() == "clear":
                clear_interpreter()
                continue

            if expresion.startswith("run "):  # Comando `run`
                filename = expresion[4:].strip()
                run_file(filename, visitor)
                continue

            # Verificar si los paréntesis están balanceados
            if not check_balanced_parentheses(expresion):
                print(Fore.RED + "Error: Paréntesis desbalanceados" + Style.RESET_ALL)
                continue

            # Proceso de análisis
            input_stream = antlr4.InputStream(expresion)
            lexer = lde_lexer(input_stream)
            token_stream = antlr4.CommonTokenStream(lexer)
            parser = lde_parser(token_stream)

            # Agregar el listener personalizado para manejar errores
            parser.removeErrorListeners()  # Remover listeners por defecto
            parser.addErrorListener(CustomErrorListener())

            tree = parser.expresion()  # Ajusta si la regla inicial es diferente

            # Evaluar el árbol
            resultado = visitor.visit(tree)
            if isinstance(resultado, float):  # Formatear resultados numéricos
                print(Fore.CYAN + f"Resultado: {resultado:.4f}" + Style.RESET_ALL)
            else:
                print(Fore.CYAN + f"Resultado: {resultado}" + Style.RESET_ALL)

        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)


def run_file(filename, visitor):
    try:
        if not filename.endswith(".dsl"):
            raise ValueError("El archivo debe tener la extensión '.dsl'")

        with open(filename, "r") as file:
            contenido = file.read()
            print(Fore.YELLOW + f"Ejecutando archivo: {filename}" + Style.RESET_ALL)

            input_stream = antlr4.InputStream(contenido)
            lexer = lde_lexer(input_stream)
            token_stream = antlr4.CommonTokenStream(lexer)
            parser = lde_parser(token_stream)

            # Agregar el listener personalizado para manejar errores
            parser.removeErrorListeners()  # Remover listeners por defecto
            parser.addErrorListener(CustomErrorListener())

            tree = parser.programa()  # Ajusta si la regla inicial es diferente

            resultado = visitor.visit(tree)
            print(Fore.CYAN + f"Resultado del archivo: {resultado}" + Style.RESET_ALL)
    except FileNotFoundError:
        print(Fore.RED + f"Archivo no encontrado: {filename}" + Style.RESET_ALL)
    except ValueError as ve:
        print(Fore.RED + f"Error: {ve}" + Style.RESET_ALL)
    except Exception as e:
        print(Fore.RED + f"Error ejecutando archivo: {e}" + Style.RESET_ALL)


if __name__ == "__main__":
    run_repl()
