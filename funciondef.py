def saludo():
    print('Bienvenidos al curso')
saludo()
saludo()

def saludo(nombre):
    print('Bienvenido {}'.format(nombre))
saludo('sofia')
saludo('Angie')

def resta(a,b):
    return a-b
resta(5,2)

def resta(a,b):
    return a-b
c= resta(5,2) #almacenada en c
print(c)

#cuando se olvida un parametro de entradda
def resta(a=None ,b=None):
    if a ==None or b== None:
        print ("Error, debes enviar dos numeros a la funcion")
        return #te manda al ultio print
    return a-b
c= resta(5,)
print('la resta es {}'.format(c))