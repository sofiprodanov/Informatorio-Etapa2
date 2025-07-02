class Vehiculos: #Pascal case
    def __init__(self, param_marca, param_modelo, param_estado, param_color): #constructor, self siempre tiene que ir
        self.marca = param_marca
        self.modelo = param_modelo
        self.estado = param_estado
        self.color = param_color

    def mostrar_info(self):
        print(f"Tengo un/a {self.marca} - {self.modelo} en un estado {self.estado} de color {self.color}")

class Auto(Vehiculos):
    def __init__(self, param_marca, param_modelo, param_estado, param_color, param_numero_puertas, param_motor, param_tipo_combustible):
        super().__init__(param_marca, param_modelo, param_estado, param_color)
        self.numero_puertas = param_numero_puertas
        self.tipo_combustible = param_tipo_combustible
        

#instancia
moto = Vehiculos("Honda", "Tornado CRF", "Excelete", "Rojo")
auto = Vehiculos("Toyota", "Yaris GR", "Impecable", "Negro")
camion = Vehiculos("Mercedes", "1114", "Se defiende", "Blanco")

# camion.mostrar_info()
# moto.mostrar_info()
# auto.mostrar_info()


mis_vehiculos = [moto, auto, camion]

for v in mis_vehiculos:
    v.mostrar_info()