#Ej 3: Simulacion de retiro de dinero en un banco

saldo = 200000

try:
    retiro = int(input("Indica el monto a retirar: \n"))

    if retiro <= saldo:
        print("Procesando extraccion.")
        saldo -= retiro
        print(f"Extraccion exitosa. Saldo restante: {saldo}")
    else:
        print("Fondos insuficientes.")
except ValueError:
    print("Por favor ingrese un monto valido.")