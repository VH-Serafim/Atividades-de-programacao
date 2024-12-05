'''
   Faça um programa que solicite ao usuário um valor n inteiro positivo e 
   imprima os n primeiros trios de valores que formam um triângulo pitagórico.
'''

import sys
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

if a <= 0 or b <= 0 or  c <= 0:
    sys.exit('Digite um valor positivo!')