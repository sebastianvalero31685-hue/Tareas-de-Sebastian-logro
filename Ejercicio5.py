# Aplicación de descuento
total_compra = float(input("Ingresa el total de la compra: $"))

if total_compra > 500:
    descuento = total_compra * 0.10
    total_final = total_compra - descuento
    print(f"¡Descuento aplicado! Total a pagar: ${total_final:.2f}")
else:
    print(f"Total a pagar: ${total_compra:.2f}")