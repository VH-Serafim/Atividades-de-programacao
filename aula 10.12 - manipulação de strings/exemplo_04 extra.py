# esse exemplo é exclusivo para python!
palavra = input('Digite uma palavra: ')

if palavra.lower() == palavra[:: -1].lower():
    print(' É um palindromo!')
else: 
    print('não é um palindromo!')