'''
   EXEMPLO 01:
   Fazer um programa que solicite ao usuário valor inteiro positivo e em seguida
   imprima conforme o exemplo abaixo:  

   Exemplo:
   Digite um valor inteiro: 5

   1
   1 2
   1 2 3
   1 2 3 4
   1 2 3 4 5
'''

import sys

n = int(input("Digite um valor inteiro positivo: "))

if n <= 0:
   sys.exit('O número deve ser positivo...')

for i in range(n + 1):
   print(f'{i} ' * i)