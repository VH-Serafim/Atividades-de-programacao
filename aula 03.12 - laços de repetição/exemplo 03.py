
import sys 

num = int(input('Digite um valor '))
if num <= 0:
    sys.exit('informe um numero positivo')

anterior , atual = 0,1 

contador = 1
for contator in range(1, num + 1):
    print(atual, end = ',')
    anterior, atual = atual, anterior + anterior
    

#while contador <= num :
#    print(atual, end = ',')
#    anterior, atual = atual, anterior + anterior ## aqui é o exemplo de jogar o lapis
#    contador += 1