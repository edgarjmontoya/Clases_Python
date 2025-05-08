"""
Código para recibir dos número ingresados y dividirlos entre sí con excepción a división entre 0
Excepción para el ingreso de caracteres y estructura finally
"""
Valido = True #Creamos variable Booleana
while Valido: #Mientras Valido sea verdadero
	try: #Inica el control de la excepción
		Numerador = int(input("Ingrese el primer valor: ")) #Lee el primer valor
		Denominador = int(input("Ingrese el divisor	")) #Lee el segundo valor

		print(Numerador, "/", Denominador, "=", Numerador/Denominador) #Imprime el resultado
		Valido = False #Se pone en falso la variable

	except ZeroDivisionError: #El error de excepción
		print("El segundo valor no puede ser 0")
		print("Vuelva a ingresar los valores")
		print("-----------------------------------")

	except ValueError:
		print("Los valores deben ser números")
		print("Vuelva a ingresar los valores")
		print("-----------------------------------")

	finally: #Estructura finally
		print("Gracias por usar este código") #Esto siempre se ejecutará

print("Finalizó el código") #Imprimimos el mensaje al finalizar el código

