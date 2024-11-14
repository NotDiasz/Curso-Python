"""
Operadores Relacionais
== > >= < <= !=

Valores do Tipo Logico sao falso ou verdadeiro ou seja booleano
"""

variavel =  'Eu'
print(variavel)

nome = input('Qual e seu nome ? ')
idade = int(input('Qual sua idade ? '))

idadep = 20
idadeb = 30

if idade >= idadep and idade <= idadeb:
    print(f'{nome}' ' voce pode pegar seu emprestimo')
else:
    print(f'{nome}' ' voce e de menor ainda nao pode')