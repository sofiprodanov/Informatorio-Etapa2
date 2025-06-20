class Usuario:
    def __init__(self, nombre, email):
        self.nombre = nombre
        self.email = email
    
    def mostrar_info(self):
        print(f"Usuario: {self.nombre}, Email: {self.email}")
    
class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
    
    def mostrar_info(self):
        print(f"Usuario: {self.nombre}, Precio: {self.email}")

#La POO fomenta la creación de programas modulares, donde cada clase representa una unidad de funcionalidad que puede ser desarrollada, probada y
# mantenida de manera independiente.
