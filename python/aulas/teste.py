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