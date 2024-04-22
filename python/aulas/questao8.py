#Larissa Regina da Silva RA 1051392411026

#Recebo do usuário o peso do prato em quilos
pesoPrato = float(input("Digite o peso do seu prato (kg): "))

#Converto esse peso de quilos para gramas (para que eu possa calcular na frente o valor a pagar) e subtraio a tara do prato
pesoConvertido = (pesoPrato*1000) - 200

#O valor que deve ser pago é equivalente a multiplicar o preço por quilo, pelo peso já convertido para gramas e dividir por 1000 (que corresponde a 1kg)
valorPagar = (63.00*pesoConvertido) / 1000

#Com isso tenho o valor calculado a partir das gramas, já tendo descontado a tara
print(f"O valor do seu prato é R${valorPagar:.2f}.")