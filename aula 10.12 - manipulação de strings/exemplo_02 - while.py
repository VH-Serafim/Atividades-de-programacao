'''
   EXEMPLO 02:
   Fazer um programa em que o usuário informe uma string e em seguida
   o programa informe quantas vogais existem na string digitada
'''

frase = input('Informe uma frase: ')

intQTVogais = 0

#percorre cada caractere digitado

intPosicao = 0
while intPosicao < len(frase):
   # if frase[intPosicao] in 'aeiouAEIOU':
   if frase[intPosicao].lower() in 'aeiou': # aqui ele converte td a string para minusculo e compara com as do if
      intQTVogais += 1
   intPosicao += 1 

print(f'A frase possui {intQTVogais} vogais! e possui {len(frase) - intQTVogais} de consoantes!')
