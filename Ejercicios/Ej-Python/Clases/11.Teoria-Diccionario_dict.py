diccionario = {"Juan": 24, "Ana": 30, "Cristian": 28}
print(diccionario)
print(diccionario["Juan"])

#Modificacion de valor
diccionario1 = {"Juan": 24, "Ana": 30, "Cristian": 28}
diccionario1["Ana"] = 18
print(diccionario1)

#OTRA FORMA DE CREAR DICCIONARIOS
#Con la funcion dict()
una_lista = [("clave1", "valor1"), ("clave2", "valor2"), ("clave3", "valor3")]
un_diccionario = dict(una_lista)
print(un_diccionario)
print(type(un_diccionario))

#o usando sintaxis de argumentos de palabras claves para especificar las claves y los valores
mi_diccionario = dict(clave1 ="valor1", clave2 = "valor2", clave3 = "valor3")
print(mi_diccionario)
print(type(mi_diccionario))

#METODOS PARA DICCIONARIOS
# clear() elimina todos los elementos del diccionario
# copy() devuelve una copia superficial del diccionario
# get() devuelve el valor asociado a una clave dada, o un valor predeterminado
# items() devuelve una vista de lista de todos los pares clave-valor en el diccionario
# keys() devuelve una vista de lista de todas las claves en el diccionario
# pop() elimina y devuelve el valor asociado a una clave dada
# popitems() elimina y devuelve un par clave-valor aleatorio del diccionario
# setdefault() devuelve el valor asociado a una clave dada, o lo crea con un valor predeterminado si la clave no esta presente
# update() actualiza el diccionario con los pares clave-valor de otro diccionario o iterable
# values() devuelve una vista de lsita de todos los valroes en el diccionario

#EJEMPLO POWERPOINT
diccionario = {"pais": "Argentina",
               "provincia": "Chaco",
               "ciudad": "Resistencia",
               "cp": "3500"
               }
print(diccionario)
print(diccionario["pais"]) #accedemos al valor
diccionario["departamento"] = "San Fernando" #agregar un par clave valor a un diccionario
print(diccionario)

curso = {"nombre": "Info", #si queremos modificar un valor llamamos a su clave y asignamos el nuevo valor
         "etapa": 1} 
print(curso)
curso["etapa"] = 2
print(curso)


#podemos verificar si una clave se encuentra en un diccionario, usando condicional:
curso = {"nombre": "Info",
         "etapa": 2}

if "nombre" in curso:
    print("La clave 'nombre' se encuentra en el diccionario.")
else:
    print("La clave 'nombre' NO se encuentra en el diccionario.")

#Tambien podemos usar bucle flor:
curso = {"nombre": "Info",
         "etapa": 2}

for clave, valor in curso.items():
    print(f"Clave: {clave}. Valor: {valor}.")

#La funcion ".items()" sirve para ver los items que conforman al diccionario.
#"f-string" es una forma de mostrar resultados encerrando entre llaves las variables.

variable = "Informatorio"
print(f"Bienvenido al {variable}.")

#Para obtener las claves o valores:
curso = {"nombre": "Info",
         "etapa": 2}

claves = list(curso.keys())
valores = list(curso.values())

print(f"Las claves del diccionario son: {claves}, y los valores son: {valores}.")

