dia_inicial = int(input('Informe o dia incial: '))
mes_inicial = int(input('Informe o mês inicial: '))

dia_final = int(input('Informe o dia final: '))
mes_final = int(input('Informe o mês final: '))



if mes_inicial == mes_final:
    diferenca_dias = dia_final - dia_inicial
else:
    diferenca_dias = ((mes_final - mes_inicial) * 30) - (dia_final - dia_inicial)

print (f'Passaram-se {diferenca_dias} dia(s).')