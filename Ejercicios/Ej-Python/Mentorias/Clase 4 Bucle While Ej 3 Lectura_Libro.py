#Ej 3: Lee hasta llegar a la ultima pagina del libro

import time

pagina_actual = 1

#Validacion de entrada de datos.
while True:
    try:
        paginas_total = int(input("Total de paginas del libro: \n"))
        if paginas_total > 0:
            break
        print("Por favor ingrese un numero mayor a cero.")
    except ValueError:
        print("Por favor ingrese un numero valido.")

#Muestra progreso:
print(f"\nIniciando lectura, {paginas_total} páginas...\n")
while pagina_actual <= paginas_total:
    print(f"Leyendo página {pagina_actual}/{paginas_total} - {pagina_actual/paginas_total:.0%} completado")
    pagina_actual += 1
    time.sleep(2)

print("Termine el libro.")
