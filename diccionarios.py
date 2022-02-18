#diccionario
edades={'David':20,'sofia':17}
print(edades['sofia'])# uestra el valor depositado en la clave
edades['David']=100
print(edades)

#diccionario de natas
notas = {'david':85,'carlos':60,'victor':98,'hecto':75}
notas.clear()
print(notas) # uso del diccionario.clear()


#uso del diccionario.copy()
notas = {'david':85,'carlos':60,'victor':98,'hecto':75}
notas_2= notas.copy()
print(notas_2)


#convertir de lista a valor , asignando el mismo valor  alas claves
notas=dict.fromkeys(['david','carlos','victor','hecto'],100)
print(notas)

#regresa el valor de la clave diccionario.get()
notas = {'david':85,'carlos':60,'victor':98,'hecto':75}
print(notas.get('david')) 

#items los separa como listas de pares 
notas = {'david':85,'carlos':60,'victor':98,'hecto':75}
items=notas.items()
print(items)

#keys devuelve el valor de las claves
notas = {'david':85,'carlos':60,'victor':98,'hecto':75}
print(notas.keys())


#diccionario1.update(diccionario2)
dic1 = {'A':1,'B':2,'C':3,'D':4}
dic2 ={'E':5,'F':6,'G':7,'H':8}
dic1.update(dic2)
print(dic1)


#value() regresa una lista con valores
dic1 = {'A':1,'B':2,'C':3,'D':4}
value = dic1.values()
print(value)