#exercicio 37

'''Elabore um programa em Python que o usuário entre com seu salário. Se o salário for menor  ou  igual  a  R$1500,00  coloque  um  acréscimo  de  20%  de  aumento.  Se  for  maior  que R$1500,00 e menor que R$2500,00 o acréscimo será de 10%, senão o acréscimo será de 5% para os demais valores.'''

salario = float(input("Insira o valor do seu salário: R$"))

if salario <= 1500:
    vinte = (salario*20)/100
    aumento1 = salario + vinte
    print(f"Seu novo salário com 20% de aumento é de R${aumento1:.2f}")

elif salario > 1500 and salario <2500:
    dez = (salario*10)/100
    aumento2 = salario + dez
    print(f"Seu novo salário com 10% de aumento é de R${aumento2:.2f}")

else:
    cinco = (salario*5)/100
    aumento3 = salario + cinco
    print(f"Seu novo salário com aumento de 5% é de R${aumento3:.2f}")