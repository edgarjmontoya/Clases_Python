#Función simple
def saludar():
    print("¡Hola, mundo!")

saludar()  # Esto imprimirá "¡Hola, mundo!"

##############################################################
#Función con parámetros
def saludar(nombre):
    print(f"¡Hola, {nombre}!")

saludar("Edgar")  # Esto imprimirá "¡Hola, Edgar!"

#########################################################
#Función con retorno
def sumar(a, b):
    return a + b

resultado = sumar(3, 5)
print(resultado)  # Esto imprimirá 8

##########################################################
#Función con parámetros predeterminados
def saludar(nombre="mundo"):
    print(f"¡Hola, {nombre}!")

saludar()  # Esto imprimirá "¡Hola, mundo!"
saludar("José")  # Esto imprimirá "¡Hola, Carlos!"