class Punto:
    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y
    def __add__(self, parametro):
        x = self.x + parametro.x
        y = self.y + parametro.y
        return x, y

punto1 = Punto(4, 6)
punto2 = Punto(1, 2)
print(punto1 + punto2)

#__add__: sobrecarga el operador de suma (+).
# __sub__: sobrecarga el operador de resta (-).
# __mul__: sobrecarga el operador de multiplicación (*).
# __div__: sobrecarga el operador de división (/).
# __eq__: sobrecarga el operador de igualdad (==).
# __lt__: sobrecarga el operador de menor que (<).