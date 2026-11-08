# Ejercicio 9
# Escribir un programa que muestre la sumatoria de todos los múltiplos de 3 encontrados en 0 y 100
suma = 0

for i in range(0, 101, 3):
    suma += i

print(f"La sumatoria de todos los múltiplos de 3 en 0 y 100 es: {suma}")