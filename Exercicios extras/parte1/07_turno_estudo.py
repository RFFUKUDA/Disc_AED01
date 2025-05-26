print('Informe o turno em que você estuda')
print('[M]atutino')
print('[V]espertino')
print('[N]oturno')
turno = input('Opção escolhida: ').upper()

if (turno == 'M'):
    print('Bom dia!')
elif (turno == 'V'):
    print('Boa tarde!')
elif (turno == 'N'):
    print('Boa noite!')
else:
    print('Turno inválido')
