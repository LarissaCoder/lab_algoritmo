#Larissa Regina da Silva RA 1051392411026

# Defino uma função para calcular o desconto com base no valor da compra
def funcao_desconto(valor_compra):
    
    # Se a compra for maior ou igual a R$ 300, dou 20% de desconto
    if valor_compra >= 300.00:
        desconto = (valor_compra * 20) / 100
        
    # Se estiver entre R$ 200 e R$ 299.99, o desconto é de 10%
    elif valor_compra >= 200.00 and valor_compra <= 299.99:
        desconto = (valor_compra * 10) / 100
        
    # Caso contrário, aplico 5% de desconto
    else:
        desconto = (valor_compra * 5) / 100
    return desconto

# Solicito o valor da compra
valor_compra = float(input("Digite o valor da sua compra: "))

# Chamo a função de desconto e passo o valor da compra como argumento
desconto = funcao_desconto(valor_compra)

# Calculo o valor final a pagar com o desconto
valor_final = valor_compra - desconto

# Exibo na tela o valor total da compra e o valor final com o desconto aplicado
print(f"O valor total da sua compra é de R${valor_compra:.2f}.")
print(f"O valor final a pagar é de R${valor_final:.2f}")