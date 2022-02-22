#Calcular IMC
def calcular_IMC():
    peso=float(input('ingrese su peso: '))
    estatura= float(input('ingrese su altura: '))
    IMC= peso/estatura**2
    return IMC
imc = calcular_IMC()
print(f'tu indice de masa corporal es {imc:.4f}') #notacion :.4f muestra solo 4decimales


#funciones con argumentos
# Calcular area del triangulo
def calcular_area_triangulo(base,altura):
    return base*altura/2
print('ingresa los siguientes valores')
base= float(input('ingrese la base del triangulo: '))
altura =float(input('ingrese la altura del triangulo: '))
print(f'area = {calcular_area_triangulo(base,altura)}')


#imc con argumentos dentro de la funcion
def calcular_IMC(peso,estatura):
    return peso/(estatura**2) #fuera de la funcion hacer la peticion de datos
print('calcula el indice de masa corporal')

p=float(input('ingrese su peso: '))
e= float(input('ingrese su altura: '))
print(f'IMC = {calcular_IMC(p,e)}')

# de segundos a min y  su equivalnte
def convertir_tiempo(segundos):
    m=segundos//60
    s= segundos % 60
    return m,s
print('esto convierte de seg a min y su equivalente')

seg= float(input('ingrese los segundos: '))
min, segu =convertir_tiempo(seg)  #en la variable min se va a guardar lo que se segrese en m
print(f'el equivalente es {min}:{segu}')

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