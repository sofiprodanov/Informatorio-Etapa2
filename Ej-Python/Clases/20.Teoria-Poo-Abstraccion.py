class CuentaBancaria:
    def __init__(self, saldo_inicial):
        self._saldo = saldo_inicial
    
    def depositar(self, cantidad):
        self._saldo += cantidad
    
    #Una clase CuentaBancaria puede ocultar los detalles de cómo se gestionan los depósitos y retiros internamente, proporcionando métodos públicos
    #que los usuarios pueden invocar.
    def retirar(self, cantidad):
        if cantidad <= self._saldo:
            self._saldo -= cantidad
        else:
            print("Fondos insuficientes")
    
    def mostrar_saldo(self):
        print(f"Saldo actual: {self._saldo}")