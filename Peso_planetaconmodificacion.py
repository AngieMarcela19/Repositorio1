#este programa calcula su peso en 3 planetas
#puede escoger donde desea calcularlo
vGL= 1.62 #gravedad en luna (m/s^2)
vGT = 9.8 #gravedad en tierra  (m/s^2)
vGMart = 3.72 #gravedad en marte (m/s^2)

masa_corpo= float(input('ingrese su masa(kg):'))

planeta = input('en que lugar (Luna,Tierra,Marte) quiere calcular su peso:')

if planeta == str('Luna').lower():
    print('su peso en la luna es:',masa_corpo*vGL)
if planeta == str('Tierra').lower():
    print('su peso en tierra es:', masa_corpo*vGT, "kg")
if planeta == str('Marte').lower():
    print('su peso en marte es:',masa_corpo*vGMart)
