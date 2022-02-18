#verificar un numero es + 0 -
from tkinter import Radiobutton


N= int(input('ingrese un numero: '))
if N<0:
    R= 'negativo'
else:
    if N==0:
        R='Neutro'
    else:
        R='positivo'
        print('el numero es:',R)