'''
   EXEMPLO 04:
   Fazer um programa em que o usuário informe uma palavra e em seguida
   o programa exiba a palavra invertida e diga se ela é um palíndromo ou não.
'''

palavra = input('digite uma palavra: ')

palavra_inv = ''
 # o len é -1 para pegar a ultima letra da ultima posição da string e dps sucessivamente as outras para poder comparalas 
for letra in range(len(palavra) - 1, -1, -1):
   palavra_inv += palavra[letra]
if palavra.lower() == palavra_inv.lower():
   print(' É um palindromo!')
else: 
   print(' não é um palindromo!')

