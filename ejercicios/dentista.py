""" Un dentista desea que se cree un programa para su sitio web donde se le presenten múltiples servicios a los clientes. El cliente elegirá la opción y se le presentará un total por el servicio que debe pagar el cliente. Los servicios se dan como se muestra a continuación:
a) Terapia de canal de raíz- $250
b) Chequeo de higiene oral- $50
c) Tratamiento de lesiones de emergencia- $100
d) Chequeo post-procedimiento- $150
e)Chequeos de rutina y consultas - $75

Para pagos anticipados, los clientes tienen un 50% de descuento

Diseñar un programa que proporcione al cliente toda la información necesaria y dar un total según lo que el cliente elija """
opciones = {
    "a": 250,
    "b": 50,
    "c": 100,
    "d": 150,
    "e": 75
}
opcion_correcta = False
anticipado_correcto = False


def descuento(precio):
    total = precio - (precio * .5)
    return total


while not opcion_correcta:
    eleccion = input("Escoja una de las siguientes opciones: \na) Terapia de canal de raíz- $250 \nb) Chequeo de higiene oral- $50 \nc) Tratamiento de lesiones de emergencia- $100 \nd) Chequeo post-procedimiento- $150 \ne)Chequeos de rutina y consultas - $75 \n")

    if eleccion in opciones:
        opcion_correcta = True
        eleccion = opciones[eleccion]


while not anticipado_correcto:
    anticipado = input("¿Desea pagar por anticipado? S/N: ").lower()

    if anticipado == 's':
        anticipado = True
        anticipado_correcto = True
        eleccion = descuento(eleccion)
    elif anticipado == 'n':
        anticipado = False
        anticipado_correcto = True
    else:
        print("Opción incorrecta, intente de nuevo: ")

print(f'Tu total sería de ${eleccion}')
