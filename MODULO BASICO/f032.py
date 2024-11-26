"""
For in em Python

"""

#texto = 'Python'

#for n, letra in enumerate(texto):
    #print(letra , n)


#pular o numero de 2 em 2 começa de 0 a 10 e pula de 2 em 2
    #for numero in range(0,10,1):
    #print(numero)

#Aqui ele decrementa
    #for n in range(20 , 0 , -2):
    #print(n)

    #break quebra laço
    #continue pula para proxima interaçao

texto = 'Python'
new_str = ''

for letra in texto:
    if letra == 't':
        continue
    elif letra == 'h':
        new_str += 'H'
    else:
        new_str += letra
    
    print(letra)