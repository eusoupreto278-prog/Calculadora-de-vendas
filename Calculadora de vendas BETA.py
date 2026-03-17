print("Olá. Bem-vindo a calculadora de vendas")
print("Digite as seguintes informações para o calculo:") #Trocar a cor do texto

contador = 1
numero_produtos = 0 #Desativado. concertar para funcionar 
preco_total = 0

preco_de_unidade = int(input(f"Qual o preco do produto {contador}:"))
imposto = int(input(f"Imposto total do produto {contador}:"))
frete = int(input(f"Frete do produto {contador}:"))
desconto = int(input(f"Desconto do produto {contador}:")) #Funciona com subtração. Trocar para porcentagem
contador += 1
    

preco_total = preco_de_unidade + imposto + frete - desconto
print (f"O preço total é: R${preco_total}") # Obs: o resto funciona certo 