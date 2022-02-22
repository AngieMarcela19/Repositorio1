# Ejemplo: Procedimiento con dos argumentos
import os
def verificar_edad(nombre, edad):
    os.system('cls')
    if edad >=18:
        print(f'{nombre}, eres mayor de edad')
    else:
        print(f'{nombre} eres menor de edad')

nombre= input('ingresa tu nombre: ')
edad = int(input('ingresa tu edad:')) 
verificar_edad(nombre,edad)
print('nos vemos')

#procedimiento 2 Tabla de multiplicar y argumento con valor por omisión
def tabla_multiplicar(numero, hasta):
    print(f'tabla de multiplicar {numero}')
    for i in range(hasta+1):
        print(f'{numero}* {i}= {numero}*{i}')
numero= input('ingrese un numero: ')
hasta = 10
tabla_multiplicar(numero,hasta)



