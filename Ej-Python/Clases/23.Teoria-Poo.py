#PROGRAMACION ESTRUCTURADA
#Funcion para calcular el area de un circulo
def calcular_area_circulo(radio):
    area = 3.14 * radio * radio
    return area

#Funcion para imprimir el resultado
def imprimir_resultado(area):
    print(f"El area del circulo es: {area}")

#Llamada a las funciones
radio = 5
area_circulo = calcular_area_circulo(radio)
imprimir_resultado(area_circulo)



#POO
#Clase Circulo
class Circulo:
    def __init__(self, radio):
        self.radio = radio
    
    def calcular_area(self):
        area = 3.14 * self.radio * self.radio
        return area
    
    def imprimir_resultado(self, area):
        print(f"El area del circulo es: {area}")

#Creacion de objeto y llamada a metodos
radio = 5
circulo = Circulo(radio)
area_circulo = circulo.calcular_area()
circulo.imprimir_resultado(area_circulo)