# Función que recibe un nombre y lo muestra 5 veces en pantalla
def print_name_5_times(name):
    for _ in range(5):
        print(name)

# Función que recibe una cadena y un número n, y muestra la cadena n veces en pantalla
def print_string_n_times(string, n):
    for _ in range(n):
        print(string)

# Función que recibe una lista de datos numéricos y retorna la suma de dichos datos
def sum_of_numbers(numbers):
    return sum(numbers)

# Función que recibe una lista de datos numéricos y retorna el promedio de dichos datos
def average_of_numbers(numbers):
    return sum(numbers) / len(numbers) if numbers else 0

# Función que recibe una lista de datos numéricos y retorna el promedio de los datos pares
def average_of_even_numbers(numbers):
    even_numbers = [num for num in numbers if num % 2 == 0]
    return sum(even_numbers) / len(even_numbers) if even_numbers else 0

# Función que recibe una lista de cadenas y retorna la suma de la cantidad de letras de cada cadena
def total_characters(strings):
    return sum(len(s) for s in strings)

# Función que recibe dos datos enteros y retorna el dato mayor
def larger_of_two(a, b):
    return max(a, b)

# Función que recibe un valor entero y muestra la tabla de multiplicar de dicho valor
def multiplication_table(n):
    for i in range(1, 11):
        print(f"{n} x {i} = {n * i}")

# Función que recibe un valor entero y determina si su último dígito es 4
def last_digit_is_4(n):
    return str(n)[-1] == '4'

# Función que recibe una lista de datos enteros y retorna la cantidad de valores de la lista que terminan en 4
def count_numbers_ending_in_4(numbers):
    return sum(1 for num in numbers if str(num)[-1] == '4')

# Ejemplos de uso
print_name_5_times("Alice")
print_string_n_times("Hello", 3)
print(sum_of_numbers([1, 2, 3, 4, 5]))
print(average_of_numbers([1, 2, 3, 4, 5]))
print(average_of_even_numbers([1, 2, 3, 4, 5, 6]))
print(total_characters(["hello", "world"]))
print(larger_of_two(10, 20))
multiplication_table(5)
print(last_digit_is_4(1234))
print(count_numbers_ending_in_4([14, 24, 34, 45, 54]))