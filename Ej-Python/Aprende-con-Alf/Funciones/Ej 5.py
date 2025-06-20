#Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.
from math import pi

def calculo_area(r):
    area = pi * r**2 #pi * radio al cuadrado
    print(f"El area del circulo es {area}.")
    return area

def calculo_volumen(r, altura):
    volumen = calculo_area(r)*altura
    print(f"El volumen del cilindro es {volumen}.")
    return volumen

calculo_volumen(3, 5)