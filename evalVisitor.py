import math, csv,random
from lde_parserVisitor import lde_parserVisitor
from lde_parser import lde_parser
import matplotlib.pyplot as plt
from multilayer_perceptron import MultiLayerPerceptron
from cluster import KMeans

class BreakException(Exception):
    """Excepción personalizada para manejar 'break'."""
    pass
class BreakException(Exception):
    """Excepción personalizada para manejar 'break'."""
    pass

class evalVisitor(lde_parserVisitor):
    def __init__(self):
        super().__init__()
        self.variables = {}  # Diccionario para almacenar las variables

    def es_matriz(self, estructura):
        return isinstance(estructura, list) and all(isinstance(fila, list) for fila in estructura) and all(len(fila) == len(estructura[0]) for fila in estructura)

    def es_vector(self, estructura):
        return isinstance(estructura, list) and all(not isinstance(x, list) for x in estructura)

    def visitPrograma(self, ctx: lde_parser.ProgramaContext):
        resultados = [self.visit(child) for child in ctx.getChildren()]
        return [r for r in resultados if r is not None]
    def visitSizeStmt(self, ctx: lde_parser.SizeStmtContext):
        valor = self.visit(ctx.factor())
        
        if isinstance(valor, list):
            return len(valor)
        else:
            raise ValueError("Error: La función size solo se puede aplicar a listas o matrices.")
    def visitDeclaracion(self, ctx: lde_parser.DeclaracionContext):
        nombre = ctx.ID().getText()
        if ctx.extraerStmt():
            valor = self.visit(ctx.extraerStmt())
        elif ctx.regresionLinealStmt():
            valor = self.visit(ctx.regresionLinealStmt())
        elif ctx.funcionAct():
            valor = self.visit(ctx.funcionAct())
        elif ctx.classificadorStmt():
            valor = self.visit(ctx.classificadorStmt())
        elif ctx.predecirStmt():
            valor = self.visit(ctx.predecirStmt())
        elif ctx.agruparStmt():
            valor = self.visit(ctx.agruparStmt())
        else:
            valor = self.visit(ctx.expresion())
        self.variables[nombre] = valor
        return f"Variable '{nombre}' asignada con el valor {valor}."
    
    def visitModificacion(self, ctx: lde_parser.ModificacionContext):
        nombre = ctx.ID().getText()
        if nombre not in self.variables:
            raise ValueError(f"Error: La variable '{nombre}' no está definida.")
        
        # Determina el nuevo valor a asignar
        if ctx.extraerStmt():
            nuevo_valor = self.visit(ctx.extraerStmt())
        elif ctx.regresionLinealStmt():
            nuevo_valor = self.visit(ctx.regresionLinealStmt())
        elif ctx.funcionAct():
            nuevo_valor = self.visit(ctx.funcionAct())
        elif ctx.classificadorStmt():
            nuevo_valor = self.visit(ctx.classificadorStmt())
        elif ctx.predecirStmt():
            nuevo_valor = self.visit(ctx.predecirStmt())
        elif ctx.agruparStmt():
            nuevo_valor = self.visit(ctx.agruparStmt())
        else:
            nuevo_valor = self.visit(ctx.expresion())
        
        # Si hay acceso, manejamos la modificación en niveles internos
        if ctx.acceso():
            estructura = self.variables[nombre]
            if not isinstance(estructura, list):
                raise ValueError("Error: El valor no es una lista o matriz.")
            acceso_ctx = ctx.acceso()
            while acceso_ctx:
                if acceso_ctx.ROWS():
                    fila_idx = self.visit(acceso_ctx.expresion())
                    if not isinstance(fila_idx, int):
                        raise ValueError("Error: El índice de fila debe ser un número entero.")
                    if fila_idx < 0 or fila_idx >= len(estructura):
                        raise IndexError("Error: Índice de fila fuera de rango.")
                    
                    # Modifica una fila específica
                    if acceso_ctx.acceso():
                        # Modificación a nivel individual en la fila
                        sub_acceso_ctx = acceso_ctx.acceso()
                        col_idx = self.visit(sub_acceso_ctx.expresion())
                        if not isinstance(col_idx, int):
                            raise ValueError("Error: El índice de columna debe ser un número entero.")
                        if col_idx < 0 or col_idx >= len(estructura[fila_idx]):
                            raise IndexError("Error: Índice de columna fuera de rango.")
                        
                        # Asigna el nuevo valor
                        estructura[fila_idx][col_idx] = nuevo_valor
                    else:
                        # Modifica toda la fila
                        if not isinstance(nuevo_valor, list) or len(nuevo_valor) != len(estructura[fila_idx]):
                            raise ValueError("Error: El nuevo valor no tiene el tamaño correcto para la fila.")
                        estructura[fila_idx] = nuevo_valor
                    break
                
                elif acceso_ctx.COLUMNS():
                    col_idx = self.visit(acceso_ctx.expresion())
                    if not isinstance(col_idx, int):
                        raise ValueError("Error: El índice de columna debe ser un número entero.")
                    if col_idx < 0 or col_idx >= len(estructura[0]):
                        raise IndexError("Error: Índice de columna fuera de rango.")
                    
                    # Modifica toda la columna
                    if not isinstance(nuevo_valor, list) or len(nuevo_valor) != len(estructura):
                        raise ValueError("Error: El nuevo valor no tiene el tamaño correcto para la columna.")
                    for i in range(len(estructura)):
                        estructura[i][col_idx] = nuevo_valor[i]
                    break
                
                else:
                    indice = self.visit(acceso_ctx.expresion())
                    if not isinstance(indice, int):
                        raise ValueError("Error: El índice debe ser un número entero.")
                    if indice < 0 or indice >= len(estructura):
                        raise IndexError("Error: Índice fuera de rango.")
                    
                    if acceso_ctx.acceso():
                        estructura = estructura[indice]
                        if not isinstance(estructura, list):
                            raise ValueError("Error: El valor no es una lista o matriz.")
                    else:
                        # Último nivel: actualiza el valor
                        estructura[indice] = nuevo_valor
                        break
                acceso_ctx = acceso_ctx.acceso()
        else:
            # Si no hay acceso, reemplaza toda la variable
            self.variables[nombre] = nuevo_valor
        
        return f"Variable '{nombre}' modificada con el valor {nuevo_valor}."
    def visitWriteStmt(self, ctx: lde_parser.WriteStmtContext):
        if ctx.expresion():
            valor = self.visit(ctx.expresion())
        elif ctx.relacional():
            valor = self.visit(ctx.relacional())
        elif ctx.logico():
            valor = self.visit(ctx.logico())
        else:
            raise ValueError("Error: Tipo de expresión no reconocido en writeStmt.")
        
        print(valor)
        return valor
    def visitGraficarStmt(self, ctx: lde_parser.GraficarStmtContext):
        tipo_grafico = ctx.tipoGrafico().getText()
        x = self.visit(ctx.expresion(0))
        y = self.visit(ctx.expresion(1)) if ctx.expresion(1) else None

        # Validación inicial
        if not self.es_vector(x) and tipo_grafico != 'heatmap':
            raise ValueError(f"Error: El argumento x debe ser un vector para '{tipo_grafico}'.")

        if tipo_grafico in ['scatter_plot', 'scatter_density', 'line_plot'] and y is None:
            raise ValueError(f"Error: El gráfico '{tipo_grafico}' requiere dos vectores (x, y).")

        # Crear gráfico
        if tipo_grafico == 'bar_plot':
            plt.bar(x, y if y else range(len(x)))  # Si y es None, usar índices como valores
            plt.title("Gráfico de Barras")
            plt.xlabel("Categoría")
            plt.ylabel("Valor")
        elif tipo_grafico == 'histogram':
            plt.hist(x, bins='auto')
            plt.title("Histograma")
            plt.xlabel("Valor")
            plt.ylabel("Frecuencia")
        elif tipo_grafico == 'scatter_plot':
            if not self.es_vector(y):
                raise ValueError("Error: Ambos argumentos deben ser vectores para 'scatter_plot'.")
            plt.scatter(x, y)
            plt.title("Gráfico de Dispersión")
            plt.xlabel("X")
            plt.ylabel("Y")
        elif tipo_grafico == 'scatter_density':
            if not self.es_vector(y):
                raise ValueError("Error: Ambos argumentos deben ser vectores para 'scatter_density'.")
            plt.hexbin(x, y, gridsize=30, cmap='Blues')
            plt.colorbar()
            plt.title("Gráfico de Densidad de Dispersión")
            plt.xlabel("X")
            plt.ylabel("Y")
        elif tipo_grafico == 'line_plot':
            plt.plot(x, y if y else range(len(x)))  # Si y es None, usar índices como valores
            plt.title("Gráfico de Líneas")
            plt.xlabel("X")
            plt.ylabel("Valor")
        elif tipo_grafico == 'heatmap':
            if not self.es_matriz(x):
                raise ValueError("Error: El argumento x debe ser una matriz para 'heatmap'.")
            plt.imshow(x, cmap='viridis', aspect='auto')
            plt.colorbar()
            plt.title("Mapa de Calor")
        else:
            raise ValueError(f"Error: Tipo de gráfico '{tipo_grafico}' no reconocido.")

        plt.show()

    def visitExtraerStmt(self, ctx: lde_parser.ExtraerStmtContext):
        archivo = ctx.ARCHIVO().getText()[1:-1]  # Eliminar las comillas alrededor del nombre del archivo
        matriz = []

        with open(archivo, newline='') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                fila = []
                for val in row:
                    try:
                        if '.' in val:
                            fila.append(float(val))
                        else:
                            fila.append(int(val))
                    except ValueError:
                        fila.append(val)  # Dejar el valor como cadena si no se puede convertir a número
                matriz.append(fila)

        # Si la matriz tiene solo una fila, devolverla como una lista
        if len(matriz) == 1:
            return matriz[0]
        return matriz
    def visitExportarStmt(self, ctx: lde_parser.ExportarStmtContext):
        data = self.visit(ctx.expresion())
        archivo = ctx.ARCHIVO().getText()[1:-1]  # Eliminar las comillas alrededor del nombre del archivo

        with open(archivo, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            if self.es_matriz(data):
                writer.writerows(data)
            elif self.es_vector(data):
                writer.writerow(data)
            else:
                raise ValueError("Error: Solo se pueden exportar vectores y matrices.")
            
    def visitRegresionLinealStmt(self, ctx: lde_parser.RegresionLinealStmtContext):
        x = self.visit(ctx.expresion(0))
        y = self.visit(ctx.expresion(1))

        if not (self.es_vector(x) and self.es_vector(y)):
            raise ValueError("Error: Los datos de entrada deben ser vectores.")

        if len(x) != len(y):
            raise ValueError("Error: Los vectores de entrada deben tener la misma longitud.")

        n = len(x)
        sum_x = sum(x)
        sum_y = sum(y)
        sum_x_squared = sum(xi ** 2 for xi in x)
        sum_xy = sum(xi * yi for xi, yi in zip(x, y))

        # Cálculo de los coeficientes de la regresión lineal
        m = (n * sum_xy - sum_x * sum_y) / (n * sum_x_squared - sum_x ** 2)
        b = (sum_y - m * sum_x) / n

        # Predicciones
        y_pred = [m * xi + b for xi in x]

        # Cálculo del Error Cuadrático Medio (MSE)
        mse = sum((yi - y_pred_i) ** 2 for yi, y_pred_i in zip(y, y_pred)) / n

        # Cálculo del Coeficiente de Determinación (R^2)
        y_mean = sum_y / n
        sse = sum((yi - y_pred_i) ** 2 for yi, y_pred_i in zip(y, y_pred))
        sst = sum((yi - y_mean) ** 2 for yi in y)
        r_squared = 1 - (sse / sst)

        # Cálculo del Error Estándar de la Pendiente (SE_m)
        se_m = (sse / (n - 2)) ** 0.5 / sum((xi - sum_x / n) ** 2 for xi in x) ** 0.5

        # Mostrar el gráfico de la regresión lineal
        plt.scatter(x, y, color='blue', label='Datos')
        plt.plot(x, y_pred, color='red', label='Regresión lineal')
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title('Regresión Lineal')
        plt.legend()
        plt.show()

        # Retornar los resultados como una lista
        return [m, b, mse, r_squared, se_m]

    def visitClassificadorStmt(self, ctx: lde_parser.ClassificadorStmtContext):
        X = self.visit(ctx.expresion(0))
        y = self.visit(ctx.expresion(1))
        layers = self.visit(ctx.expresion(2))
        activation_function = ctx.funcionAct().getText()
        learning_rate = self.visit(ctx.expresion(3))
        epochs = self.visit(ctx.expresion(4))

        if not (self.es_matriz(X) and (self.es_vector(y) or self.es_matriz(y))):
            raise ValueError("Error: Los datos de entrada deben ser una matriz y un vector o matriz.")

        if len(X) != len(y):
            raise ValueError("Error: La matriz de entrada y las etiquetas deben tener la misma longitud.")

        # Si se utiliza softmax, convertir y a codificación one-hot
        if activation_function.lower() == 'softmax':
            num_classes = int(max(y)) + 1
            y_one_hot = []
            for label in y:
                one_hot = [0] * num_classes
                one_hot[int(label)] = 1
                y_one_hot.append(one_hot)
            y = y_one_hot

        mlp = MultiLayerPerceptron(X, y, layers, activation_function, learning_rate, epochs)
        mlp.train()

        return mlp
    def visitPredecirStmt(self, ctx: lde_parser.PredecirStmtContext):
        nombre = ctx.ID().getText()
        if nombre not in self.variables:
            raise ValueError(f"Error: La variable '{nombre}' no está definida.")
        
        modelo = self.variables[nombre]
        if not isinstance(modelo, MultiLayerPerceptron):
            raise ValueError(f"Error: La variable '{nombre}' no es un modelo entrenado.")
        
        datos_nuevos = self.visit(ctx.expresion())
        predicciones = modelo.predict(datos_nuevos)
        
        return predicciones

    def visitEvaluarStmt(self, ctx: lde_parser.EvaluarStmtContext):
        modelo_nombre = ctx.ID(0).getText()
        if modelo_nombre not in self.variables:
            raise ValueError(f"Error: La variable '{modelo_nombre}' no está definida.")

        modelo = self.variables[modelo_nombre]
        if not isinstance(modelo, MultiLayerPerceptron):
            raise ValueError(f"Error: La variable '{modelo_nombre}' no es un modelo entrenado.")
        
        print(f"Evaluando modelo: {ctx.ID(0).getText()}")

        print("Árbol del contexto:")
        print(ctx.toStringTree(recog=self.parser))

        X_eval = self.visit(ctx.expresion(0))
        y_eval = self.visit(ctx.expresion(1))

        print(f"Datos de evaluación: X_eval={X_eval}, y_eval={y_eval}")

        if not (self.es_matriz(X_eval) and self.es_matriz(y_eval)):
            raise ValueError("Error: Los datos de evaluación deben ser matrices.")

        # Depuración adicional: Imprimir la forma y tipo de X_eval y y_eval
        print(f"Tipo de X_eval: {type(X_eval)}")
        print(f"Tipo de y_eval: {type(y_eval)}")
        print(f"Forma de X_eval: {len(X_eval)}x{len(X_eval[0]) if X_eval else 'unknown'}")
        print(f"Forma de y_eval: {len(y_eval)}x{len(y_eval[0]) if y_eval else 'unknown'}")

        # Evaluar el modelo
        metricas = modelo.evaluate(X_eval, y_eval)

        # Mostrar las métricas
        print("Resultados de evaluación:")
        print(f"Accuracy: {metricas['accuracy']:.4f}")
        for i, (precision, recall, f1) in enumerate(zip(metricas['precision'], metricas['recall'], metricas['f1_score'])):
            print(f"Clase {i}:")
            print(f"  Precision: {precision:.4f}")
            print(f"  Recall: {recall:.4f}")
            print(f"  F1-Score: {f1:.4f}")

        return metricas
    def visitAgruparStmt(self, ctx: lde_parser.AgruparStmtContext):
        # Obtener datos y número de clusters desde el contexto
        data = self.visit(ctx.expresion(0))
        k = self.visit(ctx.expresion(1))

        # Validar que los datos sean una matriz
        if not self.es_matriz(data):
            raise ValueError("Error: Los datos de entrada deben ser una matriz.")
        
        # Validar que k sea un entero positivo
        if not isinstance(k, int) or k <= 0:
            raise ValueError("Error: El número de clusters debe ser un entero positivo.")

        # Crear y entrenar el modelo KMeans
        kmeans = KMeans(k)
        kmeans.fit(data)

        # Generar el gráfico
        kmeans.plot_clusters(data)

        # Obtener los clusters predichos
        clusters = kmeans.predict(data)

        return clusters
    def visitExpresion(self, ctx: lde_parser.ExpresionContext):
        izquierda = self.visit(ctx.termino(0))
        for i in range(1, len(ctx.termino())):
            operador = ctx.getChild(i * 2 - 1).getText()
            derecha = self.visit(ctx.termino(i))
            if operador == '+':
                izquierda = self.sumar_o_restaurar(izquierda, derecha, 'sumar')
            elif operador == '-':
                izquierda = self.sumar_o_restaurar(izquierda, derecha, 'restar')
        return izquierda
    
    def visitTermino(self, ctx: lde_parser.TerminoContext):
        izquierda = self.visit(ctx.factor(0))
        for i in range(1, len(ctx.factor())):
            operador = ctx.getChild(i * 2 - 1).getText()
            derecha = self.visit(ctx.factor(i))
            if operador == '*':
                izquierda = self.multiplicar(izquierda, derecha)
            elif operador == '^':
                izquierda = self.transponer_o_invertir(izquierda, derecha)
            elif operador == '/':
                izquierda = self.dividir(izquierda, derecha)
            elif operador == '%':
                izquierda = self.modulo(izquierda, derecha)
        return izquierda
    
    def visitIfStmt(self, ctx: lde_parser.IfStmtContext):
        if ctx.relacional():
            condicion = self.visit(ctx.relacional())
        elif ctx.logico():
            condicion = self.visit(ctx.logico())
        else:
            raise ValueError("Error: Tipo de expresión no reconocido en ifStmt.")
        
        if condicion:
            self.visit(ctx.bloque(0))
        elif ctx.bloque(1):
            self.visit(ctx.bloque(1))
    def visitRelacional(self, ctx: lde_parser.RelacionalContext):
        izquierda = self.visit(ctx.expresion(0))
        operador = ctx.getChild(1).getText()
        derecha = self.visit(ctx.expresion(1))

        if operador == '>':
            return izquierda > derecha
        elif operador == '<':
            return izquierda < derecha
        elif operador == '>=':
            return izquierda >= derecha
        elif operador == '<=':
            return izquierda <= derecha
        elif operador == '==':
            return izquierda == derecha
        elif operador == '!=':
            return izquierda != derecha
        else:
            raise ValueError(f"Operador relacional no reconocido: {operador}")
    def visitLogico(self, ctx: lde_parser.LogicoContext):
        if ctx.NOT():
            return not self.visit(ctx.expresion(0))
        else:
            izquierda = self.visit(ctx.expresion(0))
            operador = ctx.getChild(1).getText()
            derecha = self.visit(ctx.expresion(1))

            if operador == 'and':
                return izquierda and derecha
            elif operador == 'or':
                return izquierda or derecha
            else:
                raise ValueError(f"Operador lógico no reconocido: {operador}")
            
    def visitForStmt(self, ctx: lde_parser.ForStmtContext):
        # Paso 1: Inicialización (opcional)
        if ctx.declaracion():
            self.visit(ctx.declaracion())  # Inicializar el iterador
        elif ctx.ID():
            iterador = ctx.ID().getText()
            if iterador not in self.variables:
                raise ValueError(f"Error: La variable '{iterador}' no está definida.")
        else:
            raise ValueError("Error: Falta la inicialización del iterador en forStmt.")
        
        # Paso 2: Definir funciones auxiliares
        def evaluar_condicion():
            if ctx.relacional():
                return self.visit(ctx.relacional())
            elif ctx.logico():
                return self.visit(ctx.logico())
            else:
                raise ValueError("Error: Tipo de condición no reconocido en forStmt.")

        def realizar_incremento():
            if ctx.modificacion():
                self.visit(ctx.modificacion())
            else:
                raise ValueError("Error: Incremento no especificado en forStmt.")

        # Paso 3: Ejecutar el bucle
        try:
            while evaluar_condicion():
                try:
                    self.visit(ctx.bloque())  # Ejecutar el cuerpo del bucle
                except BreakException:
                    break  # Rompe el bucle
                realizar_incremento()  # Realizar la modificación al final de cada iteración
        except BreakException:
            pass  # Capturar el 'break' si se lanza desde el cuerpo del bucle

    def visitWhileStmt(self, ctx: lde_parser.WhileStmtContext):
        def evaluar_condicion():
            if ctx.TRUE():
                return True
            elif ctx.relacional():
                return self.visit(ctx.relacional())
            elif ctx.logico():
                return self.visit(ctx.logico())
            else:
                raise ValueError("Error: Tipo de condición no reconocido en whileStmt.")

        try:
            while evaluar_condicion():
                try:
                    self.visit(ctx.bloque())  # Ejecutar el cuerpo del bucle
                except BreakException:
                    break  # Rompe el bucle
        except BreakException:
            pass  # Capturar el 'break' si se lanza desde el cuerpo del bucle

    def visitBreakStmt(self, ctx: lde_parser.BreakStmtContext):
        """Lanza la excepción para romper un bucle."""
        raise BreakException()
    
    def visitFactor(self, ctx: lde_parser.FactorContext):
        if ctx.NUMERO():
            return float(ctx.NUMERO().getText()) if '.' in ctx.NUMERO().getText() else int(ctx.NUMERO().getText())
        elif ctx.ID():
            nombre = ctx.ID().getText()
            if nombre in self.variables:
                valor = self.variables[nombre]
                if ctx.acceso():
                    return self.visitAcceso(ctx.acceso(), valor)
                elif ctx.addStmt():
                    return self.visitAddStmt(ctx.addStmt(), nombre)  # Pasamos el nombre
                elif ctx.delStmt():
                    return self.visitDelStmt(ctx.delStmt(), nombre)  # Pasamos el nombre
                return valor
            else:
                raise ValueError(f"Error: La variable '{nombre}' no está definida.")
        elif ctx.expresion():
            return self.visit(ctx.expresion())
        elif ctx.RESTA():
            return -self.visit(ctx.factor())
        elif ctx.trigonometrica():
            return self.visit(ctx.trigonometrica())
        elif ctx.lista():
            return self.visit(ctx.lista())
        elif ctx.matriz():
            return self.visit(ctx.matriz())
        elif ctx.STRING():
            return ctx.STRING().getText()[1:-1]  # Eliminar las comillas alrededor del string
        elif ctx.TRUE():
            return True
        elif ctx.FALSE():
            return False
        else:
            raise ValueError("Error: Factor no válido.")

    def visitAcceso(self, ctx: lde_parser.AccesoContext, valor):
        while ctx is not None:
            if not isinstance(valor, list):
                raise ValueError("Error: El valor actual no es una lista o matriz.")
            
            # Acceso por filas (R)
            if ctx.ROWS():
                if not all(isinstance(sublista, list) for sublista in valor):
                    raise ValueError("Error: El valor no es una matriz.")
                
                # Validar acceso posterior (índice requerido)
                ctx = ctx.acceso()
                if ctx is None or not ctx.expresion():
                    raise ValueError("Error: Debe especificarse un índice para 'R'.")
                
                indice_fila = self.visit(ctx.expresion())
                if not isinstance(indice_fila, int):  # El índice debe ser un entero
                    raise ValueError("Error: El índice de fila debe ser un número entero.")
                if indice_fila < 0 or indice_fila >= len(valor):  # Índice fuera de rango
                    raise IndexError("Error: Índice de fila fuera de rango.")
                
                # Obtener la fila
                return valor[indice_fila]

            # Acceso por columnas (C)
            elif ctx.COLUMNS():
                if not all(isinstance(sublista, list) for sublista in valor):
                    raise ValueError("Error: El valor no es una matriz.")
                
                # Validar acceso posterior (índice o nombre de columna requerido)
                ctx = ctx.acceso()
                if ctx is None or not ctx.expresion():
                    raise ValueError("Error: Debe especificarse un índice o nombre para 'C'.")
                
                indice_columna = self.visit(ctx.expresion())
                if isinstance(indice_columna, str):  # Acceso por nombre
                    if not isinstance(valor[0], list) or indice_columna not in valor[0]:
                        raise ValueError(f"Error: La columna '{indice_columna}' no existe.")
                    indice_columna = valor[0].index(indice_columna)
                elif not isinstance(indice_columna, int):  # Acceso por índice
                    raise ValueError("Error: El índice debe ser un número entero o un nombre de columna.")
                
                if indice_columna < 0 or (isinstance(valor[0], list) and indice_columna >= len(valor[0])):
                    raise IndexError("Error: Índice de columna fuera de rango.")
                
                # Obtener la columna
                return [fila[indice_columna] for fila in valor]

            # Acceso directo por índice
            else:
                indice = self.visit(ctx.expresion())
                if not isinstance(indice, int):
                    raise ValueError("Error: El índice debe ser un número entero.")
                if indice < 0 or indice >= len(valor):
                    raise IndexError("Error: Índice fuera de rango.")
                valor = valor[indice]
            
            ctx = ctx.acceso()
        
        return valor



    def visitAddStmt(self, ctx: lde_parser.AddStmtContext, nombre):
        if nombre not in self.variables:
            raise ValueError(f"Error: La variable '{nombre}' no está definida.")
        
        valor = self.variables[nombre]
        datos = self.visit(ctx.expresion())

        if ctx.ROWS():  # Añadir una fila
            if not isinstance(valor, list) or any(not isinstance(fila, list) for fila in valor):
                raise ValueError("Error: El valor debe ser una matriz para agregar filas.")
            if not isinstance(datos, list):
                raise ValueError("Error: Los datos a agregar deben ser una lista para agregar una fila.")
            if len(datos) != len(valor[0]):
                raise ValueError("Error: La fila a agregar debe tener el mismo número de columnas.")
            valor.append(datos)
        
        elif ctx.COLUMNS():  # Añadir una columna
            if isinstance(valor, list) and all(isinstance(elem, list) for elem in valor):
                # El valor es una matriz
                if isinstance(datos, list):
                    if len(datos) != len(valor):
                        raise ValueError("Error: La columna a agregar debe tener el mismo número de filas.")
                    for i, fila in enumerate(valor):
                        fila.append(datos[i])
                else:
                    for fila in valor:
                        fila.append(datos)
            elif isinstance(valor, list):
                # El valor es una lista
                if isinstance(datos, list):
                    valor.extend(datos)
                else:
                    valor.append(datos)
            else:
                raise ValueError("Error: El valor debe ser una lista o matriz para agregar columnas.")
        
        else:  # Añadir un valor a una lista
            if isinstance(valor, list) and all(isinstance(elem, list) for elem in valor):
                raise ValueError("Error: Se debe especificar si se agrega una fila (ROWS) o una columna (COLUMNS) para matrices.")
            if isinstance(datos, list):
                valor.extend(datos)
            else:
                valor.append(datos)
        
        self.variables[nombre] = valor

    
    def visitDelStmt(self, ctx: lde_parser.DelStmtContext, nombre):
        if nombre not in self.variables:
            raise ValueError(f"Error: La variable '{nombre}' no está definida.")
        
        valor = self.variables[nombre]
        if not isinstance(valor, list):
            raise ValueError("Error: El valor debe ser una lista o matriz.")
        
        indice = self.visit(ctx.expresion())
        if ctx.ROWS():
            if not all(isinstance(fila, list) for fila in valor):
                raise ValueError("Error: No se puede eliminar una fila porque el valor no es una matriz.")
            if not isinstance(indice, int) or indice < 0 or indice >= len(valor):
                raise IndexError("Error: Índice fuera de rango al eliminar fila.")
            del valor[indice]
        elif ctx.COLUMNS():
            if isinstance(indice, str):
                if not all(isinstance(fila, list) for fila in valor) or not valor:
                    raise ValueError("Error: El valor no es una matriz válida para nombres de columnas.")
                if indice not in valor[0]:
                    raise ValueError(f"Error: La columna '{indice}' no existe.")
                indice = valor[0].index(indice)
            if not isinstance(indice, int) or indice < 0 or not all(len(fila) > indice for fila in valor):
                raise IndexError("Error: Índice fuera de rango al eliminar columna.")
            for fila in valor:
                del fila[indice]
        else:
            raise ValueError("Error: Se debe especificar si se elimina una fila o una columna.")
        
        self.variables[nombre] = valor


    
    def visitLista(self, ctx: lde_parser.ListaContext):
        # Handle list expressions like [1, 2, 3]
        return [self.visit(exp) for exp in ctx.expresion()]

    def visitTrigonometrica(self, ctx: lde_parser.TrigonometricaContext):
        operador = ctx.getChild(0).getText()
        argumento = self.visit(ctx.expresion())
        funciones_trigonometricas = {
            'sin': math.sin, 'cos': math.cos, 'tan': math.tan,
            'asin': math.asin, 'acos': math.acos, 'atan': math.atan,
            'sinh': math.sinh, 'cosh': math.cosh, 'tanh': math.tanh
        }
        if operador in funciones_trigonometricas:
            return round(funciones_trigonometricas[operador](math.radians(argumento)), 4)
        else:
            raise ValueError(f"Error: Función trigonométrica no reconocida '{operador}'.")

    def sumar_o_restaurar(self, a, b, operacion):
        if isinstance(a, list) and isinstance(b, list):
            if operacion == 'sumar':
                # Sumar matrices elemento por elemento
                return [ [x + y for x, y in zip(fila_a, fila_b)] for fila_a, fila_b in zip(a, b)]
            elif operacion == 'restar':
                # Restar matrices elemento por elemento
                return [ [x - y for x, y in zip(fila_a, fila_b)] for fila_a, fila_b in zip(a, b)]
        else:
            return a + b if operacion == 'sumar' else a - b

    def multiplicar_matrices(self, a, b):
        # Verifica que el número de columnas de 'a' sea igual al número de filas de 'b'
        if len(a[0]) != len(b):
            raise ValueError("Error: El número de columnas de la primera matriz debe ser igual al número de filas de la segunda matriz para multiplicarlas.")
        
        # Multiplica las matrices utilizando el producto punto entre filas de 'a' y columnas de 'b'
        resultado = []
        for fila_a in a:
            fila_resultado = []
            for col_b in zip(*b):
                fila_resultado.append(sum(x * y for x, y in zip(fila_a, col_b)))
            resultado.append(fila_resultado)
        return resultado


    def multiplicar(self, a, b):
        if self.es_matriz(a) and self.es_matriz(b):
            return self.multiplicar_matrices(a, b)
        elif self.es_vector(a) and self.es_vector(b):
            if len(a) != len(b):
                raise ValueError("Error: Los vectores deben tener el mismo tamaño para calcular el producto punto.")
            return self.producto_punto(a, b)
        elif self.es_matriz(a) and isinstance(b, (int, float)):
            return self.multiplicar_por_escalar(a, b)
        elif self.es_vector(a) and isinstance(b, (int, float)):
            return self.multiplicar_por_escalar(a, b)
        elif isinstance(a, list) and isinstance(b, list):
            # Multiplicación elemento a elemento
            if len(a) != len(b):
                raise ValueError("Error: Las listas deben tener la misma longitud para multiplicarlas elemento por elemento.")
            return [x * y for x, y in zip(a, b)]
        else:
            # Producto normal para escalares
            return a * b


    def multiplicar_por_escalar(self, estructura, escalar):
        if self.es_vector(estructura):
            # Multiplica cada elemento del vector por el escalar
            return [x * escalar for x in estructura]
        elif self.es_matriz(estructura):
            # Multiplica cada elemento de la matriz por el escalar
            return [[x * escalar for x in fila] for fila in estructura]
        else:
            raise ValueError("Error: Solo se pueden multiplicar vectores o matrices por un escalar.")


    def dividir(self, a, b):
        if isinstance(a, list) or isinstance(b, list):
            raise ValueError("Error: No se puede dividir listas o matrices.")
        return a / b

    def modulo(self, a, b):
        if isinstance(a, list) or isinstance(b, list):
            raise ValueError("Error: No se puede aplicar módulo a listas o matrices.")
        return a % b

    def transponer_o_invertir(self, a, b):
        if self.es_matriz(a):
            if b == 0:
                return self.calcular_transpuesta(a)
            elif b == -1:
                return self.calcular_inversa(a)
            else:
                raise ValueError("El operador ^ solo soporta -1 (inversa) y 0 (transpuesta) para matrices.")
        elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return a ** b
        else:
            raise ValueError("Operación no válida para los operandos dados.")

    def producto_punto(self, A, B):
        if len(A) != len(B):
            raise ValueError("Los vectores deben tener el mismo tamaño para calcular el producto punto.")
        return sum(x * y for x, y in zip(A, B))

    def calcular_transpuesta(self, matriz):
        if not self.es_matriz(matriz):
            raise ValueError("Solo se puede calcular la transpuesta de matrices.")
        return [list(fila) for fila in zip(*matriz)]

    def calcular_inversa(self, matriz):
        if not self.es_matriz(matriz) or len(matriz) != len(matriz[0]):
            raise ValueError("Solo las matrices cuadradas tienen inversa.")
        n = len(matriz)
        identidad = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        matriz = [fila + identidad[i] for i, fila in enumerate(matriz)]
        for i in range(n):
            pivote = matriz[i][i]
            if pivote == 0:
                raise ValueError("La matriz no es invertible.")
            for j in range(2 * n):
                matriz[i][j] /= pivote
            for k in range(n):
                if k != i:
                    factor = matriz[k][i]
                    for j in range(2 * n):
                        matriz[k][j] -= factor * matriz[i][j]
        return [fila[n:] for fila in matriz]
