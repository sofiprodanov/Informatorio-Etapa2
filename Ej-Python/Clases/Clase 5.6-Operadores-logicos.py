a = 10
b = 3
c = 20

#AND
resultado = a > b and a < c #Arroja true
print(f"Operador AND: {resultado}") #Arroja true

resultado = a > b and a < c and a == "algo"
print(f"Operador AND: {resultado}") #Arroja false


#OR
resultado = a > b or a < 5
print(f"Operador OR: {resultado}") #Arroja true


#NOT
resultado = not a > b #Si a no es mayor a b
print(f"Operador AND: {resultado}") #Arroja false
