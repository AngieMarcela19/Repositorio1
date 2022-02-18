#tabla de multipilicar
N= int(input('ingrese un numero: '))
i=0
while i<=10:
    M=N*i
    i=i+1
    print(M)

#tabla de multiplicar con for
N= int(input('ingrese un numero: '))
for i in range(11):
    print(N,'x',i,'=', N*i)
    
#ejercicio mayor al anterior 
valor = int(input('cuantos valores va a introducir? : \n'))
if valor <1 :
    print('¡Error!')
else:
    primero= int(input('escriba un numero: '))
for i in range(valor,0,-1):
    numero = int(input(f'escriba un numero mas grande que el {primero}:'))
    if numero >= primero:
        print(f'el {numero} es mayor quw {primero}')
    else:
        print(f'el {numero} es el menor')
    primero = numero #el primero se va cambiando 
print('ha terminado el ejercicio')
        