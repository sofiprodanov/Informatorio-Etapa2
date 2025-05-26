#Escribir un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos tuplas y muestre por pantalla su producto escalar.

#Para poder hacer la operacion deben tener la misma dimension

vector1 = (1, 2, 3) #dimension 1x3 (fila primero dps columna)
vector2 = (-1, 0, 2) #dimension 1x3

producto = 0

if len(vector1) == len(vector2): #evalua que los vectores tengan la misma dimension
    for i in range(len(vector1)):
        producto += (vector1[i] * vector2[i])

print(f"El resultado del producto de los vectores {vector1} y {vector2} es {producto}.")