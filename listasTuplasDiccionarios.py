# Listas (lista = [])
""" Una lista está representada por corchetes y pueden contener múltiples elementos dentro de ella """


def listas():
    amigos = ['Juan', 'César', 'Eduardo', 'Jorge', 'Jaime', 'Armando']
    numeros = [5, 7, 1, 9, 2, 65, 48, 5, 9]

    # Tamaño de lista
    print(len(amigos))

    # Posiciones de lista
    print(amigos[0], amigos[1], amigos[2], amigos[3], amigos[4], amigos[5])

    # Posiciones inversas
    print(amigos[-1], amigos[-2], amigos[-3],
          amigos[-4], amigos[-5], amigos[-6])

    # Conjuntos de posiciones
    print(amigos[3:], amigos[2:5])

    # Modificación de datos en lista
    amigos[2] = 'Julian'

    # Insertar datos en posición aleatoria
    amigos.append('Luis')

    # Insertar datos en posición específica
    amigos.insert(2, 'Pedro')

    # Eliminar datos por valor (Si hay dos valores iguales, solamente eliminará el primero)
    amigos.remove('Jaime')

    # Eliminar datos por índice (devuelve el dato eliminado, si no se pasa argumento elimina el último dato de la lista)
    amigos.pop(5)

    # Ordenar listas
    numeros.sort()

    # Ordenar listas inversas
    numeros.reverse()

    # Vaciar listas
    numeros.clear()

    print(f'lista de amigos {amigos}')
    print(f'lista de números {numeros}')


# Tuplas (tupla = ())
""" Casi como las listas, la gran diferencia es que no pueden ser modificadas o cambiadas una vez se crean """


def tuplas():
    # Definicion de tuplas
    colores = ('rojo', 'verde', 'azul')

    # Acceder a un elemento de tupla
    print(f'El primer color es {colores[0]}')

    # Iterar sobre tuplas
    for color in colores:
        print(color)

    # Concatenar tuplas
    colores_adicionales = ('amarillo', 'naranja')
    todos_los_colores = colores + colores_adicionales

    print(todos_los_colores)


# Diccionarios (diccionario = {clave: valor})
""" A diferencia de las tuplas y las listas, los diccionarios trabajan con 'clave valor' """


def diccionarios():
    # Inicialización de diccionarios
    amigo = {
        'nombre': 'James',
        'edad': 30,
        'correo electrónico': 'james@dominio.com',
        'coche': 'Tesla T1'
    }

    # Acceder a un valor
    print(amigo["correo electrónico"])

    # Comprobar si existe el valor
    print(amigo.get("fecha_nacimiento"))

    # Darle datos por defecto si es que no existe
    print(amigo.get("fecha_nacimiento", "13, 08, 1999"))

    # Modificar datos de diccionario
    amigo["edad"] = 60

    # Iterar sobre un diccionario
    for clave, valor in amigo.items():
        print(f'{clave}: {valor}')

    # Agregar datos
    amigo["ocupacion"] = 'Ingeniero'

    # Eliminar datos
    del amigo["correo electrónico"]

    print(amigo)


diccionarios()
