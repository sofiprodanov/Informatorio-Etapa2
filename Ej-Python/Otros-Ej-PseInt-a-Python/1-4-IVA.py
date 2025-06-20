#4. El sistema de registración de IVA debe asignar la letra a un comprobante de venta. Para ello se debe tener en cuenta que la empresa emisora del 
# comprobante emite comprobantes ´C´ en el caso que la misma. Revista el carácter de Responsable No Inscripto (RNI), Monotributista (M) o Exento (E), 
#cualquiera sea el carácter fiscal del comprador. Si la empresa emisora es Responsable Inscripto (RI), emitirá un comprobante ´A´ si el comprador es
#RI o es RNI, pero emitirá un comprobante ´B´ si el comprador es M o E.

print("Para poder clasificar el comprobante de venta requiero que me indiques si tu empresa es:")

while True: #define el caracter fiscal de la empresa
    print("1. RNI, M o E")
    print("2. RI")
    op1 = input("Ingrese la opcion correcta (1 o 2): ")

    #Para que la string no sea redundante (volver a ingresar los mismos valores indicando que opcion corresponde a cada una, cuando solo requiero el valor numerico)
    if op1 in ('1', '2'):
        break
    print("Opcion no valida. Intente nuevamente.")


print("\n¿Cual es el caracter fiscal del comprador?")

while True: #define caracter fiscal del comprador
    print("1. RI o RNI")
    print("2. M o E")
    op2 = input("Ingrese la opcion correcta (1-2): ")

    if op2 in ('1', '2'):
        break
    print("Opcion no valida. Intente nuevamente.")
	
#Asignación de la letra del comprobante (tipo de factura s/el caracter fiscal de la empresa emisora y el comprador)
if op1 == '1': #si la empresa emisora es RNI, M o E, emite comprobante C
    letra = 'C'
else: 
    letra = 'A' if op2 == '1' else 'B' #sino (como la op1 = RI), emite comprobante A si el comprador es RI o RNI, sino emite comprobante B (comprador M o E)

print(f"\nSe emitirá factura {letra} para el comprador.")