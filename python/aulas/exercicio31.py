''' Desenvolva um programa em Python que receba via teclado um valor 
e a partir disso faça:
(1) se o valor for 1, 2 ou 3, mostre o valor elevado ao quadrado;
(2) se o valor for o número 4 ou 9, mostre a raiz quadrada do número; 
(3) se for os valores 6, 7 e 8, mostre o valor dividido 9.'''

n = int(input("Digite um número: "))

if int(1-3):
    print("O valor elevado ao quadrado é: ", n**2)

if int(4,9):
    print("A raiz quadrada do número é: ", n**(1/2))

if int(6-8):
    print("O valor dividido por 9 é: ", n/9)

else:
    print("Opção de número inválida, insira um número de 1 a 9.")