# Paso por valor (objetos inmutables)
def modificar_valor(x):
    x = x + 10
    print("Dentro de la función, x:", x)

a = 5
modificar_valor(a)
print("Fuera de la función, a:", a)

# Paso por referencia (objetos mutables)
def modificar_lista(lista):
    lista.append(4)
    print("Dentro de la función, lista:", lista)

mi_lista = [1, 2, 3]
modificar_lista(mi_lista)
print("Fuera de la función, mi_lista:", mi_lista)