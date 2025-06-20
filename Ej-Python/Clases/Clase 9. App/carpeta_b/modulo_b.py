from carpeta_a.modulo_aa import saludar_con_nombre_de_funcion_largo as saludo
from carpeta_a.modulo_ab import despedir

def ejecutar():
    mensaje = saludo("Pablo")
    print(f"modulo_b recibio: {mensaje}")

    mensaje_despedida = despedir("Juan")
    print(f"desde modulo_b: {mensaje_despedida}")

# ejecutar() si no tuviera el main.py


if __name__ == "__main__": #es para que ejecute el archivo como modulo
    ejecutar()

#Me posiciono sobre carpeta app, abro la consola y en la terminal debo poner py -m carpeta_b.modulo_b (indico carpeta y archivo)