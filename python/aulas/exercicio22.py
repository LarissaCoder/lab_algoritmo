'''#Larissa Regina da Silva RA 1051392411026 

# Declarei as variáveis
compra1 = float(input("Digite o valor da primeira compra: "))
compra2 = float(input("Digite o valor da segunda compra: "))
compra3 = float(input("Digite o valor da terceira compra: "))

# Calculei o desconto com base no valor da compra
def calcular_desconto(valor_compra):
    if valor_compra >= 300:
        return valor_compra * 0.2
    elif valor_compra >= 200:
        return valor_compra * 0.15
    elif valor_compra >= 100:
        return valor_compra * 0.1
    else:
        return 0

# Calculei desconto para cada compra
desconto_compra1 = calcular_desconto(compra1)
desconto_compra2 = calcular_desconto(compra2)
desconto_compra3 = calcular_desconto(compra3)

# Calculando o valor total de cada compra após o desconto
total_compra1 = compra1 - desconto_compra1
total_compra2 = compra2 - desconto_compra2
total_compra3 = compra3 - desconto_compra3

# Retornei os descontos e o valor total
print(f"A sua compra de R${compra1:.2f} terá um desconto de R${desconto_compra1:.2f} e o valor total de R${total_compra1:.2f}")

print(f"A sua compra de R${compra2:.2f} terá um desconto de R${desconto_compra2:.2f} e o valor total de R${total_compra2:.2f}")

print(f"A sua compra de R${compra3:.2f} terá um desconto de R${desconto_compra3:.2f} e o valor total de R${total_compra3:.2f}") 
'''

'''Faça um algoritmo que mostre os descontos concedidos pela loja ABC
em suas mercadorias. Em compras acima de 300,00 forneça 20% de desconto,
para 200,00 desconto de 15% e acima de 100,00 o desconto será de 10%. 
Atribua valores as variáveis compra1, compra2 e compra3. Mostre na tela 
o valor total e o valor com o devido desconto. Os mesmos devem ser solicitados 
ao usuário, digite os valores via teclado.'''

valor = float(input("Digite o valor da sua compra: R$"))

if valor >= 300.00:
    desconto1 = (valor*20)/100
    total1 = valor - desconto1
    print(f"A sua compra de R${valor} terá um desconto de 20%, sendo de R${desconto1:.2f}!")
    print(f"O seu total é de R${total1:.2f}")

elif valor >= 200.00:
    desconto2 = (valor*15)/100
    total2 = valor - desconto2
    print(f"A sua compra de R${valor} terá um desconto de 15%, sendo de R${desconto2}!")
    print(f"O seu total é de R${total2:.2f}")
    
elif valor >= 100.00:
    desconto3 = (valor*10)/100
    total3 = valor - desconto3
    print(f"A sua compra de R${valor} terá um desconto de 10%, sendo de R${desconto3}!")
    print(f"O seu total é de R${total3:.2f}")
    
else:
    print("A sua compra não atingiu o valor para desconto.")