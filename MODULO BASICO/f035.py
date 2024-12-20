"""
Split, Join , Enumerate em Python
Split - Divide uma str
Join - Junta uma lista Str
Enumerate - Enumerar elementos da lista #list / objt iteraveis
"""

#Aqui usei o Split para separar todas palavras por espaço na lista
#string = 'O Brasil e Penta'
#lista = string.split(' ')
#print(lista)

#string = 'O Brasil e Penta'
#lista = string.split(' ')
#lista2 = string.split(',')
#print(lista2)
#print(lista)
#Esse for percorre a Lista e nos mostra quantas vezes uma palavra apareceu na lista
#for valor in lista:
#    print(f'A palavra {valor} apareceu {lista.count(valor)} ')

#Mostra a palvra que apareceu mais vezes
#string = 'O Brasil e Penta Brasil'
#lista = string.split(' ')
#lista2 = string.split(',')
#contagem = 0
#for valor in lista:
    #qtd_vezes = lista.count(valor) #Aqui e onde ele conta as palavras que mais apareceu

    #if qtd_vezes > contagem:
        #contagem = qtd_vezes
        #palavra = valor
#print (f'A palavra que apareceu  mais vezes e #{palavra} e apareceu {contagem}x')

#string = 'O Brasil e Penta Brasil'
#lista = string.split(' ')
#lista2 = string.split(',')
#for valor in lista2:
    #print(valor.strip().capitalize())#Deixa a primeira letra maiuscula o capitalize e o strip ta tirando os espaços do incio e fim e se usasse upper deixaria tudo maiusculo

#Aqui eu transformei uma frase em lista separa por espaço
#string = 'O Brasil e Penta'
#lista =  string.split(' ')  
#print(lista)

#string = 'O Brasil e Penta'
#lista =  string.split(' ')  
#for indice, valor in enumerate(lista): #Aqui eu percorro a lista mostrando o indice da lista e o que ta atribuido a indice
#    print(indice , valor)

#lista = [
#    [1,2],
#    [3,4],
#    [5,6],
#]
#for v in lista:
#    print(v[0] , v[1])

#lista = [
#    [0,'Luiz'],
#    [1,'Joao'],
#    [2,'Miguel'],
#]
#
#for indice , nome in lista:
#    print(indice, nome)

lista = [ 'Luiz' , 'Joao', 'Miguel']

for indice , nome in enumerate(lista):
    print(indice, nome)