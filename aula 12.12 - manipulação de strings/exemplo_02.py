'''
   EXEMPLO 02:
   Fazer um programa em que o usuário informe duas palavras e em seguida
   informe se elas são anagramas.
   
   Anagrama: é uma palavra ou frase formada pela transposição das letras de outra 
   palavra ou frase. 
dicas: sorted() p/ ela ordena a string no ex da iracema vai trans
usar len pra verificar se ambas tem a mesma quantidade de caracteres 
usar o .lower pra comprarar  
subs
remover os espaços antes de ordernar tirando os espaços em branco com a função replace()

'''
p1 = 'iracema'
p2 = 'america'

# remove os espaços
p1s = p1.replace(' ','')
p2s = p2.replace(' ','')

p1s = sorted(p1s).lower()
p2s = sorted(p2s).lower()

# p1s = sorted(p1.replace(' ','')).lower()
if sorted(p1).lower() == sorted(p2).lower():
    