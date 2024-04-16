'''
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M ou F, caso esteja errado, peça a digitação novamente até ter um valor correto'''

digiteSexo = input("Digite o seu sexo (M/F): ".upper())

while digiteSexo not in "MmFf":
    digiteSexo = input("Inválido. Digite novamente: ")
    
print(f"O seu sexo é {digiteSexo}.")

