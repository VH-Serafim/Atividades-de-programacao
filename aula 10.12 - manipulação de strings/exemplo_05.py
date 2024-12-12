'''
   EXEMPLO 05:
   Fazer um programa em que o usuário informe uma string e depois uma palavra
   e em seguida o programa informe se a palavra informada está na string informada
'''

frase = input('Digite a uma frase: ')

palavra = input('Digite uma palavra: ')

if palavra.lower() in frase.lower():
   print(f'a palavra {palavra} está na frase! ')
else: 
   print(f'a palavra {palavra} não está na frase!')