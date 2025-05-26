preco1 = int(input('Informe o primeiro preço: '))
preco2 = int(input('Informe o segundo preço: '))
preco3 = int(input('Informe o terceiro preço: '))

if (preco1 == preco2) and (preco1 == preco3):
    print('Pode comprar qualquer um, ja que os preços são iguais.')
elif (preco1 < preco2) and (preco1 < preco3):
    print('Compre pelo primeiro preço')
elif (preco2 < preco3):
    print('Compre pelo segundo preço')
else:
    print('Compre pelo terceiro preco')
