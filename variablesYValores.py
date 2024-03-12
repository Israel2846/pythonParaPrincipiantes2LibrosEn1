print("Primera línea")

# Variables primitivas
nombre = "Jhon"
edad = 33
peso = 131.5
esta_casado = False

# Variables vacías
variable_vacia1 = 0
variable_vacia2 = ""

# Conversión de int a string
texto1 = "Cero es igual a "
texto2 = 0

print(texto1 + str(texto2))

# 2da converción de int a string
texto1 = "Cero sigue siendo igual a "
texto2 = str(0)

print(texto1 + texto2)

# Formato de cadena
show = "GOT"
nombre1 = "Daenerys"
nombre2 = "Jon"
nombre3 = "Tyrion"
temporadas = 8

print(f"El programa llamado {show} tenía personajes como {nombre1}, {
      nombre2} y {nombre3} en las {temporadas} temporadas")

# Valores de entrada del usuario
print("Hola y bienvenido a mi tutorial interactivo")

nombre = input("Tu nombre: ")
edad = int(input("Tu edad: "))
ciudad = input("Tu ciudad: ")
email = input("Por favor, introduzca su dirección de correo electrónico: ")

print(f"Muchas gracias {nombre}, se le contactará en {email}")
