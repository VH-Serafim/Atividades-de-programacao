'''
   Faça um programa que solicite um valor n inteiro positivo e 
   imprima na tela o seguinte padrão:

   para n = 4

   o programa deverá imprimir

   1
   2 2
   3 3 3
   4 4 4 4
'''
import sys
num = int(input('DIgite um numero: '))

if num <= 0:
    sys.exit('Digite um valor positivo!')

contador = 1

while contador < num:
    
