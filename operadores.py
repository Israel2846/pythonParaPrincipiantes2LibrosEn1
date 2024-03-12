# Diferente a (!=)
""" Se utiliza para comparar una declaración en la que retorna un valor verdadero si dicha declaración es diferente a """


def diferente():
    nombre = 'José'
    apellido = 'Pérez'
    edad = 25
    antecedentes_penales = False

    if antecedentes_penales != True:
        print('Sí puedes tener un prestamo')
    else:
        print('Lo siento, no puedes tener un prestamo')


# Mayor igual a, menor igual a (>= <=)
""" Se utiliza para comparar un número que sea mayor o menor, y a su vez si es exactamente el mismo """


def menor_mayor_igual():
    print('Bienvenido a nuestro verificador de elegibilidad en línea')

    edad = int(input('Introduce tu edad: '))
    licencia = input('¿Tienes licencia? S/N ')
    salario = int(input('¿Cuál es tu salario? $'))

    if licencia.lower() == 's':
        licencia = True
    else:
        licencia = False

    if edad <= 35:
        print('La edad está bien')

        if licencia == True:
            print('Tienes una licencia válida')

            if salario >= 3500:
                print('¡Perfecto! eres elegible')
            else:
                print('Lo siento, estás por debajo de nuestros requisitos mínimos')

        else:
            print('Lo siento, pero necesitas tener una licencia válida')

    else:
        print('Estás por encima de nuestros límites de edad máximo.')


# Operador de módulo (%)
""" Se utiliza para devolver el residuo de una división """


def modulo():
    alfa = 20
    beta = 11

    print(alfa % beta)


# Divisiones (/ y //)
""" Son divisiones, / se utiliza para divisiones sencilla y siempre retorna un valor decimar, // siempre retorna el valor entero inmediato por debajo"""


def divisiones():
    alfa = 20
    beta = 11

    print(f'La division normal es {
        alfa / beta}, la división entera es {alfa // beta}, y el redondeo es {round(alfa / beta)}')


# Exponente (**)
""" Sirve para hacer un exponente de un número """


def exponentes():
    alfa = 20
    beta = 11

    print(f'El exponente es {alfa ** beta}')


# Operadores lógicos (and or)
""" Funciona para devolver un bool dependiendo el caso, and es si 2 o más sentencias se cumplen, or es si aunque sea una de 2 o más sentencias se cumplen """


def operadores_lógicos():
    print('Comprobador de elegibilidad 101')

    nombre = input('Por favor, introduzca su nombre: ')
    salario = int(input('Por favor, introduzca su salario: '))
    salario_minimo = 5000
    buen_historial_crediticio = False

    # AND
    if salario >= salario_minimo and buen_historial_crediticio:
        print(f'Felicidades {nombre}, usted es elegible para una hipoteca.')
    else:
        print(f'{nombre}, parece que usted no es elegible en este momento')

    # OR
    if salario >= salario_minimo or buen_historial_crediticio:
        print(f'Felicidades {nombre}, usted es elegible para una hipoteca.')
    else:
        print(f'{nombre}, parece que usted no es elegible en este momento')

    # NOT
    if salario >= salario_minimo and not buen_historial_crediticio:
        print(f'Felicidades {nombre}, usted es elegible para una hipoteca.')
    else:
        print(f'{nombre}, parece que usted no es elegible en este momento')


operadores_lógicos()
