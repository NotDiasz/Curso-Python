#formatando valores em python e strings


#positivos 
texto = 'Python s2'
print(texto[2])

#negativo 
texto = 'Python s2'
print(texto[-2])

fatiamento = texto[0:6]
print(fatiamento)

fatiamento = texto[1:5]
print(fatiamento)

fatiamento = texto[0:-1]
print(fatiamento)

fatiamento = texto[0::2]
print(fatiamento)

print(len(texto))

for letra in texto:
    print(letra)
