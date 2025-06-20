#Escribir un programa que almacene en una lista los siguientes precios 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.

precios = [50, 75, 46, 22, 80, 65, 8]

print(f"El menor precio es {min(precios)}")
print(f"El mayor precio es {max(precios)}")


#OTRA SOLUCION
#precios = [50, 75, 46, 22, 80, 65, 8]
#min = max = precios[0]
#for precio in precios:
#    if precio < min:
#        min = precio
#    elif precio > max:
#        max = precio 
#print(f"El minimo es {min}") 
#print(f"El maximo es {max}")