"""
For / Else em Python
"""

#variavel = ['Miguel' , 'Dias' , 'Mendes']
#Aqui estou percorrendo a lista e printando valor por valor
#for valor in variavel:
 #   print(valor)
     
     #Aqui estou fazendo verificaçao em minha list quais nomes começam com a letra D
#variavel = ['Miguel' , 'Dias' , 'Mendes']
#for valor in variavel:
#    if valor.startswith('D'):
#      print(f'Começa com D o [{valor}]')
#    else:
#      print(f'Nao começa com D [{valor}]')

#variavel = ['Miguel', 'Dias' , 'Mendes']
#variavel_startM = False
#for valor in variavel:
#    if valor.lower().startswith('m'): # o Lower vai fazer com que se for maiuscula converta para minuscula e se for minuscula mantem
#        variavel_startM = True
#    
#if variavel_startM:
#    print('Existe uma variavel que começa com M')
#else:
 #   print('Nao exitse uma palavra que começa com M')

#variavel = ['Miguel', 'Dias' , 'Mendes']
#variavel_startM = False
#for valor in variavel:
#   print(valor)
#   if valor.lower().startswith('m'):
#       break
#else:
#    print('Nao exitse uma palavra que começa com M')

#Aqui ele vai pular os nomes que começam com M
variavel = ['Miguel', 'Dias' , 'Mendes']
variavel_startM = False
for valor in variavel:
   print(valor)
   if valor.lower().startswith('m'):
       continue
   print(valor)
else:
    print('Nao exitse uma palavra que começa com M')