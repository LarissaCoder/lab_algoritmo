#Exercícios extras do curso em vídeo

#Imprimir mensagem
print('Olá mundo')

#O resultado é um número, porque está sem aspas.
print(7+4)

#A junção da mensagem, não são interpretados como número.
print('7'+'4')

#Variáveis
NOME = 'Joana'
IDADE = 25
PESO = 68.5

print(NOME, IDADE, PESO)

#Receber input

sobrenome = input('Qual o seu sobrenome?')
print("Seu sobrenome é",sobrenome)

'''Desafio 1
    Crie um script que leia o nome de uma pessoae mostre uma mensagem de boas vindas de acordo com o valor digitado.
'''

nome1 = input('Qual é o seu nome?')
print('Seja bem-vinda', nome1, 'prazer em te conhecer')

'''Desafio 2
    Crie um script python que leia o dia, mês e ano da nascimento de uma pessoa e mostre uma mensagem com data formatada.
'''

dia = input('Qual o dia do seu nascimento? ')
mes = input('Qual o mês do seu nascimento? ')
ano = input('Qual o ano do seu nascimento? ')

print('Você nasceu no dia',dia,'do mês de',mes,'e ano de', ano )

'''Desafio 3
    Crie um script python que leia dois números e tente mostrar a soma entre eles
'''

numero1 = int(input('Insira o primeiro número: '))
numero2 = int(input('Insira o segundo número: '))

soma = numero1 + numero2

print('A soma entre os dois número é de',soma)