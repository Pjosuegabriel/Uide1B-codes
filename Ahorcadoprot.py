print("¡Hola querido Jugador! ¡Preparate para jugar al Ahorcado!")
print("¡Tendras un maximo de 5 intentos para adivinar la palabra secreta!")
print("Las categorias de las palabras serán: Nombres, Comida y Animales")
print("¡Buena Suerte!")

import random                           #random "sirve para generar valores aleatorios(al azar)"
def obtener_palabra_aleat():            #def "se usa para definir una función"
    palabra = ["maria", "jose", "arturo", "corviche", "salchipapa", "encebollado", "hipopotamo", "elefante", "tigre"]
    palabra_aletoria= random.choice(palabra)
    return palabra_aletoria


def mostrar_tabl(palabrasec, letrasadv): 
    tabl=""
    for letra in palabrasec:
        if letra in letrasadv:
            tabl+=letra
        else:
            tabl+="_"
    print(tabl)
    
def jugarah():
    palabrasec=obtener_palabra_aleat()
    letrasadv=[]
    intentosrest=5

    while intentosrest>0:
        mostrar_tabl(palabrasec, letrasadv)
        letra=input("Ingresa una letra: ").lower()

        if letra in letrasadv:
            print("Ya has adivinado esa letra, intenta con otra.")
            continue