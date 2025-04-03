#While con continue - permite seguir con la siguiente iteración del código
i = 1
while i <= 5:
	if i == 3:
		i = i + 1
		continue
	else:
		i = i + 1
		print("i1 = 2025")
print("Fin\n")

#El break detiene el ciclo
i = 1
while i <= 5:
	if i == 3:
		i = i + 1
		break
	else:
		i = i + 1
		print("i2 = 2025")
print("Fin\n")