##Faça um programa que pergunta: o momento inicial da partida (hora e minuto) ok, o momento de chegada
##(hora e minuto), o número de segundos parados para descanso, o número de litros de combustível gasto
##(em l), o preço do litro de combustível (em R$) e a distância percorrida (em Km) ok ;

# Após receber os dados, o programa informa dados típicos de um computador de bordo:
##(a) o tempo de viagem (em segundos)( hr inicial e hr final) b) a velocidade média (Km/h) global e a velocidade média em movimento (Km/h) c) o custo da viagem com combustível  ok (em R$)d) o desempenho do carro (em Km/l, l/h e R$/Km).
 

hr_inicial = int(input('Digite a hora da partida: '))
mim_incial = int(input('digite os minutos da partida: '))
hr_final = int(input('Digite a hora da chegada no destino: '))
min_final = int(input('Digite o minuto da chegada no destino: '))
temp_parado = int(input(' Digite o tempo de descanso:  '))
combus = float(input('Digite o valor em litros do combustivel gasto:'))
vcombus = float(input('Digite o valor do combustivel:  '))
distancia = float (input(' digite a distancia total percorrida em km: '))
if hr_final > 12 or hr_final > 12 : 
    print(' Digite o valor correto')

else: 
    #converte de mim p/ seg
    seg_inicial = ((hr_inicial * 60) + mim_incial) * 60 
    seg_final = ((hr_final * 60) + min_final ) * 60

    #tempo total da viagem
    temp_total = seg_final - seg_inicial + temp_parado
    
    ## velocidade media e vm global
    vmedia = distancia / ((temp_total - temp_parado) / 60) / 60

    vmediag = distancia / ((vmedia / 60) /60)
    ## gasto com combustivel
    custo_combus =  combus * vcombus

    ## gasto de combustivel por km rodado
    km_combus = combus / distancia

    ## litro por hora
    lt_porhr = km_combus / temp_total 

    ## km por real
    gastoporkm = vcombus * km_combus


## quando a hr for negativo multiplica por -1
# vm é tempo // distancia 
    print(f'O tempo total da viagem foi {temp_total} \n A velocidade média é {vmedia} km/h \n O gasto com combustivel foi de R${custo_combus} \n o desempenho do carro foi de {km_combus}L por KM rodado \n o valor gasto em litros por hora foi de {lt_porhr: .2f}L \n o gasto em reais por km foi de R${gastoporkm}')


