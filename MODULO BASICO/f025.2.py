hora = int(input('Quantas horas sao agora : '))

if (hora > 0 and hora <= 11) :
    print('Bom Dia')
elif (hora > 11 and hora < 17):
    print('Boa Tarde')
else:
    print('Boa Noite')