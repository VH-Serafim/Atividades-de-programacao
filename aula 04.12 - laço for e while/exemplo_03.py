'''
   Faça um programa que solicite um valor n inteiro positivo e 
   apresente o seu correspondente em binário.
'''
import sys

num = int(input('DIgite um numero: '))

if num <= 0:
    sys.exit('Digite um valor positivo!')

strbinario = ''

while num > 0 :
    resto = num % 2
    strbinario = str(resto) + strbinario 
    num = num // 2
    
print(strbinario)
    