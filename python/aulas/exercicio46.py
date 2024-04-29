#Larissa Regina da Silva RA 1051392411026

import math

def funcao_condicao():
    # Solicita ao usuário que digite um número
    numero = float(input("Digite um número: "))

    if numero < 0:
        # Calcula o módulo do número
        modulo = abs(numero)
        print(f"O número {numero} sem sinal é {modulo}.")

    elif numero >= 10:
        # Solicita ao usuário que digite um novo número
        novo_numero = float(input("Digite um novo número: "))
        # Calcula a diferença entre os números
        diferenca = numero - novo_numero
        print(f"A diferença entre {numero} e {novo_numero} é de {diferenca}.")

    else:
        # Divide o número por 5
        dividido = numero / 5
        print(f"O número {numero} dividido por 5 é igual a {dividido}.")

funcao_condicao()