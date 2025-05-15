class Libro():						#Declaración de la clase libro
	Tamaño = "17x24"				#Tamaño del libro			
	Peso = "200g"					#Peso del libro
	Paginas = 150					#Cantidad de paginas del libro
	Registrado = False				#Booleano para identificar si se ha registrado
	Coleccion = "Ningua"			#Colección a la que pertenece
	Precio = 40000					#Precio del libro

	def Registrar(self):			#Metodo registrar
		self.Registrar = True		#El libro se registro
		return "Registrado"			#Retorna el texto

	def Inscribir(self):			#Metodo inscribir
		self.Coleccion = "Educativo"#Se incluye en la coleccion educativo
		return self.Coleccion		#Retorna el nombre de la colección

InformacionLibro = Libro()			#Crea el objeto libro
#Imprime los mensajes con cada característica
print("Tamaño = ", InformacionLibro.Tamaño)	
print("Peso = ", InformacionLibro.Peso)
print("Paginas = ", InformacionLibro.Paginas)
print("Registro = ", InformacionLibro.Registrar())
print("Coleccion = ", InformacionLibro.Inscribir())
print("Precio = ", InformacionLibro.Precio)