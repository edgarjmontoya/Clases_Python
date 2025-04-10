# Variable global
x = 10

def mi_funcion():
    # Variable local
    y = 5
    # Modificar la variable global
    global x
    x = x + y
    print("Dentro de la función - x:", x)
    print("Dentro de la función - y:", y)

# Llamar a la función
mi_funcion()

# Imprimir la variable global fuera de la función
print("Fuera de la función - x:", x)