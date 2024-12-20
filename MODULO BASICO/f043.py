"""
Validador de Cpf
"""
while True:
    #cpf = '16899535009'

    cpf = input('Digite um Cpf : ')

    if not cpf.isnumeric():
        print('Voce digitou uma letra')
        continue

    novo_cpf = cpf[:-2] #eliminei os 2 ultimos numeros do cpf
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
    
    if cpf == novo_cpf:
        print("Cpf Valido")
    else:
        print('Cpf Invalido')
