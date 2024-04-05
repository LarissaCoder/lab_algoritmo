#exercicio 31
''' Desenvolva um programa em Python que receba via teclado um valor 
e a partir disso faça:
(1) se o valor for 1, 2 ou 3, mostre o valor elevado ao quadrado;
(2) se o valor for o número 4 ou 9, mostre a raiz quadrada do número; 
(3) se for os valores 6, 7 e 8, mostre o valor dividido 9.'''

valor = int(input("Digite um número: "))

if valor == 1 or valor == 2 or valor == 3:
    print(f"O número {valor} elevado ao quadrado é {valor**valor:.0f}.")
    
elif valor == 4 or valor == 9:
    print(f"A raiz do número {valor} é {(valor**(1/2)):.0f}.")

elif valor == 6 or valor == 7 or valor ==8:
    print(f"O número {valor} dividido por 9 é igual a {(valor/9):.2f}.")
  
else:
    print("O número que você digitou não é válido, escolha entre 1 e 9.")