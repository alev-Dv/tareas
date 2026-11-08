# Ejercicio 6
# Solicitar al usuario que ingrese una frase y luego imprimir la cantidad de vocales que se encuentran en dicha frase.
frase = input("Ingresa una frase: ")
vocales = "aeiouáéíóú"
vocales_encontradas = []

for caracter in frase.lower():
    if caracter in vocales:
        vocales_encontradas.append(caracter)

print(f"Cantidad de vocales: {len(vocales_encontradas)}")
print(f"Vocales encontradas: {', '.join(vocales_encontradas)}")