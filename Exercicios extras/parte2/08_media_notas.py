quantidade = 0
while (quantidade <= 0):
    quantidade = int(input('Você quer saber a média de quantas notas: '))
    if (quantidade <= 0):
        print('A quandidade deve ser positiva!')

soma = 0.0
for i in range(0, quantidade):
    nota = -1
    while (nota < 0) or (nota > 10):
        nota = float(input(f'Informe a nota {i+1}: '))
        if (nota < 0) or (nota > 10):
            print('A nota deve estar entre 0 e 10')
    soma += nota

print(f'A media das notas é {soma / float(quantidade)}')
