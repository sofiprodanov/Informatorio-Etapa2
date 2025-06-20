# Escribir un programa que reciba una cadena de caracteres y devuelva un diccionario con cada palabra que contiene y su frecuencia.
# Escribir otra función que reciba el diccionario generado con la función anterior y devuelva una tupla con la palabra más repetida y su frecuencia.

texto = input("Ingresa el texto: ")

def contador_palabras(texto):
    texto = texto.split() #dividir la cadena en subcadenas (Dividir el texto en palabras individuales). Ej La casa > "La", "casa"
    palabras = {}
    for i in texto:
        if i in palabras:
            palabras[i]+=1 #Si la palabra ya está en el diccionario, incrementar su conteo
        else:
            palabras[i]=1 #Si no está, agregarla al diccionario con conteo inicial 1
    return palabras #Devolver el diccionario con los conteos


def palabra_mas_repetida(palabras):
    max_palabra = ""
    max_frecuencia = 0
    for palabra, frecuencia in palabras.items():
        if frecuencia > max_frecuencia:
            max_palabra = palabra
            max_frecuencia = frecuencia
    return max_palabra, max_frecuencia

#print(contador_palabras(texto))
print(f"La palabra mas repetida con su frecuencia es {palabra_mas_repetida(contador_palabras(texto))}")


