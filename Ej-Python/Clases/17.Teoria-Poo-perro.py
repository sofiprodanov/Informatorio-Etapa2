class Perro ():
    def __init__(self, nombre, raza, poder):
        self.nombre = nombre
        self.raza = raza
        self.poder = poder

catdog = Perro("CatDog", "Teckel", "Super elasticidad")
print(catdog.nombre)
print(catdog.raza)
print(catdog.poder)