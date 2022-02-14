sum_multiplos=0 #acumulador
count=0 #contador de los multiplos de 4
for i in range(1,101):
    if i%4 == 0:
        count+=1
        sum_multiplos+=i
        print(sum_multiplos)
        continue
print('la suma de los',count, 'multiplos de 4 es :', sum_multiplos)



