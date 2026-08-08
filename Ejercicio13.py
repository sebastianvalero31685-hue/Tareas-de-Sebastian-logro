# Validación de cantidad a evaluar
cantidad = 0
while cantidad < 1:
    cantidad = int(input("¿Cuántos números deseas evaluar? (mínimo 1): "))
    if cantidad < 1:
        print("Debes ingresar una cantidad válida.")

# Contadores
positivos = 0
negativos = 0
ceros = 0

# Evaluación de números
for i in range(cantidad):
    val = float(input(f"Ingresa el número {i + 1}: "))
    if val > 0:
        positivos += 1
    elif val < 0:
        negativos += 1
    else:
        ceros += 1

print("\n--- RESULTADOS ---")
print(f"Positivos: {positivos} | Negativos: {negativos} | Ceros: {ceros}")