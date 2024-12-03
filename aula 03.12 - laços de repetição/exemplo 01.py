valor = int(input('Digite um valor:'))

multiplicador = 1

print(f' Tabuada do numero {valor}: ')
#while multiplicador <= 10: 
#   print(f' {multiplicador} x {valor} = { multiplicador * valor}')
#    multiplicador += 1

for multiplicador in range(1, 11): 
    # nesse caso ele vai contar até 10 pois o in range conta até o valor anterior ao valor final EX: o range é de 11 ent o programa vai rodar até 10 
    # se informar um unico parametro ele vai considerar ele como o valor limite do programa e ele vai considerar o valor inical como 0
    # ao informar dois parametros voce delimita eles
    # ao colocar um terceiro valor, ele vai incrementar uma varaivel e soma-la aos valores do range. Ex: range(1,11,2) ele vai rodar 1,3,5,7,9 | para em 9 pois o limete do range permanece 10| 
    print(f' {multiplicador} x {valor} = { multiplicador * valor}')

print('fim da tabuada!')