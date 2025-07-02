edad = int(27) #int
print(f"Edad:{edad}, tipo:{type(edad)}")

altura = 1.17 #float
print(f"Altura: {altura}, tipo:{type(altura)}")

z = 245j #numeros complejos - complex
print(f"Complejo: {z}, Tipo: {type(z)}")

cadena = "Juan" #str
print(f"Nombre: {cadena}, Tipo: {type(cadena)}")

verdadero = True #booleano
print(f"Bool: {verdadero}, Tipo: {type(verdadero)}")

valor = None #Nonetype
print(f"None: {valor}, Tipo: {type(valor)}")

empty_string = "" #str
print(f"None: {empty_string}, Tipo: {type(empty_string)}")

infinito = float("inf")
print(f"None: {infinito}, Tipo: {type(infinito)}")

nan = float("nan")
print(f"Not a number: {nan}, Tipo: {type(nan)}")


#Lista(arrys) > coleccion de elementos ordenados y mutables
lista = ["algo", 17, 0.5, ["otra lista", True]] #list, dentro de la lista hay otra sublista y otros elementos
print(f"Listas: {lista}, Tipo: {type(lista)}")

#Tupla(tuple) > coleccion de elementos ordenados, inmutables y tiene una longitud fija (no se puede agregar ni eliminar elementos)
tupla = (10.5, 48,5) #por ej latitud y longitud de google maps
print(f"Tuple: {tupla}, Tipo: {type(tupla)}")

#Set > Coleccion de elementos unicos (no se puede repetir), y no tiene un orden definido, si son mutables
colores = {"azul", "rojo", "verde", "azul"}
print(colores)
print(f"Set: {colores}, Tipo: {type(colores)}")

#diccionarios(mapas) > es una coleccion de elementos que tienen pares clave-valor(key-value)
estudiante = {
    #clave: valor
    #key: value
    "nombre": "Daniel",
    "edad": 23,
    "curso": "PW",
        "nombre": "Programacion Web",
        "iniciales": ["PW", "WP"]
    }
print(f"Set: {colores}, Tipo: {type(colores)}")

estudiante["curso"]["iniciales"][0] = "Python" #para cambiar un valor














