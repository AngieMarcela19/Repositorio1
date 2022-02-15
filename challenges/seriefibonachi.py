N= int(input('ingrese un numero: ')) #indica los primeros n Primeros numeros que desea ver
a= 0
b=1 
for i in range(1,N+1):
    resultado= print(f'{a}', end= ' ')
    c=a+b #suma 
    a=b
    b=c