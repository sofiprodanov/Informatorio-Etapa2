# USO DE OPERADORES:
# --> OPERADORES MATEMATICOS: suma (+), resta (-), division (/ o //), multiplicacion (*), modulo/porcentaje (%), potencia (**).
# --> OPERADORES DE COMPARACION: mayor/menor que (>/<), mayor/menor o igual que (>=/<=), igual (==), distinto (!=).
# --> OPERADORES LOGICOS: and, or, not, concatenacion, multiplicacion, mezcla.

# OPERADORES MATEMATICOS:
num1 = 10
num2 = 5

#suma
#opcion 1 
print(num1+num2)

#opcion 2: almaceno el rdo en una variable y muestro el valor de la variable
resultado = num1 + num2
print(resultado)

#resta
#opcion 1 
print(num1-num2)

#opcion 2:
resultado = num1 - num2
print(resultado)

#multiplicacion
#opcion 1 
print(num1*num2)

#opcion 2:
resultado = num1 * num2
print(resultado)

#division
#opcion 1 
print(num1/num2)

#opcion 2:
resultado = num1/num2
print(resultado)

#porcentaje/modulo
#opcion 1 
print(num1%num2)

#opcion 2:
resultado = num1%num2
print(resultado)

#potencia
#opcion 1 
print(num1**num2)

#opcion 2:
resultado = num1**num2
print(resultado)


#OPERADORES DE COMPARACION
#Mayor que: a > b
#Menor que: b < a
#Mayor o igual: a >= b
#Menor o igual: b <= a
#Igual: a = b
#Distinto: a != b


#OPERADORES DE COMPARACION:
#And (devuelte true si ambos valores son true, en cualquier otro caso es false)
#a = true
#b = true
#x = a AND b --> True 

#Or (uno de los dos tiene que ser True para que devuelva True)
#a = true
#b = true
#x = a OR b --> True  

#a = true
#b = flase
#x = a OR b --> True

#Not (cambia el valor de verdad de la variable a la que se aplica la operacion)
#a = true
#x = NOT a --> False


#Concatenacion:
print("Hola " + "Mundo")


#Multiplicacion:  
resultado = 3 * "Hola"
print(resultado)

#O en todo caso
print(3*"Hola")


#Mezcla:
resultado = 3 * "Hola " + "mundo"
print(resultado)

#o en todo caso 
print(3 * "Hola " + "mundo")