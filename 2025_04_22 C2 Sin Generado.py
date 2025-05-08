"""
Código con una función que entrega múltiplos de 3
"""

def Multiplo3 (Tope): #Definimos la función	
	Numero = 3 #Creamos variable 
	Lista = [] #Se inicia una array vacía
	while Numero < Tope: #Mientras Numero sea menor al Tope
		Lista.append(Numero) #Se anexa Numero a la lista
		Numero = Numero + 3 #Incrementa Numero en 3
	return Lista #Retorna el Array

print(Multiplo3(2000)) #Se imprime el retorno que entrega la función