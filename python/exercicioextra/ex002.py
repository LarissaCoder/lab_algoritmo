# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as inf possíveis.

a = input("Digite algo: ")

print("O tipo primitivo desse valor é ", type(a))
print("Alfabético? ", a.isalpha())
print("Numérico? ", a.isnumeric())
print("Alfanumérico? ", a.isalnum())
print("Minuscula? ", a.islower())
print("Maiuscula? ", a.isupper())
