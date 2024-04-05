#exercicio 36

'''Nesse programa o usuário deve entrar com um número e o sistema retornar se ele é divisível por 10 ou se é divisível por 5 ou se é divisível por 2, caso contrário retornar que o valor não é divisível por nenhum desses valores.'''

numero = float(input("Insira um número: "))

if numero % 10 == 0:
    print("O número informado é divisível por 10.")

elif numero % 5 == 0:
    print("O número informado é divisível por 5.")

elif numero % 2 ==0:
    print("O número informado é divisível por 2.")

else:
    print("O valor informado não é divisível por 10, 5 ou 2.")