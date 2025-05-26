# Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte al usuario por una fruta, un número de kilos
# y muestre por pantalla el precio de ese número de kilos de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.
# Banana > 1.35
# Manzana > 0.80
# Pera > 0.85
# Naranja > 0.70

frutas = {
    "Banana": 1.35,
    "Manzana": 0.80,
    "Pera": 0.85,
    "Naranja": 0.70
}

compra_fruta = input("¿Que fruta queres comprar? ").title()
kg_fruta = int(input("¿Cuantos kilos queres llevar? "))

if compra_fruta in frutas:
    precio = kg_fruta * float(frutas.get(compra_fruta)) #float porque son numeros con decimales
    print(f"El precio seria ${precio:.2f} por los {kg_fruta}kg de {compra_fruta}.") #f"{resultado:.2f}" redondea a dos decimales
else:
    print("No nos queda esa fruta.")