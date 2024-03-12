""" Sirven para crear tipos de datos, al igual pueden contener funciones y métodos """


class InstructorDeClase:
    def __init__(self, nombre):
        self.nombre = nombre

    def hablar(self):
        print("Hablar")


yo = InstructorDeClase("Israel Colín")
print(yo.nombre)
yo.hablar()


class Héroes:
    def __init__(self, nombre, edad, color):
        self.nombre = nombre
        self.edad = edad
        self.color = color

    def presentarse(self):
        print(f"Mi nombre es {self.nombre}, tengo unos {
              self.edad} años y mi disfraz es de color {self.color}")


heroe1 = Héroes("Steve", 40, "Azul")
heroe2 = Héroes("Tony", 38, "Rojo")

heroe1.presentarse()
heroe2.presentarse()


# Excepciones
""" Sirven para manejar posibles errores del programa de una manera fácil de entender """
try:
    nombre = "Bruce Wayne"
    edad = 45
    print(nombre + edad)
except TypeError:
    print("Por favor, usa una cadena formateada o convierte la edad en una cadena")

try:
    edad = 45
    edad1 = 0
    promedio = edad / edad1
    print(promedio)
except ZeroDivisionError:
    print("No dividas entre 0!!!")
except TypeError:
    print("Por favor, usa una cadena formateada o convierte la edad en una cadena")
