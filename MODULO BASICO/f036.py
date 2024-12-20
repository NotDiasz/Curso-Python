"""
Desempacotamenton de Listas em Python
"""

#lista = ['Luiz', 'Miguel', 'Dias']
#n1 , n2 , n3 = lista

#print (n2)

lista = ['Luiz', 'Miguel', 'Dias',1,2,3,4,5,6]
# uma variavel pro primeiro e segundo item e o asteristico serve para criar outra lista com os outros valores e na ultima variavel eu puxei o ultimo da lista
n1 , n2 , *outralista , ultimalista = lista  

print (n2)
print(outralista)
print(ultimalista)