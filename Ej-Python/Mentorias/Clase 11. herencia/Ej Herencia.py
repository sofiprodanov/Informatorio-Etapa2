class Persona: #clase padre
    def __init__(self, nombre, apellido): #constructor
        self.nombre = nombre
        self.apellido = apellido
    
    def nombre_completo(self):
        return f"Su nombre completo es: {self.nombre} {self.apellido}"
    

class Estudiante(Persona): #para vincularlo con la clase que hereda, es decir, clase padre
    def __init__(self, nombre, apellido, carrera): #con el constructor hereda los atributos: nombre y apellido y se agrega el atributo carrera
        super().__init__(nombre, apellido) #super permite pasar los valores de su clase padre a clase hijo. init llama nuevamente al constructor
        self.carrera = carrera #el atributo se crea solo para la clase estudiante

    def getCarrera(self):
        return f"Esta estudiando la carrera de {self.carrera}"


persona1 = Persona("Sofia", "Prodanov") #se instancia/crea el objeto con las caracteristicas ya definidas.
print(persona1.nombre_completo()) #se llama al metodo nombre completo

estudiante1 = Estudiante("Nadia", "Prodanov", "Tecnicatura en Programacion")
print(estudiante1.nombre_completo())
print(estudiante1.getCarrera())