N=int(input('ingresar un numero positivo: '))
while N<0:
    print('error, ingrese nueamente')
    N=int(input('ingrese un numero positivo nuevamente: '))
print('listo ha terminado')
pass

#calculo del numero de vocales en una frase 
frase = str (input('ingrese la frase: '))
frase = frase.lower()
vocales = 'aeiou'
contador =0
for i in frase:
    if i in vocales:
        contador = contador +1
print('hay', contador,' vocales en la frase')
