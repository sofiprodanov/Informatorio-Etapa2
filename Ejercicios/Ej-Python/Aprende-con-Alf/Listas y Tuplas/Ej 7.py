#Escribir un programa que almacene el abecedario en una lista, elimine de la lista las letras que ocupen posiciones múltiplos de 3, y muestre
#por pantalla la lista resultante.

abecedario = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "ñ", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for i in range(len(abecedario), 1, -1): #(-1) Vamos decrementando de 1 en 1. Al eliminar elementos desde el final, no afectamos las posiciones de los elementos que quedan por procesar.
    if i % 3 == 0:
        abecedario.pop(i-1) #Elimina el elemento en la posición i-1 (ya que los índices de lista comienzan en 0). Usamos i-1 porque el bucle va desde 1 hasta len(alphabet), pero los índices de la lista van desde 0.
print(abecedario)
#El resultado final será el abecedario sin las letras que originalmente estaban en las posiciones 3, 6, 9, etc. (considerando que Python indexa desde 0).