#Imprime cada uno de los catacteres del texto
for i in "Edgar ":
	print (i)

#Combinamos for con condiciones
for i in "Edgar ":
	if i == "E" or i == "r":
		print("#")
	else:
		print(i)

#for con rangos
for i in range(4):
	print("i = ",i)

#for con rango y límites
for i in range (5, 10):
	print("i2 = ", i)

#for con rango y límites incrementando una cantidad de valor
for i in range (5, 50, 5):
	print("i3 = ", i)

#Para consultar, quitar el string Banano y solo imrpimir Fresa y Naranaja
fruta = ["Fresa", "Banano", "Naranja"]
for i in fruta[2]:
	print("i4 = ", i)

#Contabilizar caracteres de un string
for i in ["Edgar", "Sol", "Seis", "esternocleidomastoideo"]:
	print("i5 = ", i, "\t", len(i))#"\t" es para tabular

