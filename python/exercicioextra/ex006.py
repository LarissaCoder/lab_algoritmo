#Operadores aritméticos

''' Ordem de precedência
1   () parênteses
2   ** potência
3   * multiplicação / divisão // divisão inteira % resto da divisão
4   + adição - subtração
'''


#Retorno de apresentação
nome = input("Qual o seu nome? ")
print("Prazer em te conhecer {}!".format(nome))


#Soma com .format
n1 = int(input("insira um valor: "))
n2 = int(input("insira outro valor: "))

print("A soma entre os dois valores é de {}!".format(n1+n2))