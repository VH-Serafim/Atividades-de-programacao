'''
   EXEMPLO:
   Fazer um programa que nomes de pessoas ao usuário. O programa deverá parar de
   solicitar quando o usuário digitar FIM.
   
   Em seguida o programa deverá solicitar um nome de uma pessoa qualquer e 
   informar se esse nome consta nos nomes digitados anterioremente ou não.
'''

lstnomes = list()

while True:
    Str_Nome = input('digite um nome e para para digite "FIM"').upper()
    if Str_Nome == 'FIM': break    ## aqui encerra o laço 
    lstnomes.append(Str_Nome)

nome = input('digite um nome qualquer:').upper()

if nome in Str_Nome:
    print(f'o nome {nome} já foi digitado')
else:
    print(f'o nome {nome} não foi digitado ')