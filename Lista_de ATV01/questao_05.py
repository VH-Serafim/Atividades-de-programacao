
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


    
    



