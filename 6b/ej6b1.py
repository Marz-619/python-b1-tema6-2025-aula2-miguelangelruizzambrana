"""
Enunciado:
Implementa dos funciones: 'count_letters(names)' y 'create_log(names)'.
En primer lugar, utilizando la librería logging, implementa una función 
'count_letters(names)' que recibe como parámetro 'names' que es una lista de 
strings con nombres. La función debe contar cuántas veces aparece cada letra 
en todos los nombres de la lista. La función debe devolver un diccionario con 
la frecuencia de cada letra.

En segundo lugar, la función 'create_log(names)' recibe también una lista
de strings con nombres, llama a la función 'count_letters(names)' y almacena
el diccionario generado en el archivo 'production.log' en formato de 
registro de nivel DEBUG.

Una vez se tenga el diccionario de la función 'count_letters(names)', debes
guardarlo con el siguiente código:
logging.info(f'Letter counts: {letter_counts}')

Parámetro:
    names: lista de strings.

Ejemplo:
    Entrada:
        ["Juan", "Pedro", "Marta"]
    Salida:
        Existe un fichero "production.log" que contiene:
        DEBUG:root:Letter counts: {'J': 1, 'u': 1, 'a': 3, 'n': 1, 'P': 1, 'e': 1, 'd': 1, 'r': 2, 'o': 1, 'M': 1, 't': 1}

Nota: Verificar que el archivo de logs se haya creado.

"""
import logging

logging.basicConfig(
    level=logging.DEBUG,  # Nivel de severidad de los mensajes
    format="%(asctime)s - %(levelname)s - %(message)s", #Formato de los mensajes del log
    filename="production.log", #Los mensajes se escribiran en el siguiente fichero log
    filemode="w" # Modo de apertura del fichero, en este caso modo escritura Write
)

logger = logging.getLogger(__name__) # Creamos el objeto logger



def count_letters(names):
    letras = {} # Creamos diccionario vacío con las repeticiones de cada letra
    for nombre in names: # Recorremos la lista de nombres
        for letra in nombre: # Recorremos las letras de cada nombre y aumentamos la frecuencia
            letras[letra] = letras.get(letra,0) + 1 # Contador de frecuencias de cada letra
    return letras

def create_log(names):
    logger.debug("Iniciando el proceso de contar las letras") # Escribimos mensaje de nivel INFO en el log
    if len(names)==0:
        logger.error("La cadena de entrada está vacía, no hay vocales")
    else:
        logger.debug("Empezamos a contar las vocales de la cadena")
        letter_counts = count_letters(names)
        logger.debug(f'Letter counts: {letter_counts}')
        logger.debug("Ejecución realizada con éxito")

# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script

#create_log(["Juan", "Pedro", "Marta"])
