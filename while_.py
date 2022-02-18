nombre= input('cual es tu nombre:? ')
print(nombre.strip().upper())
print(nombre.strip().lower())
print('=='*25)
print('tu nombre tiene',  len(nombre)-nombre.count(' ') , 'letras sin contar espacios')
nombre1 = nombre.split()
print(nombre1)
print('el primer nombre tiene' ,len(nombre1[0]),'letras')

#par normal
n1 = int(input('ingrese un numero: '))
for i in range(1,n1+1):
    if i%2 ==0:
        print(f'{i} es par')

#par continue
n1 = int(input('ingrese un numero: '))
for i in range(1,n1+1):
    if i%2 ==0:
        continue #salta a la siguiente funcion ue no sea par
        print(f'{i} es par')
    else:
        print(f'{i} es impar')

#par break
n1 = int(input('ingrese un numero: '))
for i in range(1,n1+1):
    if i%2 ==0:
        break #sale del ciclo
        print(f'{i} es par')

#seleccionar los impares y terminar al encontrar el primer numero divisible por 6
n1 = int(input('ingrese un numero: '))
for i in range(1,n1+1):
    if not(i%2) & (i%6):
        continue
    if i% 6== 0:
        break
        print(f'{i} es divisible por 6')
