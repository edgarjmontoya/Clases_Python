
class Persona:
 def __init__(self, nombre, edad):
 	self.nombre = nombre
 	self.edad = edad

 def saludar(self):
 	print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

# Crear una instancia (objeto) de la clase
persona1 = Persona("Lili", 32)
persona2 = Persona("Edgar", 33)

# Llamar a un método del objeto
persona1.saludar()
persona2.saludar()