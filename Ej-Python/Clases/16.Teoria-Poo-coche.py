class Coche:
    ruedas = 4

    #Constructor
    def __init__(self, marca, modelo, color): #metodo constructor
        #Atributos
        self.marca = marca
        self.modelo = modelo
        self.color = color
    
    #Metodo de instancia
    def acelerar(self):
        print(f"El {self.marca} {self.modelo} esta acelerando.")

    #Metodo de instancia
    def acelerar(self):
        print(f"El {self.marca} {self.modelo} esta acelerando.")
    
    #Metodo de clase
    @classmethod
    def incrementar_ruedas(cls):
        cls.ruedas += 1
    
    #Metodos estaticos
    @staticmethod
    def calcular_distancia(velocidad, tiempo):
        """Calcula una distancia recorrida dadas la velocidad y el tiempo"""
        return velocidad * tiempo

#Crear un objeto de la clase Coche
mi_coche = Coche("Toyota", "Corolla", "Roja")
otro_coche = Coche("Ford", "Ranger", "Azul")

#Acceder al estado de los atributos directamente
print("Atributos del primer coche: ")
print(mi_coche.marca) #Toyota
print(mi_coche.modelo) #Corolla
print(mi_coche.color) #Rojo
print(mi_coche.ruedas) # 4

print("Atributos del segundo coche: ")
print(otro_coche.marca) #Ford
print(otro_coche.modelo) #Ranger
print(otro_coche.color) #Azul
print(otro_coche.ruedas) # 4

#METODO DE INSTANCIA
mi_coche.acelerar() #El Toyota Corolla esta acelerando.
mi_coche.frenar() #El Toyota Corolla esta acelerando.

otro_coche.acelerar() #El Ford Ranger esta acelerando.
otro_coche.frenar() #El Ford Ranger esta acelerando.


print(mi_coche.ruedas) #4

#METODO DE CLASE:
Coche.incrementar_ruedas()
print(mi_coche.ruedas) #5

#METODOS ESTATICOS
print(Coche.calcular_distancia(88, 2)) #160