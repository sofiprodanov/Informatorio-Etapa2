#Se definen con llaves {} y estan compustos por pares (clave-valor / key-value)
#Las claves son unicas, y los valores pueden ser cualquier tipo de dato, incluso otros diccionarios...
#Son desordenados (sus elementos no tienen indice) y son mutables (podemos agregar, eliminar, modificar)

estudiante = {
    "nombre": "Ana",
    "edad": 23,
    "curso": "Matematica"
}

print(f"Conjunto diccionario: {estudiante}, {type(estudiante)}")
print(f"Edad estudiante: {estudiante['edad']}") #acceder a valores
#Las claves no se repiten, pero puede haber varios valores.

estudiante["carrera"] = "Ing" #para agregar una clave-valor
print(f"Carrera estudiante: {estudiante['Carrera']}")

del estudiante["carrera"]#para eliminar un elemento/clave junto con su valor
print(f"Estudiante: {estudiante}")

print(f"Claves (keys) del diccionario: {estudiante.keys()}") #muestra las claves
print(f"Valores (values) del diccionario: {estudiante.values()}") #muestra los valores


estudiante_dos = {
    "nombre": "Juan",
    "edad": 23,
    "curso": {
        "nombre": "Programacion web",
        "tags": ["PW", "Programacion", "Web", "Python", "Django"]
    }
}

print(f"Estudiante dos: {estudiante_dos['curso']['nombre']}")
print(f"Estudiante dos: {estudiante_dos['curso']['tags'][3]}")


estudiante_dos["curso"]["tags"][5]["algo"] = 99
print(f"Estudiante dos: {estudiante_dos['curso']['tags'][5]["algo"]}")



#usando for
calificaciones = {
    "quimica": 10,
    "fisica": 5,
    "lengua": 7
}

for materia, nota in calificaciones.items():
    print(materia, nota)


#variable = xxx.get(clave) > si no existe el elemento en el diccionario, no tire error y de el valor por defecto (si se asigna). Si no tiene valor por defecto tira none.
