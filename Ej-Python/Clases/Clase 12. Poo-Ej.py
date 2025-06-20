# class Vehiculo:
#     def __init__(self, param_marca, param_modelo, param_estado): #primer constructor > init, self > metodo de instancia (parametros)
#         self.marca = param_marca #se definen los atributos > atributo (self.marca) = parametro (marca) // ATRIBUTO PUBLICO
#         self.modelo = param_modelo #ATRIBUTO PUBLICO
#         self.estado = param_estado #ATRIBUTO PUBLICO
 
#     def mostrar_informacion(self): #creo un metodo propio, metodo de instancia
#         print(f"Marca: {self.marca}\nModelo: {self.modelo}\nEstado: {self.estado}")


# v = Vehiculo("Toyota", "Yaris", "Excelente") #instancio un vehiculo

# v.mostrar_informacion() #ejecuto



class Vehiculo:
    #METODO DE CLASE > no se llama a ella misma (self)
    contador_vehiculo = 0 #atributo decorativo de clase, puede ser __privado, _protegido, publico.

    #LOS DEF SON METODOS DE INSTANCIA > siempre manda la instancia propia del metodo
    def __init__(self, param_marca, param_modelo, param_estado): #primer constructor > init, self > metodo de instancia (parametros)
        #ATRIBUTO DE INSTANCIA
        self.marca = param_marca #se definen los atributos > atributo (self.marca) = parametro (marca) // ATRIBUTO PUBLICO
        self.modelo = param_modelo #ATRIBUTO PUBLICO
        self._estado = param_estado #ATRIBUTO PROTEGIDO
        self.__id_vehiculo = Vehiculo.contador_vehiculo + 1 #ATRIBUTO PRIVADO (creado como ej)

        Vehiculo.contador_vehiculo += 1

    def __str__(self):
        return (f"Marca: {self.marca} Modelo: {self.modelo} ID: {self.__id_vehiculo}")

    def mostrar_informacion(self): #creo un metodo propio, metodo de instancia
        print(f"Marca: {self.marca}\nModelo: {self.modelo}\nEstado: {self._estado}")
    
    #Defino getter si quiero que se pueda acceder en publico. Luego el set
    def get_estado(self): 
        return self._estado
    
    def set_estado(self, nuevo_estado): #defino con set el estado para que se pueda acceder publicamente
        self._estado = nuevo_estado

    def get_id_vehiculo(self):
        return self.__id_vehiculo
    
    #Cuando se define en un metodo ya no es necesario el getter y setter. Ej.
    def _realizar_inspeccion(self): #PROTEGIDO
        print(f"Realizar inspeccion: {self.__id_vehiculo}") #el id vehiculo se usa dentro de la clase vehiculo
    
    def __registrar_en_sistema(self): #PRIVADO
        print(f"Registrando en sistema el vehiculo: {self.__id_vehiculo}")

    #DECORADORES
    @classmethod #INDICAMOS QUE ES UUN METODO DE CLASE PARA PODER EJECUTARLO SOLO (DECORADOR - funcion que envuelve a funcion)
    def get_contador_vehiculo(cls): #no se va a poder ejecutar solo porque no esta en el constructor, esta en la clase (atrib de clase)
        return cls.contador_vehiculo #queda implicito un return None si no se le asigna un return a devolver
    
    @staticmethod #no recibe cls ni self, es un metodo estatico, no depende de la clase ni instancia.
    def calcular_costos_reparacion(hs_trabajo, tarifa_hs):
        return hs_trabajo * tarifa_hs


    
# auto = Vehiculo("Toyota", "Yaris", "Excelente") #instancio un vehiculo
# print(auto) #Metodo __str__, comportamiento de como quiero que se vea cuando se ejecuta

# auto2 = Vehiculo("Ford", "Ranger", "Bueno")
# print(auto2)

#METODO DE CLASE CONTADOR
# auto2 = Vehiculo("Fiat", "Cronos", "Perfecto")
# print(auto2.get_contador_vehiculo())
# print(Vehiculo.get_contador_vehiculo())
#auto.mostrar_informacion() #ejecuto

#STATICMETHOD
# print(auto2.calcular_costos_reparacion(3, 5000))


#el atrib. protegido se puede usar solo dentro de la clase o subclase, no por fuera. Pero no va a dar error si lo usamos por fuera
#el atrib. privado se puede usar solo dentro de la clase vehiculo, no por fuera ni en subclases


#ej atrib protegido
# print(auto._estado) #no es correcto
# print(auto.get_estado()) #es lo correcto


#ej atrib privado: cuando se le agrega un doble guion adelante, es como si python cambiara el nombre para que no lo encuentra
#print(auto._Vehiculo__id_vehiculo) #si agregamos_Vehiculo podemos ver que al ejecutar nos aparece el contenido pero NO ES CORRECTO

#No hay un encapsulamiento estricto para que no se pueda acceder directamente


