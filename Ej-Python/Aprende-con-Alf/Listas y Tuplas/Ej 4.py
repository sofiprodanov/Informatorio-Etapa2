# Escribir un programa que pregunte al usuario los números ganadores de la lotería primitiva, los almacene en una lista y los 
#muestre por pantalla ordenados de menor a mayor.

numeros_loteria = []
for i in range(6):
    num = int(input("¿Que numeros queres jugar? "))
    numeros_loteria.append(num)

numeros_loteria.sort()
print(f"Los numeros ganadores son {numeros_loteria}")

