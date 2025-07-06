#Realizá un programa en Python que permita al usuario ingresar 10 números enteros. El programa debe:
#1. Almacenar los números ingresados en una lista.
#2. Calcular la suma de todos los números pares.
#3. Contar cuántos números impares se ingresaron.
#4. Mostrar por pantalla:
#5. La lista completa de números ingresados.
#6. La suma de los números pares.
#7. La cantidad de números impares

#Consigna 1:
numeros = []
cantidad_pares = 0
cantidad_impares = 0

for i in range(10): #recorre 10 veces el bucle pidiendo 10 veces numeros
    num = int(input("Ingrese un numero: "))
    numeros.append(num)

for numero in numeros:
    if numero % 2 == 0: #si el numero del resto (%) de la division por 2 es igual a cero
        cantidad_pares += 1
    else:
        cantidad_impares += 1

print("La lista es: ", numeros)
print("La cantidad de numeros pares que hay es: ", cantidad_pares)
print("La cantidad de numeros impares que hay es: ", cantidad_impares)






