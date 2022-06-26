# Autores: Carlos, 
#
# Implemente um programa em linguagem Python que recebe como entradas a base e a altura de um triângulo
# e apresente ao usuário a área deste triângulo. A área de um triângulo é calculada a partir da
# seguinte expressão: A_T=(b*h)/2, em que b é a base do triângulo e h a sua altura.


# entrada de dados
base = float(input("informe a base do triângulo: ")) # solicita a base do triângulo
altura = float(input("informe a altura do triângulo: ")) # solicita a altura do triângulo

# processamento
area = (base * altura) / 2

# saída de dados
print(f"A área do triângulo é: {area}")

print("Fim do programa")
