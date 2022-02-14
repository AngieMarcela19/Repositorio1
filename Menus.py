menu= """ Bienvenidos al registro de usuario
LLene los campos que usted prefiera seleccionando un  numero del 1 al 3 
[1] digitar su nombre
[2] Digitar su edad 
[3] Digitar su correo electronico"""
print(menu)
opcion=input('Digite una opcion entre  y 3: ')
if opcion == '1': # 1 entre '' porque el input anterior te devuelve un string
    nombre= input('Digita tu nombre : ')
    if nombre.isalpha()== True:
        print('tu nombre es {}'.format(nombre))
    else:
        print('has digitado un nombre no valido')
elif opcion =='2':
    edad= input('Digita su edad : ')
    if edad.isnumeric():
        print('tu edad es {}'.format(edad))
    else:
        print('has digitado una edad no valida')
elif opcion =='3':
    correo= input('Digita su correo electronico : ')
    if correo.find('@')>=0 and correo.find('.')>=0:
        print('Su correo es {}'.format(correo))
    else:
        print('Tu correo no es valido')
else:
    print('error, debes digitar un numero entre 1 y 3')
    print('=-='*20)
