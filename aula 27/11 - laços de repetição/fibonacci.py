'''
   Faça um programa que solicite ao usuário um valor inteiro positivo (n)
   e imprima os n primeiros números da sequência de Fibonacci.

   exemplo:
   n = 5
   0 1 1 2 3

x = 5 
y = -3
print(x) = 5
print(y) = -3

aqui é o exemplo do jogar lapis 
x,y = y,x | troca os valores das variaveis 
agora:
   print(x) = -3
   print(y) = 5

'''

import sys 

num = int(input('Digite um valor '))
if num <= 0:
    sys.exit('informe um numero positivo')

anterior , atual = 0,1 

contador = 1

while contador <= num :
    print(atual, end = ',')
    anterior, atual = atual, anterior + anterior ## aqui é o exemplo de jogar o lapis
    contador += 1