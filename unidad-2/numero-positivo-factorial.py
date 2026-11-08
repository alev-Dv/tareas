# Ejercicio 10

# Dado un numero positivo, mostrar su factorial. El factorial de un número se obtiene multiplicando todos los números enteros
# positivos que hay entre el 1 y ese número
num = int(input("Ingresa un número: "))
numero_factorial = 1
if num > 0:
    for i in range(1, num + 1):
        numero_factorial *= i

    print(f"El factorial de {num} es {numero_factorial}")
else:
    print("El número ingresado es negativo")