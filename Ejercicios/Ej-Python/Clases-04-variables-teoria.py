variable = "valor"

# int > numeros enteros (integer)
# float > numeros decimales
# str > numeros strings o cadena de caracteres
# bool > booleanos

#Cada variable tiene un tipo de elemento o dato, en este caso una cadena de caracteres. #Cada valor tiene comillas simples (""), 
# y por mas que el valor sea distinto en cada variable, #el tipo de dato sigue siendo el mismo: STRING o SRT.

caja1 = "ropa de invierno"
caja2 = "ropa de verano"
caja3 = "elementos de cocina"

#Como Python es de tipado dinamico, el valor de nuestra variable puede cambiar en tiempo de ejecucion, #y solo debemos asignar un nuevo valor a la variable.

caja1 = 123
caja2 = 456
caja3 = 789

#La funcion print() sirve para mostrar en pantalla el valor que tienen las variables

#Para abrir la consulta en la parte inferior de VSC, presionamos ctrl + ñ, ctrl + j o #desde la parte superior en "Ver".

#Para estar seguros del tipo de dato que contiene nuestra variable, podemos usar otra funcion con lo cual podemos identificar esto.
#Esta funcion es: type()

variable1 = "Esto es un contenido de tipo str."
print (type (variable1))

variable2 = 123456
print (type (variable2))

variable3 = 4.351
print (type (variable3))

variable4 = True
print (type (variable4))

variable5 = False
print (type (variable5))

#Se ejecuta indicando en la terminal "python nombre_del_archivo.py" o desde el simbolo "Play".

# PALABRAS RESERVADAS:
# False - True // None // __peg_parser__ // and // as //assert // async // await // break - continue // class // def // del // except // finally // from //
# if - else - elif - while - for // global // import // in // is / lambda // nonlocal // not // or // pass // raise // return // try // with // yield //

# USO DE OPERADORES:
# --> OPERADORES MATEMATICOS: suma (+), resta (-), division (/ o //), multiplicacion (*), modulo/orcentaje (%), potencia (**).
# --> OPERADORES DE COMPARACION: mayor/menor que (>/<), mayor/menor o igual que (>=/<=), igual (==), distinto (!=).
# --> OPERADORES LOGICOS: and, or, not, concatenacion, multiplicacion, mezcla.
# Ej. and: a = true, b = true, x = a AND b --> True (devuelte true si ambos valores son true, en cualquier otro caso es false)
# # Ej. or: a = true, b = true, x = a OR b --> True  // a = true, b = flase, x = a OR b --> True (cambia el valor de verdad de la variable a la que se
# aplica la operacion)
# Ej. not: a = true, x = NOT a --> False (cambia el valor de verdad de la variable a la que se aplica la operacion)
# Ej. concatenacion:  "Hola" + "mundo" --> Hola mundo.
# Ej. multiplicacion:  3 * "hola" --> HolaHolaHola.
# Ej. mezcla:  3 * "Hola" + "mundo" --> HolaHolaHola mundo.

