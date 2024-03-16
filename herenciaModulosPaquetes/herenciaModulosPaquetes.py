# Herencia
""" Es un mecanismo para reutilizar el código una y otra vez """


class Transporte:
    def velocidad(self):
        print("Rapido")

    def llantas(self, numero):
        print(f"Tiene {numero} llantas")

    def motor(self, nombre):
        print(f"Tiene un enorme motor {nombre}")


class Carro(Transporte):
    def marca(self, nombre):
        print(f"Es un {nombre}")


class Motocicleta(Transporte):
    def caballito(self):
        print("Se puede hacer caballito")


ferrari = Carro()
ferrari.marca("Ferrari")
ferrari.motor("V12")
ferrari.llantas(4)
ferrari.velocidad()

yamaha = Motocicleta()
yamaha.llantas(2)
yamaha.motor("Twin-V")
yamaha.velocidad()
yamaha.caballito()


# Módulos
""" Es un archivo en el que hay código de Python, funciona para organizar nuestro código """

import convertidorDeDistancia as convertidor

print(convertidor.millas_a_kilometros(100))
print(convertidor.kilometros_a_millas(160))


from numeroMaximo import numero_mayor

numeros = [879, 858, 2, 1, 9999]
max = numero_mayor(numeros)

print(max)

# Paquetes
""" Es un directorio que contiene módulos, para crear el archivo init es el comando 'type nul > __init__.py' """
