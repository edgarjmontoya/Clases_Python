
# Matriz que representa una cruz
cruz = [
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0],
    [1, 1, 1, 1, 1],
    [0, 0, 1, 0, 0],
    [0, 0, 1, 0, 0]
]

# Imprimir la figura de la cruz
for fila in cruz:
    for pixel in fila:
        if pixel == 1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()