import sys
#saque
vsaque = float(input('Digite o valor que deseja sacar: R$ '))

if vsaque < 10 :
    sys.exit(' Digite um valor válido!')

else :
    nota_cem = vsaque // 100
    vsaque   = vsaque % 100

    nota_cinq = vsaque // 50
    vsaque    = vsaque % 50
    
    nota_vinte = vsaque // 20
    vsaque     = vsaque % 20

    nota_dez = vsaque // 10
    vsaque   = vsaque % 10

    nota_cinco = vsaque // 5
    vsaque     = vsaque % 5

    nota_dois = vsaque // 2
    vsaque    = vsaque % 2
    
    moeda_umreal = vsaque // 1
    vsaque      = vsaque % 1

    moeda_50cent = vsaque // 0.50
    vsaque       = vsaque % 0.50

    moeda_25cent = vsaque // 0.25
    vsaque       = vsaque % 0.25

    moeda_10cent = vsaque // 0.10
    vsaque       = vsaque % 0.10

    moeda_5cent = vsaque // 0.05
    vsaque      = vsaque % 0.05  

    moeda_1cent = vsaque // 0.01
    vsaque      = vsaque % 0.01

    print(f'Quantidade em notas: \n {nota_cem} de R$ 100,00 \n {nota_cinq} de R$ 50,00 \n {nota_vinte} de R$ 20,00 \n {nota_dez} de R$ 10,00 \n {nota_cinco} de R$ 5,00 \n {nota_dois} de R$ 2,00')
    print('-'*50)
    print(f'Quantidade em moedas: \n {moeda_umreal} de R$ 1,00 \n {moeda_50cent} de R$ 0,50 \n {moeda_25cent} de R$ 0,25 \n {moeda_10cent} de R$ 0,10 \n {moeda_5cent} de R$ 0,05 \n {moeda_1cent} de R$ 0,01 ')   

