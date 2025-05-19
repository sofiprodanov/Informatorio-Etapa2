# 7. La nota final en la escuela de informática se obtiene en función de 3 notas. La nota final del primer examen, la nota del segundo examen y 
# una nota de concepto del profesor. La nota del primer examen se pondera como 30% de la nota final, la del segundo examen como el 50% y la de 
# concepto como el 20% de la nota final. Elabore un algoritmo que en base a esas tres notas calcule la nota final.


print("Ingrese las notas (0-100):")
nota1 = float(input("Primer examen: ")) * 0.30
nota2 = float(input("Segundo examen: ")) * 0.50
concepto = float(input("Concepto del profesor: ")) * 0.20

print(f"\nNota final: {round(nota1 + nota2 + concepto, 2)}%")