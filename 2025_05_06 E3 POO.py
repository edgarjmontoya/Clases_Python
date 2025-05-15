class Cancion:
    def __init__(self, titulo, artista, duracion, genero):
        self.titulo = titulo
        self.artista = artista
        self.duracion = duracion  # en minutos
        self.genero = genero

    def reproducir(self):
        print(f"😁✔️😅💀🎄🌹 Reproduciendo: '{self.titulo}' por {self.artista}...")

    def mostrar_info(self):
        return f"Título: {self.titulo}\nArtista: {self.artista}\nDuración: {self.duracion} min\nGénero: {self.genero}"

    def cambiar_titulo(self, nuevo_titulo):
        self.titulo = nuevo_titulo
        print(f"El título de la canción ha sido cambiado a: {self.titulo}")

# Instancia del objeto
reproducir = Cancion("A Little Piece of Heaven", "Avenged Seven Fold", 8.2, "Rock")

# Uso de los métodos
reproducir.reproducir()
print(reproducir.mostrar_info())
reproducir.cambiar_titulo("Perfect")
