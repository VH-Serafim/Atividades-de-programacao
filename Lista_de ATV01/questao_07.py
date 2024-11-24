import math

ladoA = int(input('insira o valor do lado A:'))
ladoB = int(input('insira o valor do lado B:'))
ladoC = int(input('insira o valor do lado C:'))

if ladoA + ladoB > ladoC and  ladoA + ladoC > ladoB and ladoB + ladoC > ladoA:
    anguloA = math.degrees(math.acos((ladoB**2 + ladoC**2 - ladoA**2) / (2 * ladoB * ladoC)))
    anguloB = math.degrees(math.acos((ladoA**2 + ladoC**2 - ladoB**2) / (2 * ladoA * ladoC)))
    anguloC = 180 - anguloA - anguloB

    if ladoA == ladoB == ladoC:
        tipo_lado = 'Equilatero'

    elif ladoA == ladoB or ladoA == ladoC or ladoB == ladoC:
        tipo_lado = 'Isoceles'

    else:
        tipo_lado = 'Escaleno'

    if anguloA < 90 and anguloB < 90 and anguloC < 90:
        tipo_angulo = 'Agudo'
    elif anguloA == 90 or anguloB == 90 or anguloC == 90:
        tipo_angulo = 'Retangulo'
    else:
        tipo_angulo = 'obtuso'

    print(f'O triangulo é {tipo_angulo} e {tipo_lado}')

else:
    print(' Digite um valor valido!')
