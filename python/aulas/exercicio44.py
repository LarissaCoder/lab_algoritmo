#Larissa Regina da Silva RA 1051392411026

import math

# Define a função para calcular o cubo de um número
def funcao_cubo(numero):
    return math.pow(numero, 3)

# Define a função para calcular o fatorial de um número
def funcao_fatorial(numero):
    return math.factorial(numero)

# Define a função para dividir um número por 9
def funcao_dividido9(numero):
    return (numero / 9)

# Solicita ao usuário que digite um número
numero = int(input("Digite um número: "))

# Verifica se o número é 1 ou 2
if numero in [1, 2]:
    resultado_cubo = funcao_cubo(numero)  # Calcula o cubo do número
    print(f"O número {numero} elevado ao cubo é igual a {resultado_cubo:.0f}.")

# Verifica se o número é múltiplo de 3
elif numero % 3 == 0:
    resultado_fatorial = funcao_fatorial(numero)  # Calcula o fatorial do número
    print(f"O fatorial do número {numero} é igual a {resultado_fatorial}.")

# Verifica se o número é 4, 5, 7 ou 8
elif numero in [4, 5, 7, 8]:
    resultado_dividido9 = funcao_dividido9(numero)  # Divide o número por 9
    print(f"O número {numero} dividido por 9 é igual a {resultado_dividido9:.2f}.")

# Se o número não se encaixa em nenhuma das condições anteriores
else:
    print("O número digitado é inválido.")  # Informa que o número é inválido
