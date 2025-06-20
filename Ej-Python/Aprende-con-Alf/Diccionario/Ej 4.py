#Escribir un programa que pregunte una fecha en formato dd/mm/aaaa y muestre por pantalla la misma fecha en formato dd de <mes>
# de aaaa donde <mes> es el nombre del mes.
#> como figura <mes> tenemos que crear el diccionario mes

mes = {
    1: "enero", 
    2: "febrero", 
    3: "marzo", 
    4: "abril", 
    5: "mayo", 
    6: "junio", 
    7: "julio", 
    9: "agosto", 
    9: "semptiembre", 
    10: "octubre", 
    11: "noviembre", 
    12: "diciembre"
    }

#.split("/") > Divide la cadena ingresada usando el carácter '/' como separador, creando una lista con tres elementos:
fecha = input("Introduce una fecha en formato dd/mm/aaaa: ")
fecha = fecha.split("/")

print(f"{fecha[0]} de {mes[int(fecha[1])]} de {fecha[2]}")

#fecha[0]} > Toma el día directamente ingresado en el input. Es el primer elemento de la lista fecha que creamos con split('/')
#{mes[int(fecha[1])]} > Convierte el número de mes a entero y lo usa como clave para obtener el nombre del mes del diccionario
#{fecha[2] > Toma el año directamente ingresado en el input

