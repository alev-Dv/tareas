# Ejercicio 4

# Requerir al usuario que ingrese un número entero positivo e imprimir todos los números correlativos
# entre el ingresado por el usuario y uno menos del doble del mismo.

num = int(input("Ingresa un número: "))

if num > 0:
    limite_superior = (num * 2) - 1

    print(f"Números correlativos entre {num} y {limite_superior}")

    for i in range(num, limite_superior + 1):
        print(i)
else:
    print("El número ingresado es negativo.")
