#Consigna: 
# Pedir al usuario un número N y mostrar la tabla de multiplicar del 1 al 10 de ese número.


numero = int(input("Ingrese un numero: \n"))
print(f"Tabla de mutiplicar del numero {numero}\n")

#Se pone del 1 al 11 porque el sistema cuenta del 0 en adelante, por lo que del 0 al 10 hay 11 numeros, por eso se pone del 1 al 11
#(1, 11, 1) de forma predet. cuenta de 1 en 1 por eso no se pone el 1 y queda en (1, 11). Ahora si queremos que sume de 2 en 2,
#tendriamos que poner por ej (1, 11, 2).


for i in range(1, 11):
    resultado = numero * 1
    print(f"{numero} * {i} = {resultado}")


