while True:

    num1 = input('Digite um numero : ')
    num2 = input('Digite outro numero : ')
    op = input('Digite um operador : ')
    call = 0


    if not num1.isnumeric() or not num2.isnumeric():
        print('Voce precisa digitar um numero')
        continue

    if op == '+':
        num1 = int(num1)
        num2 = int(num2)
        call = num1 + num2
        print(call)
    elif op == '*':
        num1 = int(num1)
        num2 = int(num2)
        call = num1 * num2
        print(call)
    elif op == '-':
        num1 = int(num1)
        num2 = int(num2)
        call = num1 - num2
        print(call)
    elif  op == '/':
        num1 = float(num1)
        num2 = float(num2)
        call = num1/num2
        print ('{:.2f}'.format(call))
    else:
        print('Operador Invalido')

    sair = input('Deseja Sair [s] continuar [n] ')
     
    if sair == 's':
        break