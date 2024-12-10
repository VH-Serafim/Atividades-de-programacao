'''
   EXEMPLO 03:
   Fazer um programa em que o usuário informe uma string e em seguida
   o programa informe quantas palavras existem na string digitada
'''

frase = input('Informe uma frase: ')

intQTVogais = 0

intPosicao = 0
while intPosicao < len(frase):
  
   if frase[intPosicao].lower() in ' ': 
      intQTVogais += 1
   intPosicao += 1 

print(f' a frase possui {len(frase) - intQTVogais} de palavras  !')