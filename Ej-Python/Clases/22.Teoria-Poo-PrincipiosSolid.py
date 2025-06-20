#1. PRINCIPIO DE RESPONSABILIDAD UNICA (SRP): Una clase debe tener una sola responsabilidad o razón para cambiar. 
class Pedido:
    def calcular_total(self):
        pass #Logica para calcular el total del pedido

class ImpresoraDePedidos:
    def imprimir(self, pedido):
        pass #Logico para imprimir el pedido

#Aplicado SRP dividimos la clase en dos:
class Pedido:
    def calcular_total(self):
        pass #Logica para calcular el total del pedido

    def imprimir_pedido(self):
        pass #Logico para imprimir el pedido



#2. PRINCIPIO DE ABIERTO/CERRADO (OCP): . Esto significa que el comportamiento de una entidad debe poder extenderse sin modificar su código fuente.
class CalculadoraDeSalarios:
    def calcular(self, empleado):
        if empleado.tipo == "comisionado":
            return empleado.ventas * 0.10
        elif empleado.tipo == "asalariado":
            return empleado.salario_fijo

#Aplicado OCP, utilizamos herencia o composición para extender el comportamiento sin modificar el código existente:
class CalculadoraDeSalarios:
    def calcular(self, empleado):
        return empleado.calcular_salario()

class EmpleadoComisionado:
    def calcular_salario(self):
        return self.ventas * 0.10

class EmpleadoAsalariado:
    def calcular_salario(self):
        return self.salario_fijo



#3. PRINCIPIO DE SUSTITUCION DE LISKOV (LSP): Los objetos de una clase derivada deben poder sustituir a los objetos de su clase base sin alterar el 
#funcionamiento del programa. 
#Las clases Perro y Gato pueden sustituir a Animal sin problemas, ya que cumplen con el comportamiento esperado.

class Animal:
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Ladra"

class Gato(Animal):
    def hacer_sonido(self):
        return "Maulla"



#4. PRINCIPIO DE SEGREGACION DE INTERFACES (ISP): Los clientes no deben estar forzados a depender de interfaces que no utilizan. Es mejor tener varias
#interfaces pequeñas y específicas que una sola interfaz grande y genérica.
class Vehiculo:
    def encender(self):
        pass

    def volar(self):
        pass

    def navegar(self):
        pass

#Aplicando ISP, dividimos la interfaz en varias más específicas:
class Vehiculo:
    def encender(self):
        pass

class Avion(Vehiculo):
    def volar(self):
        pass

class Barco(Vehiculo):
    def navegar(self):
        pass



#5. PRINCIPIO DE INVERSION DE DEPENDENCIAS (DIP): Las clases de alto nivel no deben depender de clases de bajo nivel. Las abstracciones no deben
#depender de detalles; los detalles deben depender de abstracciones.
class Television:
    def encender(self):
        pass

class ControRemoto:
    def __init__(self, tv):
        self.tv = tv
    
    def presionar_boton(self):
        self.tv.encender()

#Aplicando DIP, usamos una abstracción para eliminar la dependencia directa:
class Dispositivo:
    def encender(self):
        pass

class Television(Dispositivo):
    def encender(self):
        pass

class ControlRemoto:
    def __init__(self, dispositivo):
        self.dispositivo = dispositivo

    def presionar_boton(self):
        self.dispositivo.encender()

