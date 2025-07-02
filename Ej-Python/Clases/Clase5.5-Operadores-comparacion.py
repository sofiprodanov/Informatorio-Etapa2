a = 10
b = 3

print(f"Operador ==: {a == b}") #arroja false
print(f"Operador is: {a is b}") #compara a nivel de memoria. Arroja False

x = "hola"
y = "hola"
print(f"Operador ==: {x == y}") #arroja true
print(f"Operador is=: {x is y}") #arroja true tiene el mismo objeto de memoria


lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
print(f"Operador ==: {lista1 == lista2}") #de acuerdo a los valores son verdadero
print(f"Operador is=: {lista1 == lista2}") #en cuanto a memoria es falso

resultado = a != b
print(f"Operador !=: {resultado}") #arroja True

resultado = a > b
print(f"Operador >: {resultado}") #arroja True

resultado = a < b
print(f"Operador <: {resultado}") #arroja false

resultado = a >= b
print(f"Operador >=: {resultado}") #arroja True

resultado = a <= b
print(f"Operador <=: {resultado}") #arroja True













