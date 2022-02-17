#factorial con while
'''num=int(input('calculo de factorial-** Introduzca un numero:  '))
f=1
c1=num
print(f'{num}!=' ,end='')
while c1>0:
    f=f*c1
    
    if c1==1:
        print(f' {c1} = {f}',end='')  
    else:
        print(f' {c1} x',end='')
    c1=c1-1 
       
print('')
print(f'el factorial de {num} es {f} ') '''

#factorial con for
from re import I


N= int(input('Introduzca un numero:  '))
print(f'{N}!=' ,end='')
if N <= 0:
    print('error ingrese un numero positivo')
else:
    fact = 1 #acumuladores
    for i in range(N,0-1,):
        fact= fact*i
    print('')
    print(f'el factorial de {N} ! es {fact} ')