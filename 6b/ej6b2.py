"""
Enunciado:
Utilizando un depurador de código para Python. Corrije el error de la
función llamada 'average_of_even_numbers(numbers)' que acepta una lista de
números enteros como entrada y calcula el promedio de todos los números pares
en la lista.

Para depurar el código se puede usar pdb o herramientas de depuración
externas.

La función debe devolver un número flotante redondeado a dos decimales. Si no
hay números pares en la lista, la función debe devolver 0.

Parámetros:
    numbers: una lista de números enteros.

Ejemplo:
    Entrada:
        numbers = [2, 3, 4, 5, 6]
    Salida:
        4.0
"""


from typing import List

    
def average_of_even_numbers(numbers):
    total = 0 # Promedio de todos los números pares
    count = 0 # Contador de números pares para hacer el promedio
    for num in numbers:
        if num % 2 == 0: # El número es par
            total += num # Sumatorio de números pares
            count += 1
    if count == 0: # No hay ningún número par en la lista
        return 0
    else: 
        total = round(total/count,2) # Realizamos el promedio

    return total


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script

#numbers = [2, 3, 4, 5, 6]
#result = average_of_even_numbers(numbers)
#print(result)
