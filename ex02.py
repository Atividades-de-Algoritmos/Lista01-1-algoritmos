#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 27/06/2022
#
# 2. Implemente um programa em linguagem Python que recebe   
# como entradas a base e a altura de um triângulo e apresente
# ao usuário a área deste triângulo. A área de um triângulo é
# calculada a partir da seguinte expressão: A_T=(b*h)/2, em  
# que b é a base do triângulo e h a sua altura.              


# Entrada de dados

base = float(input("informe a base do triângulo: ")) # Solicita a base do triângulo
altura = float(input("informe a altura do triângulo: ")) # Solicita a altura do triângulo

# Processamento de dados

area = (base * altura) / 2 # Calculando a área do Δ com a fórmula a = (b * altura) / 2

# Saída de dados

print(f"A área do triângulo é: {area}") # Imprimindo o valor da área do triângulo

print("fim do programa") # Informamos ao usuário que o programa terminou
