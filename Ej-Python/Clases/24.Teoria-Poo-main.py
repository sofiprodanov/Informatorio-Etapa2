class Persona:
    def __init__(self, nombre, edad):
        self.nombre = "Wanda"
        self.edad = 26
    
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")


persona1 = Persona("Wanda", 26)
persona1.saludar()
print(type(persona1)) #<class ‘__main__.Persona’>

#__main__, que nos indica que esta clase (Persona en este caso) se definió dentro del módulo principal “main” o pertenece al módulo principal.