#Calcular a média geral do aluno e retornar se foi aprovado ou não, exercício passado em aula.

p1 = float(input("Digite a primeira nota: "))
p2 = float(input("Digite a segunda nota: "))
p3 = float(input("Digite a terceira nota: "))

mg = (p1 + p2 + p3)/3
print("A sua média geral é de", mg)

#Usando condicional
if mg >= 7:
    print("Parabéns, você foi aprovado!")

else:
    print("Você não foi aprovado, continue se dedicando em seus estudos!")
