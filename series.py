#multiplos de 3
N= int(input('Ingrese un numero: ')) #cuantos elementos quieres visualizar al generar la serie
m= 3 #interruptor
for i in range(1,N+1):
    print(m, end =' ')
    m=m+3

# serie 4,3,2,1,4,3,2,1
from wsgiref.handlers import IISCGIHandler


N= int(input('Ingrese un numero:' ))
Controlador = 0
w =4 #interruptor
while Controlador < N:
    print(f'{w}', end=' ')
    if w > 1:
        w = w-1
    else:
        w=4
    Controlador= Controlador+1

 #serie A,B,A,B,A,B
N= int(input('Ingrese un numero:' ))
w= 0
for i in range(1,N+1):
    if w== 0:
        print('A')
        w=1
    else:
        print('B')
        w=0 

#serie fibonacci
N= int(input('Ingrese un numero:' ))
w= 0 #interruptor 1
w1=1 #interruptor 2
s= 0 #acumulador
c= 0 #contador
if N<=0:
    print('dato erroneo')
elif N==1:
    print(w)
else:
    while c<N:
        print(w)
        s= w+w1
        #actualizar datos
        w= w1
        w1=s
        c= c+1
