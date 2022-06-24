#
# 	Em linguagem Python, crie um programa que recebe como entrada do usuário o valor de uma variável x e seja
# 	capaz de apresentar em tela o resultado da seguinte expressão matemática:
#  E = ((x^2-x+1)/((x-5)/2))
#
# entrada de dados
x = float(input("informe o valor de x: ")) # solicita o valor de x

# processamento
E = ((x**2-x+1)/((x-5)/2))

# saída de dados
print(f"O resultado da expressão é: {E}")

print("Fim do programa")
