from random import randint

numero = str(randint(100000000 , 999999999))

novo_cpf = numero
total = 0
reverso = 10

for index in range(19):
    if index > 8: # aqui eu fiz o numero voltar e recomeçar printando do 0 quando chegar no 8 pela primeira vez
        index -= 9

    total += int(novo_cpf[index]) * reverso

    reverso -= 1
    if reverso < 2:
        reverso = 11
        d = 11 - (total % 11)

        if d > 9:
            d = 0
        total = 0
        novo_cpf += str(d)

print(novo_cpf)