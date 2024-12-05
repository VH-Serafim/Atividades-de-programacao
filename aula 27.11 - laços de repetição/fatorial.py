'''
   Fazer um programa que solicite ao usuário um valor inteiro e calcule
   o fatorial desse número. O fatorial de um número é calculado pela
   multiplicação desse número por todos os seus antecessores até o número 1.

   Exemplo: 5! = 5 * 4 * 3 * 2 * 1 = 120
'''

import sys 

num = int(input('Digite um valor '))
if num < 0:
    sys.exit('não existe fatorial para numero negativo')

if num == 0 or num == 1: 
    sys.exit(f'{num} = 1 ')

fatorial = 1
contador = num 
while contador > 1 : # multiplicar por 1 não iria alterar o resultado então 
    fatorial *= num 
    contador -= 1 ## aqui ele diminui o valor de num pq
print(f'{num} = {fatorial}')
