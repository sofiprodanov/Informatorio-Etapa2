#Escribir un programa que cree un diccionario simulando una cesta de la compra. El programa debe preguntar el artículo y su precio y añadir el par al 
#diccionario, hasta que el usuario decida terminar. Después se debe mostrar por pantalla la lista de la compra y el coste total, con el siguiente formato.

lista_de_compras = {}
continuar = True
costo = 0

while continuar:
    productos = input("Ingresa el producto: ")
    precio = float(input(f"Ingresa el precio de {productos}: "))
    lista_de_compras[productos] = precio
    continuar = input("Quieres agregar otro producto a la lista?si/no ").lower() == "si"


print("Lista de la compra")
for producto, precio in lista_de_compras.items():
    print(f"{producto}\t{precio}")
    costo += precio
print(f"Costo total {costo}")