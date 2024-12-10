'''
   EXEMPLO 01:
   Fazer um programa em que o usuário informe uma string e em seguida
   o programa informe quantos carateres existem na string digitada
'''
frase = input('Informe uma frase:')

# primeiro metodo, a funçao len retorna a quantidade de caracteres digitados, tudo o que estiver na string vai ser contado
print(f'A frase informada possui {len(frase)} caracteres!')