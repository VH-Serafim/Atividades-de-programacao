import os 

#obtendo dirtetorio atual
strDirAtual = os.path.dirname(__file__)


strNomeArquivo = f'{strDirAtual}\\resum_cpt_de-areia.txt'

# esse arqEntrada é o que vamos manipular os dados 
arqEntrada = open(strNomeArquivo, 'r', encoding='utf-8')

lstConteudo = arqEntrada.readlines()

arqEntrada.close()

print(lstConteudo)

