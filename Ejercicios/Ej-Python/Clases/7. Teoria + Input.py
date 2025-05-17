print("Parte 1")

nombre = input ("Ingrese su nombre: ")
numero = input ("Ingrese su edad: ")


print (nombre)
print (numero)

print (type(nombre))

print (type(numero)) #devuelve una string

numero = int(numero) #convierte string a numero entero
print (type(numero))



print("Parte 2")

año_nacimiento = input ("Ingrese un numero: ") #pide ingresar año de nacimiento 
conversion = int(numero) #se puede utilizar otra variable y en esa variable asignar el valor pero convertido
print (type(conversion))



print("Parte 3")
# Puede cambiar el tipo de dato a lo largo del programa, pero mas de un tipo de dato no puede existir como valor
#dentro de la variable al mismo tiempo.
numero = input("Ingrese una palabara y un numero: ")
print (type(numero))



print("Parte 4")
# Los tipos de datos se almacenen por defecto con la funcion "input()" van a ser delt ipo "str", sin embargo,
#este tipo de dato puede ser convertido y, si se vuelve a usar "input()" nuevamente a lo largo de la ejecucion
#del programa con la misma variable, esta va a volver a adoptar el tipo de dato "str".
# Para solucionar un posible error y que no se "rompa" el codigo, en el caso que necesitemos que el usuario
#ingrese solo numeros podemos usar los comandos "try-except", donde nos vamos a ahorrar la linea de conversion
#ya que no va a ser necesario convertir al tipo de dato requerido luego de su ingreso, sino que podemos pedir
#pedir el dato y hacer la conversion en un solo paso.

try:
    numero = int(input("Ingrese un numero entero: "))
    print("Muchas gracias por ingresar un numero entero.")
except ValueError: #mitigamos un posible error en el ingreso de un tipo de dato que no sea el solicitado.
    print("El dato ingresado no es un numero entero. Intente nuevamente.")