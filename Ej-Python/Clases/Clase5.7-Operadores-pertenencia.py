a = 10
b = 3
texto = "Hola mundo"
lista = [1, 2, 3, 4 ,5]

#IN
resultado = "algo" in texto
print(f"Operador IN: {resultado}") #arroja false

resultado = "mundo" in texto #podemos buscar con palabras o caracteres
print(f"Operador IN: {resultado}") #arroja ture

resultado = 6 in lista
print(f"Operador IN: {resultado}") #arroja false

resultado = 1 in lista
print(f"Operador IN: {resultado}") #arroja true

