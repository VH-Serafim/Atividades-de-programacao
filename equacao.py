import sys
a = float(input(' digite o valor de A: '))
b = float(input(' digite o valor de C: '))
c = float(input(' digite o valor de C: '))
if a == 0: 
    sys.exit(' não é uma EQ de 2º grau!')

delta = b**2 - 4 . a . c 
## sys.exit encerra o programa
if delta < 0: 
    sys.exit(' não existem raizes reais!')

## falta os valores das raizes e o else de que não 