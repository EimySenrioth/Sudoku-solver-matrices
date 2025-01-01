import random

# Función para generar una matriz cuadrada de tamaño n x n llena de 0s y 1s aleatoriamente
def generar_matriz(n):
    matriz = []
    for i in range(n):
        fila = [random.randint(0, 1) for _ in range(n)]
        matriz.append(fila)
    return matriz

# Función para imprimir la matriz de manera legible
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Función para generar un patrón aleatorio 2x2
def generar_patron():
    return [[random.randint(0, 1), random.randint(0, 1)],
            [random.randint(0, 1), random.randint(0, 1)]]

# Función para buscar cuántas veces un patrón 2x2 se repite en una matriz
def contar_patron_en_matriz(matriz, patron):
    n = len(matriz)
    contador = 0
    for i in range(n - 1):  # Recorremos hasta n-1 para evitar desbordar el índice
        for j in range(n - 1):  
            if (matriz[i][j] == patron[0][0] and matriz[i][j+1] == patron[0][1] and
                matriz[i+1][j] == patron[1][0] and matriz[i+1][j+1] == patron[1][1]):
                contador += 1
    return contador

# Función principal
def main():
    # Solicitar la dimensión de la matriz
    while True:
        n = int(input("Ingrese la dimensión de la matriz cuadrada (mayor o igual a 3): "))
        if n >= 3:
            break
        else:
            print("La dimensión debe ser mayor o igual a 3.")

    # Generar la matriz aleatoria
    matriz = generar_matriz(n)
    
    print("\nMatriz generada:")
    imprimir_matriz(matriz)
    
    # Generar 5 patrones aleatorios y contar cuántas veces se repiten en la matriz
    patrones = [generar_patron() for _ in range(5)]
    
    for i, patron in enumerate(patrones):
        print(f"\nPatrón {i+1}:")
        for fila in patron:
            print(fila)
        
        repeticiones = contar_patron_en_matriz(matriz, patron)
        print(f"El patrón {i+1} se repitió {repeticiones} veces.")

# Ejecutar el programa
if __name__ == "__main__":
    main()
