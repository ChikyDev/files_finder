import os

VERDE = "\033[92m"
NEGRITA = "\033[1m"
RESET = "\033[0m"

def examinar_archivos(extension, ruta):

    contador = 0

    for files in os.listdir(ruta):
        if files.endswith(extension):
            print(VERDE + f"Archivo encontrado: {RESET}{NEGRITA}{files}{RESET}")
            contador += 1

    print(f"Se han encontrado {contador} arcvivos totales")

archivo = input("En que termina el/los archivos que buscas (.exe, .bat, .dll, etc...): ")
direccion = input("Introduce la ruta donde quieres examinar los archivos: ")

examinar_archivos(archivo, direccion)