#saludo personalizado
def saludo_per(nombre):
    print(f'gusto en verte {nombre}')

def main(): # otro procedimiento #el llamado hacia los demas procedimientos
    usuario= input('hola, como te llamas ?: ')
    saludo_per(usuario)

if __name__== '__main__': #se sugiere ese metodo
    main() #estructura selectiva para evaluar si es es el que se esta llamando