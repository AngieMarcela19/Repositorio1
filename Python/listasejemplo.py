#administrar opeaaciones denttro de una lista
'''Agregar elementos a la lista
Insertar un elemento en la lista
Mostrar contenido de la lista
Buscar un elemento
Eliminar un elemento
Ordenar la lista
Limpiar la lista'''
import os
frutas =[]
AGREGAR = 1
INSERTAR =2
MOSTRAR =3 
BUSCAR = 4
ELIMINAR = 5
ORDENAR = 6
LIMPIAR = 7
SALIR = 0

def imprimir_menu():
    os.system('cls')
    print(f'''        fRUTAS
    {AGREGAR})  Agregar
    {INSERTAR}) Isertar
    {MOSTRAR}) Mostrar
    {BUSCAR}) Buscar
    {ELIMINAR}) Eliminar
    {ORDENAR}) Ordenar
    {LIMPIAR}) Limpiar
    {SALIR}) Salir ''')

#crear metodos correspondientes a esas opciones
def agregar_registro():
    print('      Agregar  ')
    nombre = input('Nombre=')
    frutas.append(nombre)
    print('registro agregado con exito.')

def insertar_registro():
    print('       Insertar')
    nombre = input('nombre =' )
    pos= int(input('Posición: '))
    frutas.insert(pos,nombre)
    print('registro insertada en la posicion indicada')

def mostrar_registro():
    print('       Mostrar')
    if len(frutas)>0: #si hay frutas 
        for fruta in frutas: #recorrer esa lista
            print(fruta)
    else:
        print('No se han agregado frutasa la lista')

def Buscar_registro():
    print('        Buscar')
    if len(frutas)>0:
        nombre = input('nombre a buscar: ')
        if nombre in frutas:
            cantidad = frutas.count(nombre) #para cada una de las veces que aparezac buscar la posicion
            Inicio= 0 #parametro de busqueda
            for i in range(cantidad): #dependiendo de cuantas veces aparezacame muestre la poscion
                pos= frutas.index(nombre,Inicio)
                print(f'{nombre} se encuentra en la posicion {pos+1}')
                Inicio= pos+1
        else:
            print(f'{nombre} no encontrado')
    else:
        print('no hay registros en la lista de frutas')

def eliminar_registro():
    print('        Eliminar')
    if len(frutas)>0:
        for i in range(len(frutas)):
            print(f'{i+1}. {frutas[i]}') #posicion
            print('0. cancelar')
            pos=int(input(f'posicion a eliminar: (1- {len(frutas)}): '))
            if 0<pos<=len(frutas):
                frutas.pop(pos-1)
                print('registro eliminado con exito')
            else:
                print('no se eliminara ningun registro')

    else:
        print('no hay registros en la lista de frutas')
def ordenar_registros():
    print('        Ordenar')
    if len(frutas)>0:
        frutas.sort()
        print('registros ordenados')
    else:
        print('no hay registros en la lista de frutas')
def Limpiar_registros():
    print('        Limpiar')
    frutas.clear()
    print('Han sido borrados')

def main():
    continuar = True
    while continuar:
        os.system('cls') #limpiar pantalla
        imprimir_menu()
        opc= int(input('selecciona una opcion: '))
        os.system('cls')
        if opc == AGREGAR:
            agregar_registro()
        elif opc ==INSERTAR:
            insertar_registro()
        elif opc ==MOSTRAR:
            mostrar_registro()
        elif opc == BUSCAR:
            Buscar_registro()
        elif opc == ELIMINAR:
            eliminar_registro()
        elif opc == ORDENAR:
            ordenar_registros()
        elif opc == LIMPIAR:
            Limpiar_registros()
        elif opc == SALIR:
            print('nos vemos ...')
        continuar = False
    else:
        print('opcion no valida')
    input('presiona enter para continuar .......')

if __name__ == 'main':
    main()







