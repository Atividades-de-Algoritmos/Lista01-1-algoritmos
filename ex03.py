#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 27/06/2022
#
# 3. Em linguagem Python, crie um programa que recebe como   
# entrada do usuário o valor de uma variável x e seja capaz  
# de apresentar em tela o resultado da seguinte expressão    
# matemática: E = ((x^2-x+1)/((x-5)/2))                      


# Entrada de dados

x = float(input("informe o valor de x: ")) # Solicita o valor de x

# Processamento de dados

E = ((x**2-x+1)/((x-5)/2)) # Calcula a expressão matemática

# Saída de dados

print(f"O resultado da expressão é: {E}") # Imprimindo o resultado da expressão

print("fim do programa") # Informamos ao usuário que o programa terminou
