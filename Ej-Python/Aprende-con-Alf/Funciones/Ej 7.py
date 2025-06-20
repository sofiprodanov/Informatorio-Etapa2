#Escribir una función que reciba una muestra de números en una lista y devuelva otra lista con sus cuadrados.

def lista_al_cuadrado(lista_numeros):
    lista = []
    for i in lista_numeros: #para i dentro de la lista de numeros
        lista.append(i**2)
    return lista

print(f"El cuadrado de cada uno de los numeros es {lista_al_cuadrado([1, 2, 3.3, 4])}") #Brindo la lista de numeros por eso va entre []