num1 = input('Digite um numero inteiro: ')

if num1.isdigit():
    num1 = int(num1)

    if num1 % 2 == 0 :
        print(f'Esse numero e par {num1}')
    else:
        print(f'Esse numero e impar {num1}')
else:
    print('Nao e um numero inteiro')

    #SEPARANDO CODES

if not num1.isdigit():
    
    print('Isso nao e um numero inteiro')
else:
    if not num1 % 2 == 0 :
        print(f'Esse numero e impar {num1}')
    else:
        print(f'Esse numero e par {num1}')