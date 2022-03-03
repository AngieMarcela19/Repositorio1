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

#version 2 competitiva
import os
import random
inferior = 0
superior = 100
secreto = random.randint(1,100)
usuario= -1
maquina= 0
while usuario!=secreto and maquina!= secreto:
    os.system('cls')
    maquina= random.randint(inferior, superior)
    print(f' el valor de la maquina es {maquina}')

    if maquina < secreto:
        print('tu numero es menor')
        inferior = maquina +1
    elif maquina> secreto:
        print('tu numero es mayor')
        superior = maquina - 1
    else:
        print('es el mismo, has ganado maquina')

    if maquina!= secreto:
        usuario= int(input('cual es ese numero secreto: '))
        if usuario < secreto:
            print('tu numero es menor')
        elif usuario> secreto:
            print('tu numero es mayor')
        else:
            print('es el mismo, has ganado usuario')
    input('presiona enter para continuar .... ')
input('nos vemos')