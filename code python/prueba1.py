import os
import shutil
import random
import string

def copiar_y_modificar(carpeta_origen, carpeta_destino):
    # Copiar la carpeta de origen a la carpeta de destino
    shutil.copytree(carpeta_origen, carpeta_destino)

    # Función para generar una letra mayúscula aleatoria
    def letra_mayuscula_aleatoria():
        return random.choice(string.ascii_uppercase)

    # Función para generar un dígito aleatorio
    def digito_aleatorio():
        return random.choice(string.digits)

    # Recorrer todos los archivos en la carpeta de destino y sus subcarpetas
    for ruta_actual, carpetas, archivos in os.walk(carpeta_destino):
        for archivo in archivos:
            ruta_completa = os.path.join(ruta_actual, archivo)
            with open(ruta_completa, 'r') as f:
                contenido_original = f.read()
            
            # Modificar el contenido del archivo
            contenido_modificado = ''
            for caracter in contenido_original:
                if caracter.isalpha():
                    # Cambiar letras por dígitos aleatorios
                    contenido_modificado += digito_aleatorio()
                elif caracter.isdigit():
                    # Cambiar dígitos por letras mayúsculas aleatorias
                    contenido_modificado += letra_mayuscula_aleatoria()
                else:
                    contenido_modificado += caracter
            
            # Escribir el contenido modificado de vuelta al archivo
            with open(ruta_completa, 'w') as f:
                f.write(contenido_modificado)

if __name__ == "__main__":
    carpeta_origen = r'D:\tareas\tareas2023B\sem de so\prueba'
    carpeta_destino = r'D:\tareas\tareas2023B\sem de so\copia_prueba'  # Cambia el nombre de la carpeta destino si es necesario

    copiar_y_modificar(carpeta_origen, carpeta_destino)
    print(f"Copia de la carpeta modificada creada en {carpeta_destino}")
