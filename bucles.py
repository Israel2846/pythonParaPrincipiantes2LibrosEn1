# Bucle IF
contraseña = input("Introduzca una contraseña ")
print("Bienvenido al portal")

check_contraseña = input("Por favor, introduzca su contraseña ")

if check_contraseña == contraseña:
    print("¡Exitoso! ¡Bienvenido de nuevo!")
else:
    print("¡Lo siento amigo! No es la contraseña")

 # Elif
print("Bienvenido a mi pequeño juego")

numero = int(input("Introduce un número del 1 al 3 "))

if numero == 1:
    print("Te encanta ser un líder")
elif numero == 2:
    print("Odias estar solo ¿verdad?")
elif numero == 3:
    print("Cuantos más mejor ¿no?")
else:
    print("¿Es enserio? No puedes seguir instrucciones simples, ¿verdad?")

# Bucle While
x = 0

while x <= 10:
    print(x)
    x += 1

mi_numero = 19
intento = 0
max_intentos = 3

while intento < max_intentos:
    intento += 1
    numero = int(input("Ingresa un número: "))

    if numero == mi_numero:

        if intento == (max_intentos):
            print("Al último lo lograste")
        else:
            print("Lo lograste")
        break

    else:

        if intento < max_intentos:
            print("Intente de nuevo")

else:
    print("Se te acabaron las oportunidades")

# Bucle for
for char in ["Yo", "Amo", "Programar"]:
    print(char)

for numero in range(10, 21, 2):
    print(numero)

precios = [5, 10, 15, 20, 25]
total = 0

for precio in precios:
    total += precio

print(f"El precio total es {total}")

for a in range(3):

    for b in range(3):

        for c in range(3):
            print(f"{a}, {b}, {c}")
