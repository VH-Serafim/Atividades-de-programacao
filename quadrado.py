base = float(input('Digite o numero da base do quadrado: '))
altura = float(input(' Digite o numero da altura do quadrado: '))
# a base e altura tem que ser >= 0 para quadrilateros 
if base <= 0:
    print(' a base deve ser positiva!')
elif altura <= 0: 
    print(' a altura deve ser positiva!')
elif base == altura: 
    print(' é um quadrado!')
else: 
    print(' é um retangulo!')