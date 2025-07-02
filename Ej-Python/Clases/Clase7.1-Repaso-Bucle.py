## Flag es una variable la cual guarda un valor de True


#BUCLE INFINITO
# while True: #Es como si pusiera while "A" == "A"
#     print("Hola hace frio")

#ctrl + c > para detener el bucle

#CONTADOR#
# contador = 0
# while True:
#     contador += 1
#     print(f"Hola hace frio, {contador} veces")


#BUCLE CON FLAG
# flag = True
# while flag:
#     print("Hola info")
#     respuesta = input("Desea continuar? s/n: ")
    
#     if respuesta == "n":
#         flag = False



# while True:
#     print("Hola info")
#     respuesta = input("Desea continuar? s/n: ")
    
#     if respuesta == "n":
#         break

#     print("Luego del break")




while True:
    print("Hola info")
    respuesta = input("Desea continuar? s/n: ")

    if not (respuesta == "a" or respuesta == "n"): #negamos la condicion
        continue #corta la iteracion, no se termina de ejecutar y va a la siguiente
    #otra opcion if not respuesta == "a" and not respuesta == "n":

    if respuesta == "n":
        break

    print("Luego del break")