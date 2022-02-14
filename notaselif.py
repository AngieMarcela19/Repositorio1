#notas
N= float(input('ingrese su nota: '))
if N<= 50:
    R='reprobado'
elif N<=80:
    R='Aprobado'
elif N<=90:
    R='sobresaliente'
else:
    R='Excelente'
print('la nota es: ',N,R)