salario = float(input('Informe o valor do salário do colaborador: '))

if (salario <= 280):
    percentual = 20
elif (salario <= 700):
    percentual = 15
elif (salario <= 1500):
    percentual = 10
else:
    percentual = 5

aumento = salario * (percentual / 100.0)
novo_salario = salario + aumento

print('Salario antes do reajuste:', salario)
print('Percentual de aumento:', percentual, '%')
print(f'Valor do aumento: {aumento:.2f}')  #formata com apenas 2 casas decimais
print('Novo Salario:', novo_salario)
