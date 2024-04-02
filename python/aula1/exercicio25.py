#Larissa Regina da Silva RA 1051392411026

metros_quadrados = input("Informe o tamanho em metros quadrados da área a ser pintada: ")

# Verifiquei se a entrada do usuário é um número válido
if metros_quadrados.replace('.', '', 1).isdigit():
    metros_quadrados = float(metros_quadrados)
    
    # Calculei a quantidade de tinta necessária com 10% de folga
    tinta_necessaria = (metros_quadrados / 6) * 1.1
    
    # Opção a) Comprar apenas latas de 18 litros
    latas_a = (tinta_necessaria / 18)
    if tinta_necessaria % 18 != 0:
        latas_a += 1
    preco_a = latas_a * 80
    
    # Opção b) Comprar apenas galões de 3,6 litros
    galoes_b = (tinta_necessaria / 3.6)
    if tinta_necessaria % 3.6 != 0:
        galoes_b += 1
    preco_b = galoes_b * 35
    
    # Opção c) Misturar latas e galões para obter o menor preço
    latas_c = tinta_necessaria // 18
    galoes_c = ((tinta_necessaria % 18) / 3.6)
    if (tinta_necessaria % 18) % 3.6 != 0:
        galoes_c += 1
    preco_c = latas_c * 80 + galoes_c * 35
    
    print("\nQuantidade de tinta e preço para:")
    print("a) Comprar apenas latas de 18 litros:", int(latas_a), "latas, R$", round (preco_a, 0))
    print("b) Comprar apenas galões de 3,6 litros:", int(galoes_b), "galões, R$", round (preco_b, 0))
    print("c) Misturar latas e galões:", int(latas_c), "latas e", int(galoes_c), "galões, R$", round (preco_c, 0))
else:
    print("Por favor, insira um número válido para o tamanho da área.")