class Persona:
	def __init__(self, Nombre, Edad):
		self.Nombre = Nombre
		self.Edad = Edad

	def saludar(self):
		print(f"Hola, mi nombre es {self.Nombre} y tengo {self.Edad} años")

Persona1 = Persona("Edgar", 33)
Persona2 = Persona("Elliott", "0,2")

Persona1.saludar()
Persona2.saludar()
