class Circulo:
    def __init__(self, radio):
        self.radio = radio
        self.__pi = 3.1415

    def calcularPerimetro(self):
        return 2 * self.pi * self.radio
    
    def calcularArea(self):
        return self.pi * self.radio**2
    
    def getPi(self, nuevoValorPi):
        if type(nuevoValorPi) == int or type(nuevoValorPi) == float:
            if nuevoValorPi > 0:
                self.__pi = nuevoValorPi
                print(f"El nuevo valor de Pi es: {self.__pi}") #correcto para atrib privado
            else:
                print("Pi no puede ser negativo")
        else:
            print("El valor debe ser un numero")

    def __prueba(self):
        return f"Esto es un metodo privado"


circulo_uno = Circulo(3.5)

print(circulo_uno.calcularArea())
print(circulo_uno.calcularPerimetro())
# print("El valor de PI en la clase es {circulo_uno.pi}")

# circulo_uno.pi = "Pizza"
# print(f"El nuevo valor de Pi en la clase es {circulo_uno.pi}")

# print(circulo_uno.__dict__) > verificar que atributos son privados y cuales no

print(circulo_uno.getPi()) #correcto para atrib privado

circulo_uno.getPi(4.6)
circulo_uno.getPi(-5)
circulo_uno.getPi("Hola")

circulo_uno.__prueba() #metodo privado usado fuera de la clase da error