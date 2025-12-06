"""
Enunciado:
Utilizando un depurador de código para Python, corregir los errores en las
funciones 'is_prime(num)' y 'check_primes(nums)'.

La función 'is_prime(num)' es utilizada dentro de 'check_primes(nums)' para
determinar si un número es primo.

La función llamada 'check_primes(nums)' acepta una lista de números enteros
como entrada y devuelve una lista de valores booleanos, indicando si cada
número en la lista es primo o no.

Para depurar el código, se puede utilizar pdb u otras herramientas de depuración
externas.


Parámetros:
    nums: una lista de números enteros.

Retorno:
    Una lista de valores booleanos, indicando si cada número en la lista es primo o no.

Ejemplo:
    Entrada:
        nums = [1, 5, 11, 12, 13, 14, 15]
    Salida:
        [False, True, True, False, True, False, False]

"""


from typing import List


def isprime(num):
    if num < 2: # Número inferiores a dos no son primos
        return False
    for i in range(2, int(num**0.5)+1): # Comprobamos los divisores de dos
        if num % i == 0:
            return False
    return True


def check_primes(nums: List[int]) -> List[bool]:
    results = []
    for num in nums:
        results.append(isprime(num))
    return results


# Si quieres probar tu código, descomenta las siguientes líneas y ejecuta el script
#numbers_list = [1, 5, 11, 12, 13, 14, 15]
#print(check_primes(numbers_list))
