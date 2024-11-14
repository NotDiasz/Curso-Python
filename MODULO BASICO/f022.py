#LEN E CHECAGEM DE CARACTERES

user = input('Digite nome de Usuario')
qtd_char = len(user)

print(user , qtd_char, ' CARACTERES ' , type(qtd_char))

if qtd_char <= 6:
    print('Digite no minimo 6 caracteres')
else:
    print('Voce foi Registrado no Sistema')


#SOMA DE CARACTERES

str1 = input('Digite um nome')
str2 = input('Digite um nome')

print(f'Soma de Carcteres {len(str1) + len(str2)}')