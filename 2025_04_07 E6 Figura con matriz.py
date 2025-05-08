#Matriz Binaria
Cruz = [
	[1, 0, 1, 0, 1],
	[0, 1, 1, 1 ,0],
	[1, 1, 1, 1, 1],
	[0, 1, 1, 1 ,0],
	[1, 0, 1, 0, 1]
	]

#Imprmimos la figura
for i in Cruz:
	for j in i:
		if j == 1:
			print('#', end=' ')
		else:
			print(' ', end=' ')
	print()

