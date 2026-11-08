# Ejercicio 11
# Crea un algoritmo que realice la sucesion de fibonacci
a = 0
b = 1
limite = 15

for i in range(limite):
    print(a, end=" ")

    siguiente_numero = a+b

    a = b
    b = siguiente_numero