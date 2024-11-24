#Até duas horas: R$ 8,00/hora ou fração;
#Entre três e quatro horas: R$ 5,00/hora ou fração;
# Horas seguintes: R$ 3,00/hora ou fração.
#Depois de 12h, o custo passa a ser fixo: R$ 30,00
#Faça um programa que leia o número de minutos que um veículo permaneceu no estacionamento e exiba
#o valor a ser pago pelo responsável.
#Como exemplo, considere que o carro ficou 310 minutos no estacionamento; deve pagar: R$ 16,00 (pelas
#duas primeiras horas) + R$ 10,00 (pela terceira e quarta horas) + R$ 6,00 (pela quinta hora e fração da
#sexta hora): total de R$ 32,00




tempo = int(input('Digite o tempo em minutos que voce ficou no estacionamento: '))

valor_pagar = 0




if tempo <= 60 :     
    valor_pagar += 8
    print(f'O valor a ser pago é de R${valor_pagar}')

elif tempo <= 120 :
    valor_pagar += (8*2)
    print(f'O valor a ser pago é de R${valor_pagar}')

elif tempo <= 180 :
    valor_pagar += 5
    print(f'O valor a ser pago é de R${valor_pagar}')

elif tempo <= 240 :
    valor_pagar += (5*2)
    print(f'O valor a ser pago é de R${valor_pagar}')
    
    



