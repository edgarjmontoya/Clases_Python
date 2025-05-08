#Creamos las matrices
Matriz1 = [
	[1, 2, 3],
	[4, 5, 6],
	[7, 8, 9]
]

Matriz2 = [
	[10, 20, 30],
	[40, 50, 60],
	[70, 80, 90]
]

#Suma de matrices
Suma = [[Matriz1[i][j]*Matriz2[i][j] 
		for j in range(len(Matriz1[0])) 
		]
		for i in range(len(Matriz1))
		]
print("La suma de las matrices es: ")

for k in Suma:
	print(k)