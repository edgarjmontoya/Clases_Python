#Código para determinar si un número es de 3 dígitos

#Solicitamos el número entero al usuario
num = int(input("Por favor, ingrese un número para identificar si es de 3 dígitos: "))

#Hacemos la comparación para verificar si el número es de tres dígitos
if num >= 100 and num <= 999:
	print("Él número: ", num, " es de tres dígitos")

else:
	print("El número: ", num, " no es de tres dígitos")

