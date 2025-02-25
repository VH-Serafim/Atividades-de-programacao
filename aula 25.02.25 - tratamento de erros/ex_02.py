import sys

try: 
    dividendo = int(input('Digite o dividendo: '))
    divisor = int(input('Digite o divisor: '))
    quociente = dividendo / divisor
except ValueError:
    print(f'Erro: Digite apenas numeros inteiros')
except KeyboardInterrupt:
    print('\n Aviso: Operação interrompida pelo usuario')
    
except: 
    print(f'Erro: {sys.exc_info()[0]}') # aqui para ver o erro em especifico

else: 
    print(f' {dividendo} / {divisor} = {quociente}')
