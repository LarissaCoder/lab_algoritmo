'''Faça um algoritmo que leia o salário de um funcionário 
e mostre seu novo salário, com 15% de aumento.'''

salario = float(input("Qual o seu salário anterior? R$"))

novo = salario+(salario*15/100)

print("O seu novo salario com aumento de 15% será de R${:.2f}.".format(novo))