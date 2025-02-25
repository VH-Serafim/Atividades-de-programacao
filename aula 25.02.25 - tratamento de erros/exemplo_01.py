import sys, math

try: 
    valor = int(input('Digite um valor: '))
except: 
    print('valor invalido')
    print(f'Erro: {sys.exc_info()}')
else: 
    print(f'O fatorial de {valor} é {math.factorial(valor)}')



