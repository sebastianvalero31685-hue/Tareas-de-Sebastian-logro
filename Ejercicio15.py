# Validación de texto no vacío
palabra = ""
while len(palabra.strip()) == 0:
    palabra = input("Ingresa una palabra: ")

vocales = "aeiouAEIOUáéíóúÁÉÍÓÚ"

print("\nAnálisis de cada letra:")
for pos, letra in enumerate(palabra):
    if letra in vocales:
        resultado = pos * 3
        print(f"Letra '{letra}' (posición {pos}): Vocal -> {pos} * 3 = {resultado}")
    else:
        resultado = pos // 2
        print(f"Letra '{letra}' (posición {pos}): Consonante -> {pos} // 2 = {resultado}")