numero = int(input('Informe o número que você quer ver a tabuada: '))

print('Tabuada de', numero, ':')
for i in range(1, 11):
    print(f'{numero} X {i} = {numero * i}')
