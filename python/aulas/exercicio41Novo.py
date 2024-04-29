#Larissa Reginda da Silva RA 1051392411026

import math

#Determinei a função para o calculo do numero ao quadrado
def funcao_quadrado (numero):
    return math.pow(numero,2)


#Determinei a função para calculo da raiz
def funcao_raiz (numero):
    return math.sqrt(numero)

#Determinei a função para dividir o valor por 9
def funcao_dividido (numero):
    return (numero/9)

#Criei o input para o usuário inserir o número
numero = int(input("Digite um número: "))

#Determinei as condições com base nos critérios,dependendo do número será retornado o resultado da função
if numero in [1,2,3]:
    resultado = funcao_quadrado(numero)
    print(f"O número {numero} elevado ao quadrado é igual a {resultado:.0f}.")

elif numero in [4,9]:
    resultado = funcao_raiz(numero)
    print(f"A raiz do número {numero} é igual a {resultado:.0f}.")

elif numero in [6,7,8]:
    resultado = funcao_dividido(numero)
    print(f"O número {numero} dividido por 9 é igual a {resultado:.2f}.")
    
else:
    print("O número digitado é inválido. Favor digitar um número entre 1-4 e 6-9.")