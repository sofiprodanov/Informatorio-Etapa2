#Escribir una función que reciba una muestra de números en una lista y devuelva su media.

def promedio(lista):
    calculo = sum(lista)/len(lista)
    return calculo

print(f"El promedio es {promedio([1, 4, 5,  6, 7.5, 8])}.")
