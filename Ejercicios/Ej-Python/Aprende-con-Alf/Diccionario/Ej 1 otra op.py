#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo
#o un mensaje de aviso si la divisa no está en el diccionario.

simbolo = {
    "euro": "€",
    "dolar": "$",
    "yen": "¥"
}

divisa = input("¿Por cual divisa te gustaria consultar? ")

if divisa in simbolo:
    print(f"El simbolo es {simbolo.get(divisa)}.")
else:
    print("La divisa que indicas no se encuentra en el diccionario.")
