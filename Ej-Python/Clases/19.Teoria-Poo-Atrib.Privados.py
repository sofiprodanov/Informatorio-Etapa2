class Punto:
    def __init__(self, x, y):
        #Atributos "privados" para seguir que no deben modificarse directamente
        self._x = x
        self._y = y
    
    @property
    def x(self):
        return self._x
    
    @property
    def y(self):
        return self._y
    

    # La inmutabilidad es una característica donde el estado de un objeto no puede cambiar después de su creación. En Python, los objetos inmutables
    # incluyen tipos como int, float, str, y tuple.
    def __str__(self):
        return f"Punto({self.x}, {self.y})"

#Crear un objeto de la clase Punto
p = Punto(3, 4)

#Acceder a sus atributos
print(p.x) #3
print(p.y) #4

#Intentar modificar los atributos lanzara un error
#p.x = 10 > Esto generara un error de atribucion
