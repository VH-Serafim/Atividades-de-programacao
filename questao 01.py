

# fFaça um programa que aceita um número de até 4 dígitos (0 a 9999) e exiba a soma dos seus algarismos.
numero = int(input('digite um valor: '))
if numero <= 0:
    print(' digite um valor acima de 0 ')
elif numero > 9999: 
    print('digite apenas numeros abaixo 9999!')
else:
    
    milh = numero //1000
    numero = numero % 1000

    cen = numero// 100
    numero = numero % 100

    dec = numero // 10
    numero = numero % 10

    und = numero // 1 
    numero = numero % 1

    somageral = milh + cen + dec + und

    print(f' o valor digitado foi {numero} e a soma dos seus algarismos é {somageral}')
