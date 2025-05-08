def PromedioLista(Lista):
    return sum(Lista)/ len(Lista)

Numeros = []

print("Ingrese los numeros uno por uno. Cuando quiera finalizar escriba 'fin'")

while True:
    Entrada = input("Número: ")

    if Entrada == "fin":
        break

    Numero = int(Entrada)
    Numeros.append(Numero)

Promedio = PromedioLista(Numeros)
print("El promedio ingresado es: ", Promedio)