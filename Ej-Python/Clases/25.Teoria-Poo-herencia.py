class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
    
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

class Estudiante(Persona):
    def __init__(self, nombre, edad, grado):
        super().__init__(nombre, edad)
        self.grado = grado
    
    def estudiar(self):
        print(f"{self.nombre} esta estudiando en el grado {self.grado}.")
    
    def saludar(self):
        print(f"Hola, soy {self.nombre} y soy un estudiante de {self.grado}.")


persona1 = Persona("Wanda", 26) #Hola, mi nombre es Wanda y tengo 26 años.
persona1.saludar()
estudiante1 = Estudiante("Informatorio", 12, "A") #Hola, soy Informatorio y soy un estudiante de A.
estudiante1.saludar()

#super().__init__(nombre, edad) > forma de acceder y usar métodos y atributos de clases principales, o padres o como también podemos llamarlas, superclases.