#Consigna:
#Pedir un número al usuario. Mostrar un mensaje que diga si el número es positivo, negativo o cero.


number = float(input("Ingrese un numero: "))

if number > 0:
    print("El numero es positivo.")
elif number < 0:
	print("El numero es negativo.")
else: 
    print("El numero es cero.")


