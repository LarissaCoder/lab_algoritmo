#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.

n1 = input("Digite algo aqui: ")
print(type(n1))

#Informar se é numerico
if (n1.isnumeric()):
    print("'{}' é um número!".format(n1))
else:
    print("O que você digitou não é um número.")

#Informar se é alfabético
if (n1.isalpha()):
    print("'{}' são caracteres alfabéticos!".format(n1))
else:
    print("Não são caracteres alfabéticos. ")