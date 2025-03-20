#Solicitamos los datos del vendedor
CodigoVendedor = input("Ingrese el código del vendedor: ")
NombreVendedor = input("\nIngrese el nombre del vendedor: ")

#Creamos variables para almacenar las ventas de cada mes
VentasEnero = int(input("Ventas de enero: "))
VentasFebrero = int(input("Ventas de Febrero: "))
VentasMarzo = int(input("Ventas de Marzo: "))

#Calculamos el promedio
Promedio = (VentasEnero + VentasFebrero + VentasMarzo)/3

#Comparamos si cumple la meta del promedio de ventas del primer trimestre
if Promedio >= 1000:
	print("El vendedor ", NombreVendedor, " con códgio ", CodigoVendedor, " vendió un promedio de ", round(Promedio, 2), " por lo que cumplió la meta.")
else:
	print("El vendedor ", NombreVendedor, " con códgio ", CodigoVendedor, " vendió un promedio de ", round(Promedio, 2), " por lo que NO cumplió la meta.")
