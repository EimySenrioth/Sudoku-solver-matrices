#sudoku solver with backtracking usando nmero
def is_valid(grid, r, c, k): #Como sabemos que el sudoku tiene forma de regillas de 4x4, entonces podemos usarlo para hacer una validacion de manera mas eficiente
    #done r es la fila y c es la columna dento del grid y k es el numero que se va a colocar
    # Check row
    not_in_row = k not in grid[r] #verifica si el numero k no se encuentra en la fila r del grid
    
    # Check column
    not_in_column = k not in [grid[i][c] for i in range(16)] #verifica si el numero k no se encuentra en la columna c del grid
    #aqui creo una lista de comprencion con los elementos de la columna c del grid, es decir recorre todos los numeros de la columna c del grid
    #la i va del 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 o 16
    
    # Check 4x4 box
    box_r, box_c = (r // 4) * 4, (c // 4) * 4 #calcula la posicion de la regilla para la fila r y la columna c
    #en las submetricas de [c/4]*4, veamos: se divide la fila en 4, tamaño de la cuadricula en las celdas r, c
    #mltiplicar por 4 nos da la posicion de la regilla
    not_in_box = k not in [grid[i][j] for i in range(box_r, box_r + 4) 
                           for j in range(box_c, box_c + 4)] # se verifica si el numero k no se encuentra en la cuadricula 4x4
    #los box_r nos la coordennadas calculadas en la linea anterior (0, 1, 2 o 3, ejemplo)
    #implementalos de nuevo la lista de comprencion  para k no este en la regilla en i fila y j columna
    #y para j no da los vallores columna es dceir si tenemo 8, en en rango de 8 a 12 nmops dara 8,9,10,11 
    
    return not_in_row and not_in_column and not_in_box
#la funcion empesara en 0,0 y va de 0 a 16
def solve(grid, r=0, c=0):
    if r == 16: #ponemos el rnago de 16 porque el sudoku tiene 16 filas
        return True #si tenemos la solucion regresa true
    elif c == 16:
        return solve(grid, r+1, 0)#si es igual a 16 nos moevmos a la siguiente fila
    elif grid[r][c] != 0:#si la celda no esta vacia
        return solve(grid, r, c+1) #no se toca y nos movemos a la siguiente
    else: #backtracking
        for k in range(1, 17):  # Numeros 1-16
            if is_valid(grid, r, c, k):
                grid[r][c] = k #si es valido colocamos el numero y nos movemos, empezamos de nuevo
                if solve(grid, r, c+1): #implementamos recursividad, es decir lo sigue haciendo
                    return True #encontramos la solucion
                grid[r][c] = 0 #si no encontramos la solucion, volvemos a 0
        return False #lamentablemente no encontramos la solucion

# Optamos por un lista que es el grid en otras palabras el sudoku, lo pusimos todo en 0 para facilitar el tiempo
grid = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
]

# Solve the Sudoku
print(f"matriz inicial:\n{grid}")
if solve(grid): #llamamos a la funcion solve para el sudoku osea grid
    for row in grid: #vamos a iterar en las filas dentro del sudoku
        print(row)
else:
    print("No solution exists.")

#porque este enfoque: 