# Dado un diccionario llamado agenda que almacena contactos, donde cada clave es el 
# nombre de una persona y su valor otro diccionario con su teléfono y correo electrónico, 
# escribí un programa qué: 
# A- Le pida al usuario que ingrese un nombre para buscar
# B- Verifique si ese nombre está en la agenda
# C- Si está, muestre el número de teléfono y el email correspondiente 
# D- Si no está, no muestre nada

agenda = {
    "Ana": {"tel": "1234",
            "email": "ana@gmail.com"},
    "Luis": {"tel": "5678",
             "email": "luis@gmail.com"}
}

nombre = input("Buscar contacto: ")

if nombre in agenda:
    print("Tel: ", agenda[nombre]["tel"])
    print("Email: ", agenda[nombre]["email"])
else:
    "No se encuentra en la agenda."


#agregar contacto a la agenda