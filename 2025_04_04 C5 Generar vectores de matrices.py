# Definir la matriz
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Extraer una fila (segunda fila)
vector_fila = matriz[1]
print("Vector Fila:", vector_fila)

# Extraer una columna (segunda columna)
vector_columna = [fila[1] for fila in matriz]
print("Vector Columna:", vector_columna)

# Extraer la diagonal principal
vector_diagonal = [matriz[i][i] for i in range(len(matriz))]
print("Vector Diagonal:", vector_diagonal)