import random
from ast import While


def Usuario(name):
    print('Su nombre de usuario es :',user)
    return print('Bienvenido', user)
user= input('Ingrese su usuario: ')
Usuario(user)
#Settings Words
print('\n')
print('contamos con los mundos:')
print('\n')
print('La cicatriz de cristal = designado por 1\nEl abismo de los lamentos = designado por 2\nLa grieta del invocador =  designado por 3\nEl bosque retrocido = designado por 4')
def campo_dejusticia(mundo):
    print('Puede escoger su Rol en el juego')
Campo= int(input('En que campo desea entrar: ')) 
if Campo ==1:
    print('usted ha ingresado en La cicatriz de cristal  ')
if Campo ==2:
    print('usted ha ingresado en El abismo de los lamentos')
if Campo == 3:
    print('usted ha ingresado en La grieta del invocador')
if Campo==4:
    print('usted ha ingresado El bosque retrocido')
campo_dejusticia(Campo)
print('\n')
for Role in ["Asesino = 1","Luchador= 2","Mago =3","Tirador= 4","Soporte=5"]:
    print('Puede escoger el rol',Role)
def Roles(Rol):
    return print('Puedes comenzar la batalla')
Rol= int(input( 'Ahora que rol que desea tener: '))
nivel_vidamin= 20
nivel_vidamax= 100
nivel_podermin = 40
nivel_podermax =100
nivel_poder=random.randint(nivel_podermin,nivel_podermax)
nivel_vida=random.randint(nivel_vidamin,nivel_vidamax)
if Rol==1:
    print('Eres un Asesino, con un nivel de vida', nivel_vida, 'y nivel de poder de', nivel_poder)
if Rol==2:
    print('Eres un Luchador con un nivel de vida', nivel_vida, 'y nivel de poder de', nivel_poder)
if Rol==3:
    print('Eres un Mago con un nivel de vida', nivel_vida, 'y nivel de poder de', nivel_poder)
if Rol==4:
    print('Eres un Tirador con un nivel de vida', nivel_vida, 'nivel de poder de', nivel_poder)
if Rol==5:
    print('Eres de soporte con un nivel de vida', nivel_vida, 'y nivel de poder de', nivel_poder)
Roles(Rol)
ruta1=random.choice(["moverte a la derecha", "moverte a la izquierda", "sigue tus compañeros"])
print('Lo primero que vas a hacer es:', ruta1)
if ruta1=="moverte a la derecha":
    ingresa1= int(input('Ingresa un numero positivo para avnazar y un numero negativo para quedarte cerca de una torre: '))
    if ingresa1 >0:
        print('Te has encontrado con tu equipo')
    print('necesitas avanzar hay un enemigo cerca')
if ruta1=="moverte a la izquierda":
    print('o no te has encontrado con un enemigo')
    print('huye de ahi')
    ruta1p= input('Que deseas hacer 1 para pelear 2 pedir ayuda: ')
    if ruta1p ==1:
        print('pelea')
    if ruta1p==2:
        print('Pronto llegaran los refuerzos')
else:
    ruta1=="sigue tus compañeros"
    print('sigue con tu equipo avanza y destruye torres')
print('tengos sueño, quieres salirte?')
for i in [ruta1]:
    print('despues de', ruta1, 'bye, espero que te haya gustado el juego')




