#Escribe un algoritmo que convierta una temperatura dada en grados Celsius a grados Fahrenheit.

#Obtenemos la temperatura en celsius
Temperatura = int(input("Por favor ingrese la temperatura en celsius para convertirla en fahrenheit"))

#Convertimos la temperatura
Conversion = (Temperatura * (9/5)) + 32

#Imprimimos la conversiónext
print("\nLa temperatura en fahenheit es: ", Conversion)