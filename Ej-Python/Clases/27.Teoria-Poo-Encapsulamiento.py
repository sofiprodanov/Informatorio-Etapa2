class Abuelo():
    atributo = "de clase" #ATRIBUTO DE CLASE
    _atributo = "Este es un atributo de clase, protegido." #ATRIBUTO PROTEGIDO - se pone un guion bajo delante del atributo
    __atributo = "Este es un atributo de clase, privado." #ATRIBUTO PRIVADO - dos guiones bajo

    def __init__(self, nombre):
        self.nombre = nombre
        #self._nombre = "Este es un atributo de instancia protegido."
        #self.__nombre = "Este es un atributo de instancia privado."
    
    def saludar(self):
        print("Cuando saludo, paso la mano.")
    
    def construir_casas(self):
        print("Puedo construir casas tradicionales de ladrillo y cemento.")


class Abuela():
    pass

    def saludar(self):
        print("Cuando saludo, doy un abrazo.")
    
    def construir_casas(self):
        print("Puedo pintar casas con rodillo y pincel.")

class Padre(Abuela, Abuelo):
    pass

class Hijo(Padre):
    pass


# hijo = Hijo()
# hijo.pintar_casas()
# hijo.construir_casas()
# hijo.saludar()


Abuelo.atributo = "cambiando el valor" #ATRIBUTO DE CLASE: accedemos al que habiamos creado sin tener que instanciar un objeto nuevo y le asignamos un nuevo valor.
print(Abuelo.atributo)
print(Padre.atributo)
print(Hijo.atributo)

objeto1 = Hijo(None) #PARA EJ ATRIBUTO DE CLASE
print(objeto1.atributo)

print(Abuelo._atributo) #ATRIBUTO PROTEGIDO
objeto = Hijo(None)
print(objeto._nombre)

# print(Abuelo.__atributo) #ATRIBUTO PRIVADO - al acceder al mismo dara error
# objeto = Hijo(None)
# print(objeto.__nombre) #ATRIBUTO PRIVADO

# print(Abuelo._Abuelo__atributo) #ATRIBUTO PRIVADO - para poder acceder correctamente
# objeto = Hijo(None)
# print(objeto._Abuelo__nombre) #ATRIBUTO PRIVADO