class Persona():
    def __init__(self, nombre):
        self.nombre = nombre
    
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")

class Empleado():
    def __init__(self, nombre, puesto):
        self.nombre = nombre
        self.puesto = puesto
    
    def saludar(self):
        print(f"El puesto en el que me desempeño es el de {self.puesto}.")

class Profesor(Persona, Empleado):
    def __init__(self, nombre, puesto, antiguedad):
        Persona.__init__(self, nombre)
        Empleado.__init__(self, nombre, puesto)
        self.antiguedad = antiguedad
    
    def saludar(self):
        Persona.saludar(self)
        Empleado.saludar(self)
        print(f"Estoy en este puesto hace {self.antiguedad} años.")

profesor1 = Profesor("Informatorio", "profesor", 11)
profesor1.saludar()

#La clase “Profesor” hereda tanto de “Persona” como de “Empleado”. Aunque la clase “Profesor” tiene su propio método “saludar”, también estamos heredando
#el método “saludar” de las clases padre que hemos incluido.


#---------------------------------------------------------
class Persona():
    def __init__(self, nombre):
        self.nombre = nombre
    
    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre}")

class Empleado():
    def __init__(self, nombre, puesto):
        self.nombre = nombre
        self.puesto = puesto
    
    def saludar(self):
        print(f"El puesto en el que me desempeño es el de {self.puesto}.")

class Profesor(Persona, Empleado):
    def __init__(self, nombre, puesto, antiguedad):
        Persona.__init__(self, nombre)
        Empleado.__init__(self, nombre, puesto)
        self.antiguedad = antiguedad
    
    def saludar(self):
        print(f"Estoy en este puesto hace {self.antiguedad} años.")

profesor1 = Profesor("Informatorio", "profesor", 11)
profesor1.saludar()

#Si no se especifica la inclusión de los métodos “saludar()” de las clases anteriores, como en el ejemplo anterior donde se incluyeron los métodos de las
#clases padres y, por lo tanto, se mostraron los tres métodos en pantalla, solo se mostrará el mensaje de la clase hija “Profesor” al llamar al método 
#“saludar()”. Los mensajes de las clases padres con el mismo nombre no se mostrarán. 