import math

# Definir vectores
vector_a = [1, 2]
vector_b = [3, 4]

# Suma de vectores
suma = [vector_a[i] + vector_b[i] for i in range(len(vector_a))]
print("Suma de vectores:", suma)

# Resta de vectores
resta = [vector_a[i] - vector_b[i] for i in range(len(vector_a))]
print("Resta de vectores:", resta)

# Producto escalar
producto_escalar = sum(vector_a[i] * vector_b[i] for i in range(len(vector_a)))
print("Producto escalar:", producto_escalar)

# Magnitud de un vector
magnitud_a = math.sqrt(sum(component ** 2 for component in vector_a))
print("Magnitud del vector a:", magnitud_a)

# Magnitud del vector b
magnitud_b = math.sqrt(sum(component ** 2 for component in vector_b))
print("Magnitud del vector b:", magnitud_b)