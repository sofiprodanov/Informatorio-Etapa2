def saludar ():
    return "Hola Mundo!"

print(saludar())


#PARAMETROS
def sumar (a, b):
    return a + b

resultado = sumar(3, 4)
print(f"El resultado es: {resultado}")


#TIPO DE PARAMETRO> *ARGS
def saludar(nombre, mensaje = "Hola"):
    return f"{mensaje} {nombre}!"

def receta_de_cocina(titulo, *args):
    print(f"Receta de {titulo}")
    print("Ingredientes")

    for ingredientes in args:
        print(ingredientes)


#TIPO DE PARAMETRO> *ARGS
def suma(**kwargs):
    resultado = 0

    for clave, valor in kwargs.items():
        print(clave, "=", valor)
        resultado += valor
    
    return resultado



#RETORNO DE VALORES
def es_par(numero):
    return numero % 2 == 0

print(es_par(4))


def operaciones(a, b):
    suma = a + b
    resta = a - b

    return suma, resta

print(operaciones(5, 3))

resultado_suma, resultado_resta = operaciones(5, 3)
print(f"El resultado de la suma es: {resultado_suma}")
print(f"El resultado de la resta es: {resultado_resta}")



#MODULARIDAD
def leer_datos():
    #codigo para leer tados
    pass

def procesar_datos():
    #codigo para leer tados
    pass

def guardar_datos():
    #codigo para leer tados
    pass

leer_datos()
procesar_datos()
guardar_datos()



#FACILIDAD DE PRUEBAS
def multiplicar(a, b):
    return a * b

#Prueba de la funcion
#assert os ayuda a verificar si una condicion es verdadera. En caso de que sea falsa nos retorna un error en la terminal.
assert multiplicar(2, 3) == 6
assert multiplicar(0, 3) == 0



#VARIABLES LOCALES
# def mi_funcion():
#     x = 10
#     print(x)

# mi_funcion()
# print(x)

#VARIABLES GLOBALES
x=10

def mi_funcion():
    print(x)

mi_funcion()
print(x)