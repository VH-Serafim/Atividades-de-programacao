import sys
num = int(input('DIgite um numero: '))

if num <= 0:
    sys.exit('Digite um valor positivo!')

cont_primos = 0
n_primo = 2

while cont_primos < num: 
    cont_divisores = 0
    for i in range(1,n_primo +1):
        if n_primo % i == 0: ## cada vez que o numero for divisivel por i ele vai adicionar ao contador de divisores 
            cont_divisores += 1
            
    if cont_divisores == 2:
        print(n_primo)
        cont_primos += 1
    n_primo +=1