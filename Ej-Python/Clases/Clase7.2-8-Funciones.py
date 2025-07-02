# def saludo(nombre): #parametro
#     print(f"Hola {nombre}")

# saludo("Pablo") #argumento
# saludo("Elias")
# saludo("Edu")


# notas = [10, 5, 7, 8]
# suma = 0

# for nota in notas:
#     suma += nota

# promedio = suma / len(notas)

# print (suma)

# print(f"Suma: {suma}")
# print(f"Cantidad de notas: {len(notas)}")
# print(f"Promedio: {promedio}")


# def promedio(notas):
#     return sum(notas) / len(notas)

# promedio_pablo = promedio([5, 6, 8, 9])
# promedio_juan = promedio([10, 5, 6, 9])

# print(f"Promedio Pablo: {promedio_pablo}")
# print(f"Promedio Juan: {promedio_juan}")

#################################

# variable_global = 10

# # def prueba():
# #     print(variable_global)

# # prueba()
# # print(variable_global)

#################################

# def prueba():
#     contador(20)
#     print(contador)

# contador = 0
# contador = 10

# def prueba ():
#     global contador #para definir de manera global fentro de la funcion
#     contador = 20 #define de manera local en la funcion
#     print(contador)

# prueba()
# print(contador)

#################################

# def suma(num1, num2, num3):
#     return num1 + num2, num3

# resultado = suma(10, 10, 10)
# print(f"El resultado es: {resultado}")

#################################
# *args: permiten pasar a una funcion un numero variable indeterminado de argumentos posicionales.

# def suma(*numeros):
#     print(numeros)
#     print(type(numeros)) #nos devuelve una tupla

#     resultado = 0
#     for n in numeros:
#         resultado += n

#     return resultado

# resultado = suma(10, 10, 20, 50)
# print(f"El resultado es: {resultado}")

#################################
# **kwargs > permiten pasar a una funcion un nro variable/indeterminado de argumentos con nombre (calve-valor).

# def ver_persona(**kwargs):
#     print(kwargs)
#     print(type(kwargs))

#     for clave, valor in kwargs.items():
#         print(f"Clave: {clave}, valor: {valor}")

# ver_persona(nombre = "Juan", edad = 25, ciudad = "Resistencia")

#################################
#ORDEN: 1) valores indeterminados posicionales(sin nombre), 2) determinados posicionales, 3)nombrados determinados/definidos, 4)nombrados indeterminados. 

def mostrar_info(*args, nombre, edad = 0, **kwargs):
    print(f"Posicionales indeterminados: {args}")
    print(f"Posicionales determinados: {nombre}")
    print(f"Nombrados determinados: {edad}")
    print(f"Nombrados indeterminados: {kwargs}")

mostrar_info(50, True, "algo", nombre="Pablo", edad=28, ciudad="Resis")