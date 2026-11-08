# Ejercicio 5
# Escribir un programa que solicite al usuario una cantidad y luego itere la cantidad de veces dada
# En cada iteración, solicitar al usuario que ingrese un número. Al finalizar, mostrar la suma de todos los números ingresados.

cantidad = int(input("Ingresa una cantidad: "))
suma = 0

for i in range(cantidad):
    num = int(input(f"[{i + 1}] Ingresa un número: "))
    suma += num

print(f"La suma de todos los números integrados es {suma}")
