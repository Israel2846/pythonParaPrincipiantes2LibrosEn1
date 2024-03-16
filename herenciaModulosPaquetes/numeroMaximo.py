def numero_mayor(numeros):
    max = numeros[0]

    for numero in numeros:
        
        if numero > max:
            max = numero

    return max
