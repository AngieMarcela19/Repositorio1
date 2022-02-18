#este programa suma los numeros del 1 al 6
N=int(input('ingrese un numero: '))
suma = 0 #acumulador
i= 1
while i<=N:
    suma=suma+i
    print(suma)
    i=i+1
print(suma)