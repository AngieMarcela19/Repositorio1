N= int(input('ingrese un numero: ')) #indica los primeros n Primeros numeros que desea ver
a= 0 #interruptor 1
b=1  #interruptor 2 
for i in range(1,N+1):
    resultado= print(f'{a}', end= ' ')
    #actualizar datos
    c=a+b #suma 
    a=b
    b=c