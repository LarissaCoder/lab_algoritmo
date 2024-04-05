#exercicio 35

'''Desenvolva um programa em Python que receba via teclado um valor e a partir disso faça:
(1)se for um valor negativo, mostre o módulo(valor sem sinal) do valor;
(2)se for um valor maior do que 10,solicite outro valor e mostre a diferença entre eles;
(3)Caso o valor não seja de nenhuma condição anterior, mostre o valor dividido por 5'''

valor = float(input("Digite um número: "))

if valor < 0:
    print(f"O módulo de {valor} é {valor*(-1)}.")

elif valor >= 10:
    valor2 = float(input("Insira um segundo número: "))
    dif = valor - valor2
    print(f"A diferença entre {valor} e {valor2} é de {dif}")

else:
    print(f"O número {valor} dividido por 5 é {valor/5}")