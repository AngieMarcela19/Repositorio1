from re import T


def conversorcelcius(Temperatura, Unidad):
    T= float(input('ingrese la temperatura: '))
    if Unidad== "F" or Unidad== "f":
        C= print('la temperatura en grados Farenheit es:', (T*(9/5))+32)
    elif Unidad == "K" or Unidad== "k":
        C= print('la Temperatura en grados kelvin es : ', T+273)  
    else:
        print('No ha ingresado la unidad correcta')
    return C
conversorcelcius(T,"f")
