#Larissa Regina da Silva RA 1051392411026 

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