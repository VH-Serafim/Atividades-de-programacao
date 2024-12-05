# numeros primos são os divisiveis por ele mesmo e por 1 
# Ex:
import sys

num = int(input('Digite um valor:'))
 # num é o parametro final
if num <= 0:
    sys.exit('digite um valor maior que 0!')

contador = 1
while contador < num:
    for contador in range(1, num +1):
        if num // 1 == 1 and num // num == 0: 
            print()     
