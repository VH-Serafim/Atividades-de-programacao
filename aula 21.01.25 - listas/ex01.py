import os, keyboard

lstAluno = list()
straviso = '\n Pressione qualquer tecla para continuar'

while True: 
    
    os.system('cis' if os.name == 'nt' else 'clear') #limpa a tela 

    nome_aluno = input("digite o nome do Aluno: ").upper().strip() # strip remove espaços antes e depois do texto(somente nas pontas)

    #verifica se o nome é FIM para sair do Laço
    if nome_aluno == 'FIM': break

    if nome_aluno == '': 
        print(f' O nome do aluno não pode ser vazio, {straviso}')
        keyboard.read_event()
        continue

    while True:
        intNota_1 = int(input('Digite a primeira nota do aluno: '))
        if intNota_1 < 0 or intNota_1 > 100:
           print(f'Nota invalida! {straviso}')
           keyboard.read_event()
        else: break



    while True:
        
        intNota_2 = int(input('Digite a primeira nota do aluno: '))
        if intNota_2 < 0 or intNota_2 > 100:
           print(f'Nota invalida! {straviso}')
           keyboard.read_event()
        else: break
        

    lstAluno.append([nome_aluno, intNota_1, intNota_2])


#________________________________________________________________
#TODO implementar a ordem alfabetixca na lista
#_______________________________________________________________
#


for nome_aluno in lstAluno:

    fltmedia = (nome_aluno[1]*2 + nome_aluno[2]*3) / 5

    strSituacao = 'REPROVADO!'
    if fltmedia >= 59.5: strSituacao = 'Aprovado'

    print(f'Aluno: {lstAluno[0]} | Nota 1: {lstAluno[1]} | Nota 2: {lstAluno[2]} | Média: {fltmedia: .0f} | Situação: {strSituacao}')
    


