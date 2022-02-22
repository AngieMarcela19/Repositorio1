#menu generico
def menu(titulo,*args,**kwargs):
    print(f'        {titulo}')
    for i in range(len(args)): #serie de opciones que vienen en los args
        print(f'{i+1}) {args[i]}') #un for para recorrer esos argumentos por indice #posicion i+1 para que empiece en 1 en la lista de argumentos el que este en la posicion i
    opc= int(input('selecciona una opcion:  '))
    if 1<= opc <= len(args): #esa opc y es menor que la cantidad de argumentos
        print(f'seleccionaste la opcion {args[opc-1]}') #las listas comienzan en cero
    else:
        print('opcion no validad')
        if 'error' in kwargs:
            print(f'{kwargs["error"]}')
menu('operaciones aritmeticas', 'suma', 'resta', 'multiplicacion', error ='no existe tal opcion')
print('nos vemos')