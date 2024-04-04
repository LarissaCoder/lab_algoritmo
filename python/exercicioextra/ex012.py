# Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar (considere US1,00=R$3,27).


cash = float(input("Quanto dinheiro você tem? R$"))

dolar = cash/3.27

print("Com R${} reais, você pode comprar U${:.2f} dólares.".format(cash, dolar))