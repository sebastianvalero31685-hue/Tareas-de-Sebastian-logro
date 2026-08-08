NUMERO_OCULTO = 15
jugar_de_nuevo = "si"

while jugar_de_nuevo.lower() == "si":
    adivinado = False
    print("\n--- ¡Nuevo juego! Tienes 3 intentos ---")
    
    for intento in range(1, 4):
        num = int(input(f"Intento {intento}: Ingresa tu número: "))
        
        if num == NUMERO_OCULTO:
            print("¡Felicidades! Adivinaste el número. 🎉")
            adivinado = True
            break
        elif num < NUMERO_OCULTO:
            print("El número oculto es MAYOR.")
        else:
            print("El número oculto es MENOR.")
            
    if not adivinado:
        print(f"Agotaste tus intentos. El número era {NUMERO_OCULTO}.")
        
    jugar_de_nuevo = input("\n¿Quieres volver a jugar? (si/no): ")