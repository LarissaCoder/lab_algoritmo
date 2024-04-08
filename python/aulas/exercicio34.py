#Larissa Regina da Silva RA 1051392411026

'''Elabore  um programa em PYTHON, que mostre  os descontos  concedidos  pela  loja  ABC  em suas mercadorias. Em  compras  acima  de  R$  300,00  forneça  20%  de  desconto,  entre  R$  200,00  a  R$  299,99 desconto de 10% e abaixo de R$ 199,99 o desconto será de 5%. Mostre na tela o valor total e o valor final a pagar (com o desconto).Solicite ao usuário que digite os valores via teclado.'''

#Entrada do valor
valor = float(input("Digite o valor da compra: "))

#Aplicado desconto de 20%
if valor >= 300.00:
    print(f"O seu desconto de 20% é de R${(valor*20)/100:.2f}")
    print(f"O total da sua compra é de R${valor-((valor*20)/100):.2f}")

#Aplicado desconto de 10%
elif valor >=200.00 and valor <= 299.99:
    print(f"O seu desconto de 10% é de R${((valor*10)/100):.2f}")
    print(f"O total da sua compra é de R${valor-((valor*10)/100):.2f}")

#Aplicado desconto de 5%
else:
    print(f"O seu desconto de 5% é de R${((valor*5)/100):.2f}")
    print(f"O valor total da sua compra é de R${valor-((valor*5)/100):.2f}")