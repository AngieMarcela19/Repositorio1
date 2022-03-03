import os #limpiar pantalla
segundos_minutos =1
segundos_horas= 2
minutos_segundos= 3
minutos_horas= 4
salir = 0

def segundos_a_minutos(segundos):
    min= segundos//60
    segs= segundos % 60
    return min, segs

def minutos_a_segundos(minutos,segundos):
    segs = minutos*60 +segundos
    return segs

def minutos_a_horas(minutos, segundos):
    hrs = minutos//60
    min = minutos%60
    segs= segundos
    return hrs,min,segs

def segundos_a_horas(segundos):
    min, segs = segundos_a_minutos(segundos)
    hrs, min, segs =minutos_a_horas(min, segs)
    return hrs,min,segs


def mostrar_menu():
        print(f'''          Conversiones
    {segundos_minutos}) Segundos a minutos
    {segundos_horas}) Segundos a horas
    {minutos_segundos}) Minutos a segundos
    {minutos_horas})  Minutos a horas
    {salir}) Salir
    ''')
def main():
    continuar = True
    while continuar:
        os.system('cls') #limpiar pantalla
        mostrar_menu()
        opc= int(input('Que conversion deseas hacer?: '))
        os.system('cls')

        if opc == segundos_minutos:
            s= -1
            while 0 > s:
                s= int(input('ingrese los segundos: '))
                min, segs = segundos_a_minutos(s)
                print(f'el euivalente es {min}:{segs}')

        elif opc == segundos_horas:
            s= -1
            while 0 > s: #validacion
                s= int(input('ingrese los segundos: '))
                hrs, min, segs = segundos_a_horas(s)
                print(f'el euivalente es {hrs}:{min}:{segs}')
           
        elif opc == minutos_segundos:
            m= -1
            while 0 > m: #validacion
                m= int(input('ingrese los minutos: '))
                s= -1
                while 0> s or s >= 60:
                    s= int(input('ingrese los segundos: '))
                    segs = minutos_a_segundos(m,s)
                    print(f'el euivalente es {min}:{segs}')
        
        elif opc == minutos_horas:
            m= -1
            while 0 > m: #validacion
                m= int(input('ingrese los minutos: '))
                s= -1
                while 0> s or s >= 60:
                    s= int(input('ingrese los segundos: '))
                hrs, min, segs = minutos_a_horas(m,s)
                print(f'el euivalente es {hrs}: {min}:{segs}')
      
        elif opc == salir:
            continuar = False
        else:
            print('opcion no valida')
        input('presiona enter para continuar .......')
print('nos vemos ...')


if __name__== '__main__': 
    main()