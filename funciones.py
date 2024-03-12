""" Sirven para definir un proceso que se realizará varias veces y solo hacerlo una vez, también para tener más orden en el código """


def di_hola(nombre):
    print(f'Hola {nombre}\nBienvenido a mi transmisión en vivo')


usuario = input("Escribe tu nombre: ")
di_hola(usuario)


def cubo(numero):
    return numero ** 3


numero = int(input("Escribe un número: "))
print(cubo(numero))
