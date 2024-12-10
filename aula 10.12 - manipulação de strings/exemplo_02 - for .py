'''
   EXEMPLO 02:
   Fazer um programa em que o usuário informe uma string e em seguida
   o programa informe quantas vogais existem na string digitada
'''

frase = input('Informe uma frase: ')

intQTVogais = 0
#o for pega cada posição da stirng por vez 
for caractere in frase:
    if caractere.lower() in 'aeiou':
      intQTVogais += 1 
    
print(f'A frase possui {intQTVogais} vogais! e possui {len(frase) - intQTVogais} de consoantes!')
