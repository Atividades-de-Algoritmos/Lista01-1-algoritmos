# Autores:
# michel silva
# Carlos Eduardo
#
# data: 26/06/2022
#
# 5.Desenvolva um programa em linguagem Python que recebe do usuário o preço de um produto e um valor de desconto.
# Com estas informações, o programa deve exibir o preço do produto com desconto. Observações: O valor do desconto
# deve ser informado entre 1 (100%) e 0 (0%). Assim, 0.5 corresponde a um desconto de 50%. Neste momento,
# considere que sempre serão informados valores válidos pelo usuário.
# caso precise formatar o valor de um número numérico,
# sugerimos que assistam a este vídeo: link para vídeo do Youtube.  https://youtu.be/7QuriwzICaY
#

# entrada de dados
preco = float(input("informe o preço do produto: ")) # solicita o preço do produto
desconto = float(input("informe o valor do desconto: ")) # solicita o valor do desconto

# processamento
preco_desconto = preco - (preco * (desconto)) # calcula o valor do produto com desconto

# saída de dados
print(f"O preço do produto com desconto é: R$ {preco_desconto:,.2f}") # exibe o valor do produto com desconto

print("Fim do programa")
