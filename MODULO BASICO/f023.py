num1 = input('Digite um numero : ')
num2 = input('Digite outro numero : ')

#isnumeric isdigit isdecimal

print(num1 + num2)

if num1.isdigit () and num2.isdigit ():
    num1 = int(num1)
    num2 = int(num2)

    print(num1 + num2)
else :
    print('Nao pode ser convertido para soma')

#try: tenta executar um bloco de codigo 
#except: se der erro no try executa esse bloco de codigo
