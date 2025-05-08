"""
Código para obtener los múltiplos de 3 hasta un tope, implementando un generador
"""
def Multiplo3 (Tope): #Definimos la función	
	Numero = 3 #Creamos variable 
	while Numero < Tope: #Mientras Numero sea menor al Tope
		yield Numero #Pausa temporalmente la función y entrega un valor
		Numero = Numero + 3 #Incrementa Numero en 3

GeneradorMultiplo = Multiplo3(2000) #Almacena el dato que se va generando de la función

for i in GeneradorMultiplo: #Para i en cada valor almacenado en GenerarMultiplo
	print(i) #Imprime el contenido de i