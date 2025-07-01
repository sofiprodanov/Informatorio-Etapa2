class Libro:
    def __init__(self, titulo, autor, ISBN, numero_paginas, genero):
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.__numero_paginas = numero_paginas
        self.genero = genero

    def __prestar(self):
        pass

    def devolver(self):
        pass

    def buscarPorTitlo(self):
        pass

class Autor:
    def __init__(self, nombre, nacionalidad, fecha_nacimiento):
        self.nombre = nombre
        self.nacionalidad = nacionalidad
        self.fecha_nacimiento = fecha_nacimiento

    def publicarLibro(self):
        pass

class Lector:
    def __init__(self, nombre, edad, direccion, numero_socio):
        self.nombre = nombre
        self.direccion = direccion
        self.numero_socio = numero_socio

    def solicitarPrestamo(self):
        pass

    def devolverLibro(self):
        pass

class Libreria:
    def __init__(self, libros, autores, lectores):
        self.libros = libros
        self.autores = autores
        self.lectores = lectores
    
    def agregarLibro(self):
        pass

    def buscarLibro(self):
        pass

    def prestarLibro(self):
        pass

    def devolverLibro(self):
        pass

    def registrarLector(self):
        pass

class Libroinfantil(Libro):
    def __init__(self, titulo, autor, ISBN, numero_paginas, genero):
        super().__init__(self, edad, recomendada, ilustraciones)
        self.titulo = titulo
        self.autor = autor
        self.ISBN = ISBN
        self.__numero_paginas = numero_paginas
        self.genero = genero

    def __prestar(self):
        pass

    def devolver(self):
        pass

    def buscarPorTitlo(self):
        pass