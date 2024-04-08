#Larissa Regina da Silva RA 1051392411026

'''Nesse programa o usuário deve entrar com um número e o sistema retornar se ele é divisível por 10 ou se é divisível por 5 ou se é divisível por 2, caso contrário retornar que o valor não é divisível por nenhum desses valores.'''

#Entrada do valor
numero = float(input("Insira um número: "))

#Primeira condição, divisivel por 10
if numero % 10 == 0:
    print("O número informado é divisível por 10.")
    
#Segunda condição, divisivel por 5
elif numero % 5 == 0:
    print("O número informado é divisível por 5.")

#Terceira condição, divisivel por 2
elif numero % 2 ==0:
    print("O número informado é divisível por 2.")

#Aos demais, valor inválido
else:
    print("O valor informado não é divisível por 10, 5 ou 2.")