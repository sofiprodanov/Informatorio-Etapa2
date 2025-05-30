#Escribir un programa que almacene el diccionario con los créditos de las asignaturas de un curso 
#{'Matemáticas': 6, 'Física': 4, 'Química': 5} y después muestre por pantalla los créditos de cada 
#asignatura en el formato <asignatura> tiene <créditos> créditos, donde <asignatura> es cada una de las
#asignaturas del curso, y <créditos> son sus créditos. Al final debe mostrar también el número total de 
#créditos del curso.

materias = {
    "matematicas": 6,
    "fisica": 4,
    "quimica": 5,
}
total_creditos = 0

for materia, credito in materias.items():
    print(f"La asignatura {materia} tiene {credito} creditos.")
    
    total_creditos += credito # suma los creditos de cada materia

print(f"Tiene {credito} creditos acumulados durante el curso.")
