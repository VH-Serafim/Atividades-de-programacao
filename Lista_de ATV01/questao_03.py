
hr_inicial  = int(input('Digite a hora da partida: '))
mim_incial  = int(input('Digite os minutos da partida: '))
hr_final    = int(input('Digite a hora da chegada no destino: '))
min_final   = int(input('Digite o minuto da chegada no destino: '))
temp_parado = int(input('Digite o tempo de descanso (em segundos):  '))
combus_gasto      = float(input('Digite o valor em litros do combustivel gasto:'))
vcombus     = float(input('Digite o valor do combustivel:  '))
distancia   = float (input('Digite a distancia total percorrida em km: '))

# conversão para segundoos
segsPartida = (hr_inicial * 3600) + (mim_incial  * 60)
segsChegada = (hr_final * 3600) + (min_final * 60)

#Calculando tempo de viagem
tempViagem = segsChegada - segsPartida

if segsChegada > segsPartida:
    tempViagem += 24 *3600
    # calculo para que o resultado não dê um valor negativo em viagens que aconteçam de um dia p/ outro

    #Calculando a velocidade média total
    vmedia = distancia / (tempViagem / 3600)

    #Calculando a velocidade média em movimento
    velMediaMov = (distancia / ((tempViagem / 3600)- temp_parado)) * 1

    #Calculando o custo total da viagem
    custoViagem = combus_gasto * vcombus

    #Calculando o custo total da viagem
    custo_combus = combus_gasto * vcombus

    #Calculando o desempenho em Km/L
    km_combus = distancia / combus_gasto

    #Calculando o desempenho em L/h
    lt_porhr = combus_gasto / (tempViagem / 3600)

    #Calculando o desempenho em R$/Km
    gastoporkm = custo_combus / distancia
print('-----'*3)
print(f'O tempo total da viagem foi {tempViagem} \n A velocidade média total é {vmedia} km/h \n A velocidade media em movimento foi de {velMediaMov}\n O gasto com combustivel foi de R${custo_combus} \n O desempenho do carro foi de {km_combus}L por KM rodado \n O valor gasto em litros por hora foi de {lt_porhr: .2f}L \n O gasto em reais por km foi de R${gastoporkm}')


