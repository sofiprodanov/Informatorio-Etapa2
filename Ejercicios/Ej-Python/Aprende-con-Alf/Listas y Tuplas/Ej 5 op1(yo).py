#Escribir un programa que almacene en una lista los números del 1 al 10 y los muestre por pantalla en orden inverso separados por comas.
numeros = []
for i in range(10):
    num = int(input("Ingresa un numero entero: "))
    numeros.append(num)

numeros.sort(reverse= True)
print(numeros)