# exemplos laços de repetição com while

valor = int(input('Digite um valor:'))
# exemplo de tabela de multiplicação
multiplicador = 1

print(f' Tabuada do numero {valor}: ')
while multiplicador <= 10: 
    # enquanto o valor for verdadeiro ele permanece no laço, e quando for falso ele segue com o que está abaixo do codigo 

    print(f' {multiplicador} x {valor} = { multiplicador * valor}')
    multiplicador += 1

print('fim da tabuada!')