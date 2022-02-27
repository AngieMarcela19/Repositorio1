import os
import random

secreto = random.randint(1,100)
usuario= -1
while usuario!=secreto:
    os.system('cls')
    usuario= int(input('cual es ese numero secreto: '))
    if usuario < secreto:
        print('tu numero es menor')
    elif usuario> secreto:
        print('tu numero es mayor')
    else:
        print('es el mismo, has ganado')
    input('presiona enter para continuar .... ')
input('nos vemos')