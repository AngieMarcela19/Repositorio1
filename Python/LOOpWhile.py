#Mostrar números con un ciclo. del 0 al 13
print('este programa te muestra los numeros del 0 al 13')
i= 0 #contador
while i <= 13:
    print(f'contador: {i}')
    i= i+1
else:
    print('he terminado de contar')

#script en python que suma valores pares y multiplica valores impares mientras el usuario no ingrese
#un 0 
Acumulador_1 = 0 #suma
Acumulador_2 = 1 #multiplicacion
Numero = 1
while Numero != 0:
    Numero = int(input('ingrese un numero (0 para salir): '))
    if Numero % 2 == 0:
        Acumulador_1 = Numero + Acumulador_1
    else:
       Acumulador_2 =Numero*Acumulador_2
    print(f' la suma da {Acumulador_1}')
    print(f'la multiplicacion da {Acumulador_2}')

    #validacion de datos
import os
USER = "amarcela"
PASSWORD = "12345"

Username = ""
contraseña = ""

while USER!= Username or PASSWORD!= contraseña:
    os.system("cls")
    Username = input("ingrese usuario: ")
    contraseña = input("Ingrese Contraseña: ")

    if USER!= Username or PASSWORD!=contraseña:
        print("Error")
        print("intente de nuevo")
        input("presiona enter para continuar")

else:
    print("ha ingresado con exito")
input("nos vemos...")

# menu con diferentes personajes de videojuegos
import os
MAGO = 1
GUERRERO = 2
SACERDOTISTA= 3
SALIR = 4

#bandera
Continuar = True
while Continuar:
    os.system('cls')
    print(f'''          personajes
    {MAGO} ) Mago
    {GUERRERO}) Guerrero
    {SACERDOTISTA}) Sacerdotista
    {SALIR}) Salir''')
    opc= int(input('selecciona tu personaje:'))
    if opc== MAGO:
        print(''' 
        Fuerza: 15
        Energia: 20
        Especial: 12
        ''')
    elif opc== GUERRERO:
        print(''' 
        Fuerza: 20
        Energia: 40
        Especial: 30
        ''')
    elif opc==SACERDOTISTA:
         print(''' 
        Fuerza: 2
        Energia: 14
        Especial: 10
        ''')
    elif opc== SALIR:
        Continuar= False
    else:
        print('opcion Incorrecta')
    input('presiona enter para continuar') #por si se equivoco
print('Bienvenido al juego') 
