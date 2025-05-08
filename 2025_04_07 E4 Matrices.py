#Creamos una matriz
Matriz1 = [
	[20, 30, 50],
	[10, 70, 13],
	[10, 36, 72]
]
#Creamos segunda matriz
Matriz2 = [
	[100, 200, 300],
	[150, 250, 350],
	[400, 500, 600]
]
#Imprimimos los valores de la matriz 1
print("La matriz 1 contiene: ")
for i in Matriz1:
	print(i)

#Extraemos un valor de la matriz en una posición
Elemento = Matriz1 [1][2]
print("El elemento de la fila 1 y columna 2 es: ", Elemento)

#Hacemos una suma de dos componentes ubicados en cada una de las matrices
suma = Matriz1[0][2] + Matriz2[2][1]
print("La suma de los valores solicitados es: ", suma)