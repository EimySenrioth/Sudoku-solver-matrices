import random #para que en el grid se mezclen las letras

# Letras disponibles
letras = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P'] # 16 letras qe voy a usar

#sudoku solver with backtracking usando nmero
def es_valido(grid, r, c, letra):#Como sabemos que el sudoku tiene forma de regillas de 4x4, entonces podemos usarlo para hacer una validacion de manera mas eficiente
    #done r es fial, c es la columna dento del grid y letra si es valido colocarla
    # Verifica fila
    if letra in grid[r]:#verifica si la letra esta en la fila si no es asi se puede colocar y si se encentranla misma ñletra da falso
        return False #no se puede colocar
    # Verifica columna
    if letra in [grid[i][c] for i in range(16)]: #si la letra esta yya en c en las columnass del 0 a 15, si ya esta no s pudes
        return False #evitar duplicados
    # Verifica sub-matriz 4x4
    box_r, box_c = (r // 4) * 4, (c // 4) * 4 #calcula la posicion de la regilla para la fila r y la columna c
    #en las submetricas de [c/4]*4, veamos: se divide la fila en 4, tamaño de la cuadricula en las celdas r, c
    #mltiplicar por 4 nos da la posicion de la regilla

    for i in range(box_r, box_r + 4): #litera sobre las filas en la submatriz
        for j in range(box_c, box_c + 4): #itera sobre las columnas en la submatriz
            if grid[i][j] == letra: #se comparan las letras
                return False #si ya la tenemos no se puede colocar
    return True

# Función de backtracking para llenar la matriz
def generar_matriz(grid, r=0, c=0):
    if r == 16:  # Si llegamos al final de la matriz, hemos llenado la matriz (ya que las filas se numeran de 0 a 15)
        return True
    elif c == 16:  # significa que hemos llegado al final de la columna de la fila actual
        return generar_matriz(grid, r + 1, 0)
    
    if grid[r][c] != '':  # Si la celda ya está llena, pasamos a la siguiente y compara si no es na celda vacia
        return generar_matriz(grid, r, c + 1) #llamamos a la recursividad para movernos
    
    # Intentamos colocar una letra válida
    random.shuffle(letras)  # Mezclar letras para aleatoriedad
    for letra in letras: #recorremos todas las letras
        if es_valido(grid, r, c, letra): #verificamos si la letra es valida
            grid[r][c] = letra #si es valida la colocamos
            if generar_matriz(grid, r, c + 1): #recursividad a la funcion, es decir iintenamos llenar la siguiente celda en la misma fila pero en la siguiente columna
                return True
            grid[r][c] = ''  # Si no funciona, retrocedemos
    
    return False  # Si no se encuentra una letra válida, fallamos

# Función de resolución (backtracking) para resolver el Sudoku
def resolver_matriz(grid, r=0, c=0):
    if r == 16:  # recorrimos todas las filas
        return True
    elif c == 16:  # Si hemos llegado al final de una fila, pasamos a la siguiente
        return resolver_matriz(grid, r + 1, 0)
    
    if grid[r][c] != '':  # Si la celda ya está llena, pasamos a la siguiente
        return resolver_matriz(grid, r, c + 1)#usando
    
    # Intentamos colocar una letra válida
    random.shuffle(letras)  # Mezclar letras para aleatoriedad
    for letra in letras:
        if es_valido(grid, r, c, letra): #verificamos si la letra es valida
            grid[r][c] = letra #si es valida la colocamos
            if resolver_matriz(grid, r, c + 1): #recursividad a la funcion
                return True
            grid[r][c] = ''  # Si no funciona, retrocedemos
    
    return False  # Si no se encuentra una letra válida, fallamos

# Inicializa la matriz vacía
def inicializar_matriz():
    return [['' for _ in range(16)] for _ in range(16)] #cada celda está vacía, representada por una cadena vacía ''
# una lista de comprecion doble con 16 filas y 16 columnas de cadenas vacias ''
# Función para imprimir la matriz
def imprimir_matriz(grid):
    for fila in grid:
        print(fila)
        #se imprmen en 16 elemneto y asi sucesivamente hata llegar a 16

# Generar la matriz inicial
matriz_inicial = inicializar_matriz()

if generar_matriz(matriz_inicial):
    print("Matriz inicial generada:")
    imprimir_matriz(matriz_inicial)
else:
    print("No se pudo generar una matriz inicial válida.")

# Simular un Sudoku incompleto (borrar celdas aleatorias)
def borrar_celdas(grid, num_borrados=40): #pusimos 40 para simular un sudoku incompleto, se puede ajutar a su gusto
    for _ in range(num_borrados):
        r, c = random.randint(0, 15), random.randint(0, 15) #generacion de indices aleatorios dentro del rango
        grid[r][c] = ''  # Borra el contenido de una celda, para que despues la llenemos

# Borrar celdas de la matriz generada para simular un Sudoku incompleto
matriz_incompleta = [fila[:] for fila in matriz_inicial]  # Copia de la matriz generada
#se crea una deep copy para que no cambie la matriz original
borrar_celdas(matriz_incompleta) #llama a la fncion y ya tenemos celdas borradas, asi que ahora tenemos un sudoku incompleto

print("\nMatriz incompleta (con celdas borradas):")
imprimir_matriz(matriz_incompleta)

# Resolver la matriz incompleta
matriz_resuelta = [fila[:] for fila in matriz_incompleta]  # Crear una copia de la matriz incompleta
#se crea una deep copy para que no cambie la matriz original con fila[:]
if resolver_matriz(matriz_resuelta): #llamamos a la fnciones qe creamos para crar la matriz inicial
    print("\nMatriz resuelta:") #si tenemos true
    imprimir_matriz(matriz_resuelta)#la imprime fila por fila
else:
    print("No se pudo resolver la matriz.") #upss, si no tenemos true, entonces no se puede resolver
