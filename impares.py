#identificar pares e inmpares
n1= int(input('ingrese un numero:'))
n2= int(input(f'ingrese un numero mayor que {n1}:'))
if n2 < n1:
    print(f'ingrese un numero mayor que {n1}')
else:
    for i in range(n1,n2+1):
        if i % 2 ==0:
            print(i,'es par')
        else:
            print(i,'es impar ')
            
# de n1 a n2 me va a inspeccionar cuales son pares e impares
