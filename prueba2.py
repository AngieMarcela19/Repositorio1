print('inicialmente guarde sus datos')

def username(usuario):
    print('su correo es :', name_user)
    return print('guardado')
name_user = str(input('ingrese su correo:' ))
ingreso_user = username(name_user) #la variable se guarda en ingreso_user

def passwor_user(contrasenia):
    print('su contraseña es:',Contra_user)
    return print('guardado')
Contra_user = input('ingrese su contraseña: ')
ingreso_Contrasenia= passwor_user(Contra_user) #la variable se guarda en ingreso_contrasenia

print('inicio')
def star(user,passw):
    print('ha iniciado session')
    return print('Bienvenido')
usuario= str(input('Ingreso de correo: '))
contrasenia = input('ingrese su contrasenia:')
while usuario!=name_user: #mientras no se cumplan estas condiciones no se admite el login
    print('ingrese nuevamente su usuario correctamente')
    usuario= str(input('Ingreso de usuario: '))
print('su usuario es correcto')
while contrasenia!=Contra_user:
    print('ingrese nuevamente su contrasenia correctamente')
    contrasenia = input('ingrese su contrasenia:')
print('su contraseña es correcto')
ingreso_oficial = star(usuario,contrasenia)

