# Escribir una función que calcule el total de una factura tras aplicarle el IVA. La función debe recibir la cantidad sin IVA y el porcentaje de IVA
# a aplicar, y devolver el total de la factura. Si se invoca la función sin pasarle el porcentaje de IVA, deberá aplicar un 21%.

def calculo_iva(montosiniva, iva = 21):
    """Calcula el iva de una factura.
    Parametro:
    - Monto sin iva.
    - Monto definido del 21% el iva."""
    factura_iva = montosiniva + (montosiniva * iva /100)
    print(f"La factura total es {factura_iva}")

calculo_iva(10000)

