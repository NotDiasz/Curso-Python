"""
Operador Ternário em Python
"""
#logged_user = False
#if logged_user == True:
#   msg = 'Usuario Logado'
#else:
#   msg = 'Usuario sem Login'
#print(msg)

""""""
#logged_user = True
#msg = 'Usuario Logado' if (logged_user == True) else 'Usuario precisa logar.' # Aqui eu criei a variavel e a condiçao ja que eu quero que ela #apareça # e podemos usar toda estrutura de parenteses se quiser colocar mais condiçoes 
#print(msg)

""""""

idade = input("Digite a idade : ")

if not idade.isnumeric(): # aqui usei is numeric para conferir se tem apenas numeros ai uso o not se nao tem apenas numero da o print caso contrario executa o bloco de comando else 
    print("Voce precisa digitar apenas numeros")
else:
    idade = int(idade) #Aqui transformei em inteiro
    e_de_maior = (idade >= 18) #aqui fiz a condiçao que olha se e de maior
    msg = 'Pode acessar' if (e_de_maior == True) else 'Nao pode acessar' #se em cima der false idade menor ou igual a 18 aqui em baixo usa o else
    print(msg)
