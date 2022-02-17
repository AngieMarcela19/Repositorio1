#numeros desccendentes con while
N=int(input('ingrese un numero: '))
i=N
while i>=1:
    print(i)
    i= i-1


#numeros descendientes con for
N= int(input('ingrese un numero: '))
for i in range(N,0,-1):
    print(i)
print('ha finalizado')

#la suma de los primeros n numeros
N=int(input('ingrese un numero: '))
suma = 0 #acumula la suma
for i in range(1,N+1):
    suma =suma+i
print(suma)