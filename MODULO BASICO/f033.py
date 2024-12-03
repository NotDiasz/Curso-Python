"""
Listas em Python

append , insert , pop , del , clear , extend , min , max

range
"""

#lista = ['A', 'B' , 'C' , 'D' , 'E']
#print(lista[0], lista[-5])
#print(lista[0:4:2])

#l1 = [1,2,3]
#l2 = [4,5,6]
#l3 = l1 + l2
#print(l1)
#print(l2)
#print(l3)

#l1 = [1,2,3]
#l2 = [4,5,6]
#l1.extend(l2)
#print(l1)

#l1 = [1,2,3]
#l2 = [4,5,6]
#l2.append('B')
#print(l2)

#l1 = [1,2,3]
#l2 = [4,5,6]
#l2.insert(0 , 'mIGUEL')
#print(l2)
#l2.pop()
#print(l2)

#l1 = [1,2,3,4,5,6,7,8,9]
#print(l1)
#del(l1[3:5])
#print(l1)

#l1 = [1,2,3]
#l2 = [4,5,6]
#print(max(l1))
#print(min(l1))

#Aqui eu criei uma lista de 0  a 100 com multiplos de 8 uso o range para fazer o 0 a 100 e pular de 8 em 8 w o List para fazer a lista e os possiveis numeros dentro dela com o range ne 
#l2 = list(range(1,100,8))
#print(l2)

#Aqui eu apenas printei a lista
#l2 = list(range(0,100,8))
#print(l2)
#Aqui eu printei os valores dentro da Lista
#for valor in l2:
#    print(valor[1])

#l1 = [0,1,2,3,4,5,6]
#soma = 0
#for valor in l1:
#    soma = soma + valor
#print(soma,'valor da soma de todos valores da lista')

#Checagem do tipo de variaveis
#l2 = ['Str', True, 10, -20.5]
#for elem in l2:
#    print(f'O tipo do {elem} checado e {type(elem)}')

secreto = 'perfume'
digitadas = []
chances = 6

while True:
    if chances <= 0:
        print('Voce perdeu')
        break

    letra = input('Digite uma letra; ')

    if len(letra) > 1:
        print('Isso nao vale digite apenas uma letra')
        continue
    
    digitadas.append(letra)

    if letra in secreto:
        print(f'a letra [{letra}] existe na palavra secreta')
    else:
        print(f'A letra [{letra}] nao existe na palavra secreta')
        digitadas.pop

    #Aqui eu fiz a palavra indo ser descoberta pouco a pouco e mostrando ao usuario e sempre tampando com * as letras nao descobertar e assim que descoberta destampa o * na letra , esse laço for vai adicionando as letras tambem ate formar a palavra
    secreto_temp = ''
    for letra_secreta in secreto:
        if letra_secreta in digitadas :
            secreto_temp += letra_secreta
        else:
            secreto_temp += '*'
    
    if secreto_temp == secreto:
        print(f'parabens voce ganhou o jogo a palavra secreta era [{secreto}]')
        break
    else:
        print(f'A palavra secreta esta assim [{secreto_temp}]')

    if letra not in secreto:
        chances -= 1

    print(f'Voce ainda tem [{chances}] chances ')