#Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, pregunte al usuario por una divisa y muestre su símbolo
#o un mensaje de aviso si la divisa no está en el diccionario.

#.title() > Convierte una cadena de texto en una nueva cadena donde la primera letra de cada palabra está en mayúsculas, y el resto de las letras en minúsculas.

simbolo = {
    "Euro": "€",
    "Dolar": "$",
    "Yen": "¥"
}

divisa = input("¿Por cual divisa te gustaria consultar? ")

if divisa.title() in simbolo:
    print(f"La divisa es {simbolo[divisa.title()]}") #Es lo mismo que simbolo["Euro"], simbolo["Dolar"] o simbolo["Yen"] ya que es lo que ingresa por input
else:
    print("La divisa no se encuentra en el diccionario.")


#OTRA OPCION
#monedas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
#moneda = input("Introduce una divisa: ")
#print(monedas.get(moneda.title(), "La divisa no está.")) > Busca en el diccionario: Si encuentra la clave, devuelve su valor (el símbolo). Si no la encuentra, devuelve el mensaje "La divisa no está."

