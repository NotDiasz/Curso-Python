frase = 'miguel e lindao'
tamanho_frase = len(frase)

contador = 0
new_str = ''
user = input('Digite uma letra que quer maior')


while contador < tamanho_frase:
    #print(frase[contador] , contador)
    
    letra = frase[contador]

    if letra == user:
        new_str += user.upper()
    else:
        new_str += letra

    print(new_str[contador] , contador)
    contador += 1


    texto = 'Python'
cont = 0

#while cont < len(texto):
   # print(texto[cont])
   # cont += 1