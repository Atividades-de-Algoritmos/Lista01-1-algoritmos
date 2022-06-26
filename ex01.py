#
# Autores:
# Michel Silva
# Emanuel Franklyn
# Carlos Eduardo
#
# data: 26/06/2022
#
# 1. De uma forma geral, pode-se afirmar que os Algoritmos   
# são compostos por um conjunto de entradas de dados e uma   
# etapa de processamento para a obtenção de sua(s) saída(s). 
# Muitas vezes, as saídas de um algoritmo são apresentadas em
# tela. Sabendo disso, desenvolva um programa em linguagem   
# Python que solicite do usuário o seu nome e apresente em   
# tela um cabeçalho padrão, seguido pelo nome informado,     
# exatamente como ilustrado a seguir.                        

# Entrada de dados

nome = input("informe o seu nome: ") # solicita o nome do usuário

# Processamento e saída de dados

print('**************************************')
print('* ALGORITMOS E LÓGICA DE PROGRAMAÇÃO *')
print('* Turma: 1° INTIN   Ano letivo: 2022 *')  # Série de prints imprimindo o cabeçalho
print('* Professores: Leandro e Michel      *')
print('* Monitores: Emanuel e Carlos        *')
print('**************************************')
print(f"Aluno: {nome}") # imprime o nome do usuário

print("Fim do programa") # Informamos ao usuário que o programa terminou
