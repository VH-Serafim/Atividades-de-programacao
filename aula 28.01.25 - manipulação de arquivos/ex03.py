import os 

#obtendo dirtetorio atual
strDirAtual = os.path.dirname(__file__)


strNomeArquivo = f'{strDirAtual}\\capitais_brasil.csv'

# esse arqEntrada é o que vamos manipular os dados 
arqEntrada = open(strNomeArquivo, 'r', encoding='utf-8')
lstConteudo = list()
while True:
    linha = arqEntrada.readline()
    
    if not linha: break
    linha = linha.strip().split(';')
    lstConteudo.append([ linha[0].replace('\'',''),
                         linha[1].replace('\'',''),
                         linha[2].replace('\'',''),
                         int(linha[3])])
arqEntrada.close()



print(lstConteudo)

PopulacaoRegia = map(lambda x: [x[2], 0], lstConteudo)


