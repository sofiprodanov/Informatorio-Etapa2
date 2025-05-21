#Dado este diccionario:
#estudiante = {
# "nombre": "Ana",
# "edad": 20,
# "materias": ["Matemática", "Historia"]
#}
#1- Mostrá el nombre y la edad
#2- Agregá una materia nueva a la lista materias
#3- Mostrá cuántas materias cursa con len()


estudiante = {
    "nombre": "Ana",
    "edad": 20,
    "materias": ["Matemática", "Historia"]
    }

#Punto 1
print("Nombre:", estudiante["nombre"])
print("Edad:", estudiante["edad"])

#Punto 2
estudiante["materias"].append("Plastica")
print("Tu diccionario quedo de la siguiente forma: ", estudiante)

#Punto 3
cantidad_materias = len(estudiante["materias"])
print("Esta cursando", cantidad_materias,"materias.")








