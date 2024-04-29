#Larissa Regina da Silva RA 1051392411026

'''Desenvolva um programa em Python que receba via teclado um valor e a partir disso faça:
(1) se o valor for 1, 2 ou 3, mostre o valor elevado ao quadrado;
(2) se o valor for o número 4 ou 9, mostre a raiz quadrada do número;
(3) se for os valores 6, 7 e 8, mostre o valor dividido 9'''

#Primeiro o exercício foi resolvido sem função
'''valor = float(input("Digite um número: "))

if valor == 1 or valor == 2 or valor == 3:
    quadrado = valor**valor
    print(f"O número {valor:.0f} elevado ao quadrado é igual a {quadrado:.0f}.")

elif valor == 4 or valor == 9:
    raiz = valor**(1/2)
    print(f"A raiz quadrada do número {valor:.0f} é igual a {raiz:.0f}.")
    
elif valor == 6 or valor == 7 or valor == 8:
    dividido = valor/9
    print(f"O número {valor:.0f} dividido por 9 é igual a {dividido:.2f}.")

else:
    print (f"Favor inserir um número de 1 a 4 ou 6 a 9, o número {valor:.0f} digitado é inválido.")'''
    
#Resolvendo com função

import math
 
numero = float(input("Digite um número: "))
 
def func_quadrado(numero):
    if numero in [1,2,3]:
        return math.pow(numero, 2)
    else:
        return None
 
resultado_quadrado = func_quadrado(numero)
 
if resultado_quadrado is None:
    print("Número inválido")
else:
    print(f"O número {numero} elevado ao quadrado é igual a {resultado_quadrado}.")
 
def func_raiz(numero):
    if numero in [4,9]:
        return math.sqrt(numero)
    else:
        return None
 
resultado_raiz = func_raiz(numero)
 
if resultado_raiz is None:
    print("Número inválido")
else:
    print(f"A raiz do número {numero} é igual a {resultado_raiz}.")
 
def func_divisao(numero):
    if numero in [6,7,8]:
        return (numero/9)
    else:
        return None
 
resultado_divisao = func_divisao(numero)
 
if resultado_divisao is None:
    print("Número inválido")
else:
    print(f"O número {numero} dividido por 9 é igual a {resultado_divisao}.")