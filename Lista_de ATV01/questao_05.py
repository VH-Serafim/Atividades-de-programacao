#Até duas horas: R$ 8,00/hora ou fração;
#Entre três e quatro horas: R$ 5,00/hora ou fração;
# Horas seguintes: R$ 3,00/hora ou fração.
#Depois de 12h, o custo passa a ser fixo: R$ 30,00
#Faça um programa que leia o número de minutos que um veículo permaneceu no estacionamento e exiba
#o valor a ser pago pelo responsável.
#Como exemplo, considere que o carro ficou 310 minutos no estacionamento; deve pagar: R$ 16,00 (pelas
#duas primeiras horas) + R$ 10,00 (pela terceira e quarta horas) + R$ 6,00 (pela quinta hora e fração da sexta hora): total de R$ 32,00




minuto = int(input('Digite o tempo em minutos que voce ficou no estacionamento: '))

tempo = minuto / 60
valor_pagar = 0


if tempo <= 2 :     
    valor_pagar = tempo * 8
   
elif tempo > 2 and tempo < 4 :
    valor_pagar = 16 + ((tempo - 2) * 5)

elif tempo > 4 and tempo < 12 :
    valor_pagar = 26 + ((tempo - 4) * 6)

else:
    valor_pagar = 30 + ((tempo - 12) * 6)

    

print(f'O valor a ser pago é de R${valor_pagar:.2f}')

    
    



