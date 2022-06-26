# Autores:
# michel silva
# Carlos Eduardo
#
# data: 26/06/2022
#
# Elabore um programa em linguagem Python que implementa o cálculo do valor de um polinômio do terceiro grau.
# Um polinômio do terceiro grau possui a seguinte equação geral:
#
# p(x)=ax^3+bx^2+cx+d
#

# entrada de dados
a = float(input("informe o valor de a: ")) # solicita o valor de a
b = float(input("informe o valor de b: ")) # solicita o valor de b
c = float(input("informe o valor de c: ")) # solicita o valor de c
d = float(input("informe o valor de d: ")) # solicita o valor de d
x = float(input("informe o valor de x: ")) # solicita o valor de x

# processamento
p = (a*x**3) + (b*x**2) + (c*x) + d

# saída de dados
print(f"O resultado da expressão é: {p}")

print("Fim do programa")
