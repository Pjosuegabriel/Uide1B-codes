print("¡Hola querido Jugador! ¡Preparate para jugar al Ahorcado!")
print("¡Tendras un maximo de 5 intentos para adivinar la palabra secreta!")
print("Las categorias de las palabras serán: Nombres, Comida y Animales")
print("¡Buena Suerte y recuerda que solo se permite una letra por intento no numeros!")

import random                   #random "sirve para generar valores aleatorios(al azar)"
def palabra_aleat():            #def "se usa para definir una función"
    palabra = ["maria", "jose", "arturo", "corviche", "salchipapa", "encebollado", "hipopotamo", "elefante", "tigre"]
    palabra_aletoria= random.choice(palabra)
    return palabra_aletoria     #return "se usa para devolver un valor desde una función y finalizar su ejecución"


def mostrar_tabl(palabrasec, letrasadv): 
    tabl=""
    for letra in palabrasec:
        if letra in letrasadv:
            tabl+=letra
        else:
            tabl+="_"
    print(tabl)


def jugarah():
    palabrasec=palabra_aleat()
    letrasadv=[]
    intentosrest=5

    while intentosrest>0:
        mostrar_tabl(palabrasec, letrasadv)
        letra=input("Ingresa una letra: ").lower()

        if letra in letrasadv: 
            print("Ya has adivinado esa letra, intenta con otra.")
            continue

        if letra in palabrasec:    
            letrasadv.append(letra)               #append "se usa para agregar un elemento al final de una lista"
            if set(letrasadv)==set(palabrasec):   #set "se usa para crear un conjunto de elementos únicos"
                print("¡Felicidades! Has adivinado la palabra secreta")
                break                             #break "se usa para salir de un bucle o una función"

        else:
            intentosrest-=1
            print(f"Letra incorrecta. Solo te quedan {intentosrest} intentos.")     #f "se usa para formatear cadenas de texto y mostrar variables dentro de ellas"
        if intentosrest==0:
            print(f"¡Lo siento has perdido! La palabra secreta era: {palabrasec},¡Sigue practicando!")

while True:     #Agrega un bucle para permitir jugar varias veces
    jugarah()
    jugar_otra_vez = input("¿Deseas jugar otra vez? (s/n): ").lower()
    if jugar_otra_vez != "s":
        print("¡Gracias por jugar! Hasta la próxima.!")
        break