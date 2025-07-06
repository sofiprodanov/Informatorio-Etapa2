#Consigna:
#Pedir al usuario su nombre y su edad. Mostrar un mensaje que diga: "Hola [nombre], tenés [edad] años."


nombre = input("Hola! ¿Cual es tu nombre? ")

try:
    edad = int(input("¿Cual es tu edad? "))
    print(f"Hola {nombre}!, tenes {edad} años.")
except ValueError:
    print("El valor ingresado no es correcto, por favor ingresa un numero.")


#Aclaracion Input:
# Los tipos de datos se almacenen por defecto con la funcion "input()" van a ser delt ipo "str", sin embargo,
#este tipo de dato puede ser convertido y, si se vuelve a usar "input()" nuevamente a lo largo de la ejecucion
#del programa con la misma variable, esta va a volver a adoptar el tipo de dato "str".
# Para solucionar un posible error y que no se "rompa" el codigo, en el caso que necesitemos que el usuario
#ingrese solo numeros podemos usar los comandos "try-except", donde nos vamos a ahorrar la linea de conversion
#ya que no va a ser necesario convertir al tipo de dato requerido luego de su ingreso, sino que podemos pedir
#pedir el dato y hacer la conversion en un solo paso.