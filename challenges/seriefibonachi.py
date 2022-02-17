N= int(input('ingrese un numero: ')) #indica los primeros n Primeros numeros que desea ver
def serie(N):
    a= 0 #interruptor 1
    b=1  #interruptor 2
    resultado= [] 
    for i in range(1,N+1):
        resultado.append(a)
         #actualizar datos
        c=a+b #suma 
        a=b
        b=c
    print(resultado)
serie(N)