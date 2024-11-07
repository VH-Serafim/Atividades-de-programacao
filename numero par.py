# codigo para verificar se um numero é par ou impar
## divisão real é / e divisão inteira é // ele pega o resto da divisão e compara com o dividendo ( não usando numero reais ou 0.5) | %  trabalha com o resto da divisão, em divisões reais/pares ele retona 0 e caso contrario retorna 1 
 

intNum = int(input('Digite um valor:')) 
# um numero é par quando o resto da divisão(%) for igual a 0
if intNum % 2 == 0:
    print(f' o numero {intNum} é par!')
else:
    print(f' o numero {intNum} é impar!')
