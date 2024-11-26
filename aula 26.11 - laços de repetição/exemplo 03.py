# imprimindo valores que são divisiveis por 2 e por 3 de 1 a 100
x = 1

while x <= 100:
    if x % 2 == 0 and x % 3 == 0:
        print(x)
    x+= 1