#DECORADORES: permiten modificar el comportamiento de una función o método existente sin modificar su implementación original.

class Persona():
    def __init__(self, nombre, edad):
        self._nombre = nombre
        self._edad = edad
    
    @property
    def nombre(self):
        return self._nombre
    
    @property
    def edad(self):
        return self._edad

    @edad.setter
    def edad(self, nueva_edad):
        if nueva_edad > 0:
            self._edad = nueva_edad


persona = Persona("Info", 11)
print(persona.nombre)
print(persona.edad)

persona.edad = 11
print(persona.edad)

persona.edad = -5
print(persona.edad) #No se actualiza la edad porque no es valida