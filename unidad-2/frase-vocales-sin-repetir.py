# Ejercicio 6
# Solicitar al usuario que ingrese una frase y luego imprimir un listado de las vocales que aparecen en esa frase (sin repetirlas)
frase = input("Ingresa una frase: ")
vocales = "aeiouáéíóú"
vocales_encontradas = []

for caracter in frase.lower():
    if caracter in vocales and caracter not in vocales_encontradas:
        vocales_encontradas.append(caracter)

print(f"Vocales encontradas: {', '.join(vocales_encontradas)}")