#Calcula qual valor é o maior entre 3

valor1 = float(input("Digite o primeiro número: "))
valor2 = float(input("Digite o segundo número: "))
valor3 = float(input("Digite o terceiro número: "))

if valor1 > valor2:
    maximo = valor1
else:
    maximo = valor2

if valor3 > maximo:
    maximo = valor3

print(f"O maior número entre os informados é {maximo:.0f}")