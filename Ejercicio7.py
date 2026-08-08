# Comparador de números
a = float(input("Ingresa el primer número: "))
b = float(input("Ingresa el segundo número: "))

if a > b:
    print(f"El número mayor es {a}.")
elif b > a:
    print(f"El número mayor es {b}.")
else:
    print("Ambos números son exactamente iguales.")