class Libro():
	Tamano = "17x24"
	Peso = "200g"
	Paginas = 150
	Registrado = False
	Coleccion = "Ninguna"

	def Registrar(self):
		self.Registrar = True
		return "Si"

	def Inscribir(self):
		self.Coleccion = "Educativo"
		return self.Coleccion

InformacionLibro = Libro()

print("Tamano = ", InformacionLibro.Tamano)	
print("Peso = ", InformacionLibro.Peso)	
print("Paginas = ", InformacionLibro.Paginas)	
print("Registrado = ", InformacionLibro.Registrar())
print("Coleccion = ", InformacionLibro.Inscribir())