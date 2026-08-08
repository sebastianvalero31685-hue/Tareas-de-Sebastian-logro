# Categorización de temperatura
temp = float(input("Ingresa la temperatura en °C: "))

if temp < 15:
    print("Ambiente frío")
elif temp >= 15 and temp <= 25:
    print("Ambiente templado")
else:
    print("Ambiente caluroso")