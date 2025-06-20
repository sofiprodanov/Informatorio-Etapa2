class Coche:
    def __init__(self, marca, consumo_por_km):
        self.marca = marca
        self.consumo_por_km = consumo_por_km
    
    def calcular_consumo(self, distancia):
        return self.consumo_por_km * distancia
#Podés modificar el metodo correspondiente sin afectar a las demás clases o funciones del programa.
