#Bucle normal
""""
i = 0 
j = 0
while i < 10:  # "< es menor que" # > "es mayor que"
    i += 1
    print(i)"""

#Bucle Infinito
""""
a = 0
b = 0
while b < 10:
    a+= 1
    print(a)"""

#No se ejecuta nunca
"""
a=100
b=0
while a < 10 :
    a+=1 
    print(a)"""

#Bucle Ganador

winnumb = 21
numb = int (input("""
Adivina el numero y Gana!!!
Ingresa un numero del 1 al 100: """))
while numb != winnumb:                     #!= "es diferente de"
    print("""
          ¡Lo siento, el numero que ingresaste no es el correcto.
          Intenta de nuevo!.""")
    numb = int (input("Ingrese otro numero: "))
print("¡¡¡Felicidades, adivinaste el numero ganador!!!")

