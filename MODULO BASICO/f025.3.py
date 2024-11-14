nome = input('Digite seu nome : ')
tamanho = len(nome)

if tamanho <= 4:
    print('seu nome e muito curto')
elif tamanho <= 6 :
    print('seu nome e normal')
else:
    print('seu nome e muito grande')