import os
import antlr4
import readline  # Para historial de comandos y autocompletado
from colorama import Fore, Style
from lde_lexer import lde_lexer
from lde_parser import lde_parser
from evalVisitor import evalVisitor

# Función de completado para el comando `run` y `clear`
def completer(text, state):
    # Comandos disponibles
    commands = ["run ", "clear", "exit"]
    
    # Sugerencias para autocompletar
    if text.startswith("run "):
        prefix = text[4:]  # Eliminar "run "
        options = [f"run {f}" for f in os.listdir('.') if f.startswith(prefix)]
    else:
        options = [cmd for cmd in commands if cmd.startswith(text)]
        options += [f for f in os.listdir('.') if f.startswith(text)]
    
    if state < len(options):
        return options[state]
    return None

# Configurar readline para usar el autocompletador
readline.set_completer(completer)
readline.parse_and_bind("tab: complete")


# Mensaje de bienvenida
WELCOME_MESSAGE = Fore.GREEN + "Bienvenido al intérprete de tu DSL. Escribe 'exit' para salir." + Style.RESET_ALL

def clear_interpreter():
    os.system('cls' if os.name == 'nt' else 'clear')
    print(WELCOME_MESSAGE)

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
            
            input_stream = antlr4.InputStream(expresion)
            lexer = lde_lexer(input_stream)
            token_stream = antlr4.CommonTokenStream(lexer)
            parser = lde_parser(token_stream)
            tree = parser.expresion()  # Ajusta si la regla inicial es diferente
            
            resultado = visitor.visit(tree)
            print(Fore.CYAN + f"Resultado: {resultado}" + Style.RESET_ALL)
        except Exception as e:
            print(Fore.RED + f"Error: {e}" + Style.RESET_ALL)

def run_file(filename, visitor):
    try:
        # Validar que el archivo tenga extensión `.dsl`
        if not filename.endswith(".dsl"):
            raise ValueError("El archivo debe tener la extensión '.dsl'")
        
        # Intentar abrir y leer el archivo
        with open(filename, "r") as file:
            contenido = file.read()
            print(Fore.YELLOW + f"Ejecutando archivo: {filename}" + Style.RESET_ALL)
            
            # Procesar el contenido del archivo
            input_stream = antlr4.InputStream(contenido)
            lexer = lde_lexer(input_stream)
            token_stream = antlr4.CommonTokenStream(lexer)
            parser = lde_parser(token_stream)
            tree = parser.programa()  # Ajusta si la regla inicial es diferente
            
            # Evaluar el árbol usando el visitor
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

