#Escribir una función que reciba un número entero positivo y devuelva su factorial.

def factorial(n): #numero entero positivo
    """Funcion que calcula el factorial de un numero entero positivo.
    Parametros:
    - n: numero entero positivo
    Devuelve el factorial de n.
    Arroja error si no es un entero o es negativo."""

    #VALIDACION DEL INPUT
    if not isinstance(n, int) or n < 0: #verifica que si no es una instancia de la clase entero o si n es un numero negativo arrojara el error.
        raise ValueError("n debe ser un entero positivo.") #raise > para dar excepciones manualmente

    num = 1
    #CALCULO FACTORIAL
    for i in range(n):
        num *= i + 1 #Esta línea multiplica el valor actual de num por (i + 1)) y guarda el resultado nuevamente en num
    return num

print(factorial(5))