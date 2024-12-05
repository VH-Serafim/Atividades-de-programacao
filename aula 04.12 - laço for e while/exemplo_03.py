'''
   Faça um programa que solicite um valor n inteiro positivo e 
   apresente o seu correspondente em binário.
'''

import sys
num = int(input('DIgite um numero: '))

if num <= 0:
    sys.exit('Digite um valor positivo!')