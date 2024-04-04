#Faça um algoritmo que leia o preço de um produto e mostre o seu novo preço com 5% de desconto.

prod = float(input("Preço do produto para aplicar o desconto: R$"))

desc = (prod*5)/100

vlr = prod-desc

print("O desconto aplicado ao produto de R${:.2f} é de R${:.2f}. \nO seu total é de R${:.2f}.".format(prod, desc,vlr))