#Escribir un programa que cree un diccionario de traducción español-inglés. El usuario introducirá las palabras en español e inglés separadas por dos 
#puntos, y cada par <palabra>:<traducción> separados por comas. El programa debe crear un diccionario con las palabras y sus traducciones. Después pedirá
#una frase en español y utilizará el diccionario para traducirla palabra a palabra. Si una palabra no está en el diccionario debe dejarla sin traducir.

#.split() > divide el texto el palabras individuales usando un separador especifico que debe indicarse entre (). Si no se aclara, se divide por espacios. Ej .split(" "), .split(","), etc.
#end=" " > hace que las palabras se impriman en la misma linea separadas por espacios

dic_traduccion = {}

palabras = input("Ingrese la palabra en espanol e ingles separada por dos puntos(español:ingles): ")

#DA FORMATO:
for i in palabras.split(','): #divide la cadena por comas
    clave, valor = i.split(':') #hace que clave, valor sea clave: valor
    dic_traduccion[clave] = valor #añade la clave valor al diccionario

frase = input("Introduce una frase en español: ")

#TRADUCCION
for palabra in frase.split(): #divide la frase en palabras individuales
    if palabra in dic_traduccion:
        print(dic_traduccion[palabra], end=' ') #si existe imprime su traduccion
    else:
        print(palabra, end=' ') #si no existe, imprime la palabra original sin traduccion



