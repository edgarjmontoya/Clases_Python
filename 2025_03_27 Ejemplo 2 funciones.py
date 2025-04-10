#Código sin función
#Construir un programa que permita a un usuario
#ingresar un valor y determinar si este se
#encuentra o no en una array.

Array = [1, 2, 3, 4, 5] #Creamos el array con los valores
Comprobar = False #Creamos una variable booleana para comprobar si el valor ingresado se encuentra o no
NumeroUsuario = int(input("Ingrese el número a buscar: "))	#Almacenamos el valor ingresado por el usuario

for i in Array:
	if i == NumeroUsuario:
		Comprobar = True
	
if Comprobar:
	print("Lo encontré")

else:
	print("No lo encontré")


################################3
#El mismo requerimiento, pero implementando función
def BuscarDato (DatoUsuario, Lista):
	Verificar = False
	for j in Lista:
		if j == DatoUsuario:
			Verificar = True
	return Verificar

Conjunto = [1, 2, 3, 4, 5]
Valor = int(input("Dato a buscar: "))
if BuscarDato(Valor, Conjunto):
	print("Si está ese número en el conjunto")
else: 
	print("No existe ese número en el conjunto")

print("Fin")