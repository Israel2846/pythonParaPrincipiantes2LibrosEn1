""" Un streamer de YouTube decidió realizar una encuesta en la que se pidió a los usuarios que dieran su opinión sobre lo que les fustaría ver en la siguiente transmisión. Su trabajo es crear un programa que y utilice la siguiente información e imprima el resultado de lo que el usuario eligió, junto con un mensaje de agradecimiento

¿Qué debería transmitir?
a) Days Gone
b) Resident Evil 2
c) Fortnite
d) Apex Legends
e) Death Stranding
f) ¡Sorpréndenos!

El mensaje final debería ser: 

Ha elegido (opción) ¡Apreciamos su tiempo y espero verle en la próxima! """
opciones = ("a", "b", "c", "d", "e", "f")
correcto = False

while not correcto:
    respuesta = input(
        "¿Qué debería transmitir? \na) Days Gone \nb) Resident Evil 2 \nc) Fortnite \nd) Apex Legends \ne) Death Stranding \nf) ¡Sorpréndenos! \n"
    ).lower()

    if respuesta not in opciones:
        print("Respuesta equivocada, intentelo de nuevo")
    else:
        correcto = True

print(f"Ha elegido {
      respuesta}, ¡Apreciamos su tiempo y espero verle en la próxima!")
