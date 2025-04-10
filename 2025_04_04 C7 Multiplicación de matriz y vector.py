# Definir la matriz y el vector
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

vector = [1, 2, 3]

# Multiplicación de matriz por vector
resultado = [sum(matriz[i][j] * vector[j] for j in range(len(vector))) for i in range(len(matriz))]

print("Resultado de la multiplicación de la matriz por el vector:", resultado)