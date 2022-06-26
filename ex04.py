#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 26/06/2022
#
# 4. Elabore um programa em linguagem Python que implementa o
# cálculo do valor de um polinômio do terceiro grau.         
# Um polinômio do terceiro grau possui a seguinte equação    
# geral: p(x)=ax^3+bx^2+cx+d                                 


# Entrada de dados
a = float(input("informe o valor de a: ")) # solicita o valor de a
b = float(input("informe o valor de b: ")) # solicita o valor de b
c = float(input("informe o valor de c: ")) # solicita o valor de c
d = float(input("informe o valor de d: ")) # solicita o valor de d
x = float(input("informe o valor de x: ")) # solicita o valor de x

# Processamento de dados
p = (a*x**3) + (b*x**2) + (c*x) + d # Calcula o resultado do polinômio

# Saída de dados
print(f"\nO resultado da expressão é: {p}") # Imprimindo o resultado do polinômio

print("fim do programa") # Informando ao usuário que o programa terminou
