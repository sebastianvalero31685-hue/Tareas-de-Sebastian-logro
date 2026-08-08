# Validación del número entero positivo
numero = 0
while numero <= 0:
    numero = int(input("Ingresa un número entero positivo: "))
    if numero <= 0:
        print("Error: El número debe ser mayor a cero.")

# Cálculo de la suma de pares
suma_pares = 0
for i in range(1, numero + 1):
    if i % 2 == 0:
        suma_pares += i

print(f"La suma de los números pares del 1 al {numero} es: {suma_pares}")