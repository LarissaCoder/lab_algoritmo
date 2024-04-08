'''#Larissa Regina da Silva RA 1051392411026 

# Solicitei os valores ao usuário
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Operações matemáticas
soma = numero1 + numero2
subtracao = numero1 - numero2
multiplicacao = numero1 * numero2
divisao = (numero1 / numero2)

# Exibir os resultados na tela
print("Resultados:")
print(f"Soma: {soma}")
print(f"Subtração: {subtracao}")
print(f"Multiplicação: {multiplicacao:.2f}")
print(f"Divisão: {divisao}")    '''

'''Faça um algoritmo com duas variáveis numéricas (tipo int) que realize as 4 operações básicas (soma, subtração, multiplicação e divisão), mostre os resultados na tela. Os mesmos devem ser solicitados ao usuário, digite os valores via teclado.'''

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

soma = n1 + n2
print(f"A soma entre {n1} e {n2} é {soma}.")

sub = n1 - n2
print(f"A subtração entre {n1} e {n2} é {sub}.")

mult = n1 * n2
print(f"A multiplicação entre {n1} e {n2} é {mult}.")

div = n1 / n2
print(f"A divisão entre {n1} e {n2} é {div:.2f}.")