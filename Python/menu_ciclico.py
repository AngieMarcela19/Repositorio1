import os #limpiar pantalla
ESP =1
ING= 2
NO_SUBS =3
SALIR =4

def mostrar_menu():
    print(f'''          subtitulos
    {ESP}) Español
    {ING}) Ingles
    {NO_SUBS}) sin subtitulos
    {SALIR}) Salir
    ''')
continuar = True
while continuar:
    os.system('cls') #limpiar pantalla
    mostrar_menu()
    opc= int(input('selecciona una opcion: '))
    os.system('cls')
    if opc ==ESP:
        print('subtitulos en español')
    elif opc ==ING:
        print('subtitulos en ingles')
    elif opc ==NO_SUBS:
        print('sin subtitulos')
    elif opc == SALIR:
        continuar = False
    else:
        print('opcion no valida')
    input('presiona enter para continuar .......')
print('nos vemos ...')
