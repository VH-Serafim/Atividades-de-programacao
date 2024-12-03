import sys 

num = int(input('Digite um valor: '))
if num < 0:
    sys.exit('não existe fatorial para numero negativo')

if num == 0 or num == 1: 
    sys.exit(f'{num} = 1 ')

fatorial = 1
#contador = num 
#while contador > 1 : # multiplicar por 1 não iria alterar o resultado então 
#    fatorial *= num 
#   contador -= 1 ## aqui ele diminui o valor de num pq

for contador in range(num, 1, -1):
    # nesse exemplo ele vai pegar os valores de num iniciando em 2 (pelo paremetro ser 1) e vai decrementar por conta do -1 
    fatorial *= contador

print(f'{num} = {fatorial}')