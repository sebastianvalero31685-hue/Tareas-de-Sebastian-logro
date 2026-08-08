# División segura contra ceros
dividendo = float(input("Ingresa el dividendo (número a dividir): "))
divisor = float(input("Ingresa el divisor: "))

if divisor == 0:
    print("Error: División por cero no permitida.")
else:
    resultado = dividendo / divisor
    print(f"El resultado de la división es: {resultado}")