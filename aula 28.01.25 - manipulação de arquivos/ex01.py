import os 

#obtendo dirtetorio atual
strDirAtual = os.path.dirname(__file__)


strNomeArquivo = f'{strDirAtual}\\capitais_brasil.csv'

# esse arqEntrada é o que vamos manipular os dados 
arqEntrada = open(strNomeArquivo, 'r', encoding='utf-8')

strConteudo = arqEntrada.read()

arqEntrada.close()

print(strConteudo)
