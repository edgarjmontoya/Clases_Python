"""
Código para recibir dos número ingresados y dividirlos entre sí con excepción a división entre 0
"""
try: #Inica el control de la excepción
	Numerador = int(input("Ingrese el primer valor: ")) #Lee el primer valor
	Denominador = int(input("Ingrese el divisor	")) #Lee el segundo valor

	print(Numerador, "/", Denominador, "=", Numerador/Denominador) #Imprime el resultado

except ZeroDivisionError: #El error de excepción
	print("No puedes ingresar 0 en el denominador")
	print("Reinicie el código y vuelva a intentarlo")

print("Finalizó el código") #Imprimimos el mensaje al finalizar el código
