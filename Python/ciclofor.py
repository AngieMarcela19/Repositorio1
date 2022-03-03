#numeros desde el 0 al 13
print('programa ue muestra los numeros del 1 al 13')
for numero in range(0,14):
    print(f'{numero}')

#imprimir numeros pares

for pares in range(20):
    if pares % 2 == 0:
        print(f'{pares}')
else:
    print('terminamos')

#cuenta regresiva
import os
import time
for indice in range(13,1,-1):
    os.system('cls')
    print(f'{indice}') 
    time.sleep(1)

#tabla de multiplicar
N1= int(input('que numero deseas ver la tabla de multiplicar?: '))
limite= int(input('hasta que multiplo deseas ver?: '))
for multiplo in range(1,limite+1):
    print(f'tabla de multiplicar del {N1}')
    print(f'{N1}x {multiplo} = {N1*multiplo} ')

#tablas de multiplicar del  al 10
import os
for numero in range(1,11):
    os.system('cls')
    print(f'tabla de multiplicar del {numero}')
    for multiplo in range(1,11): #este for se encarga de aumentar ese multiplo
        print(f'{numero}x {multiplo}= {numero*multiplo}')
    input('presiona enter para continuar....')
print('-'*20)

for palabra in ('hola'):
    print(palabra)

Acumulador = 0
print('vamos a calcular un promedio')
total_datos= int(input('cantidad de datos a registrar:' ))
for valor in range(total_datos):
    numero = int(input(f'ingresa el valor {valor+1}:'))
    Acumulador+= numero
promedio= Acumulador/total_datos



