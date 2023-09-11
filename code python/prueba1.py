import os     # Importa la biblioteca os para operaciones de sistema de archivos
import shutil # Importa la biblioteca shutil: es una biblioteca que proporciona operaciones en sistemas de archivos.
import random # Importa la biblioteca random para generar números aleatorios
import string # Importa la biblioteca string para acceder a cadenas de caracteres

def procesamientolotes(original, final):
    # Copiar la carpeta de origen a la carpeta de destino, copytree se utiliza para copiar un directorio y todo su contenido a otro directorio.
    shutil.copytree(original, final)
    # Función para generar una letra mayúscula aleatoria
    def letra_mayuscula_aleatoria():
        return random.choice(string.ascii_uppercase)
    # Función para generar un dígito aleatorio
    def digito_aleatorio():
        return random.choice(string.digits)
    # Recorrer todos los archivos en la carpeta de destino y sus subcarpetas
    for rActual, carpetas, archivos in os.walk(final):
        for archivo in archivos:
            ruta_completa = os.path.join(rActual, archivo)
            #with: se usa para asegurarse de que el archivo se cierre automáticamente después de su uso
            #r es para modo lectura
            with open(ruta_completa, 'r') as f:
                contenido = f.read()
            # Modificar el contenido del archivo
            contenidocopiado = ''
            for caracter in contenido:
                #Estos if determinan que sí el caracter es letra, la cambia a digito y si es digito la cambia a letra
                if caracter.isalpha():
                    # Cambiar letras por dígitos aleatorios
                    contenidocopiado += digito_aleatorio()
                elif caracter.isdigit():
                    # Cambiar dígitos por letras mayúsculas aleatorias
                    contenidocopiado += letra_mayuscula_aleatoria()
                #si es un caracter indefinido, se copia tal cual
                else:
                    contenidocopiado += caracter
            # Escribir el contenido modificado de vuelta al archivo
            with open(ruta_completa, 'w') as f:
                f.write(contenidocopiado)
#Colocar las rutas                
if __name__ == "__main__":
    original = r'D:\tareas\tareas2023B\sem de so\prueba'
    final = r'D:\tareas\tareas2023B\sem de so\copia_prueba'

    procesamientolotes(original, final)
