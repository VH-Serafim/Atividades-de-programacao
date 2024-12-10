'''
   Faça um programa que solicite ao usuário um valor n inteiro positivo e 
   imprima os n primeiros trios de valores que formam um triângulo pitagórico.
o menor triangulo pitagorico é 3,4,5
um triangulo é pitagorico quando a² + b² = c²
o C sempre é o maior lado 
vai ser um for pra A e pro B e o C+1

'''

import sys
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

if a <= 0 or b <= 0 or  c <= 0:
    sys.exit('Digite um valor positivo!')