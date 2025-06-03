#Escribir una función que calcule el área de un círculo y otra que calcule el volumen de un cilindro usando la primera función.

def calculo_area(r):
    pi = 3.14

    area = pi * r**2 #pi * radio al cuadrado
    print(f"El area del circulo es {area}.")
    return area

calculo_area(425)

def calculo_volumen(r, altura):
    return calculo_area(r) * altura

