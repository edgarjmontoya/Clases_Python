#Importamos librería
import math

i = 10
while i <= 50:
	print("Raiz cuadrara de ", i, " = ", (round(math.sqrt(i), 2)))
	i = i + 10
print("fin\n")

#Determinar cuántos caracteres tiene un string
Contador = 0
Frase = input("Escriba un frase: ")

for i in Frase:
	if i == "a":
		Contador = Contador + 1

print("nLa frase tiene", Contador, " a repetidas")