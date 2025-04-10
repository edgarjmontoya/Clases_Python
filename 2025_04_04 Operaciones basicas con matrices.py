# Crear matrices
matriz1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matriz2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

# Suma de matrices
suma = [[matriz1[i][j] + matriz2[i][j] for j in range(len(matriz1[0]))] for i in range(len(matriz1))]
print("Suma de matrices:")
for fila in suma:
    print(fila)

# Multiplicación de matrices
producto = [[sum(matriz1[i][k] * matriz2[k][j] for k in range(len(matriz1))) for j in range(len(matriz2[0]))] for i in range(len(matriz1))]
print("Producto de matrices:")
for fila in producto:
    print(fila)

# Transposición de una matriz
transpuesta = [[matriz1[j][i] for j in range(len(matriz1))] for i in range(len(matriz1[0]))]
print("Transposición de la matriz:")
for fila in transpuesta:
    print(fila)