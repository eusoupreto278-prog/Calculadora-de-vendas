print("Olá. Bem-vindo a calculadora de vendas") 

seletor = 0
contador = 1
seletor = int(input("O que gostaria de fazer? 1 = Calculadora de vendas, 2 = sair"))

if seletor == 1:
 while True:
        preco_total = 0
 
        print("Digite as seguintes informações para o calculo:")

        preco_de_unidade = int(input(f"Qual o preço do produto {contador}:"))
        imposto = int(input(f"Imposto total do produto {contador}:"))
        frete = int(input(f"Frete do produto {contador}:"))
        desconto = int(input(f"Desconto do produto {contador}:")) 
        contador += 1
        def recibo():
            preco_total = preco_de_unidade + imposto + frete - desconto
            print (f"=== RECIBO ===") 
            print(f"Produto numero {contador} ")
            print(f"Preço total: R${preco_total}")
            print(f"Imposto: R${imposto}")
            print(f"Frete: R${frete}")
            print(f"Desconto R${desconto}")

        recibo()

        input("\n ===Aperte ENTER para continuar===")

elif seletor == 2:
    input("\n ===Aperte ENTER para sair===")

else:
    print("Comando invalido")
    seletor = int(input("O que gostaria de fazer? 1 = Calculadora de vendas, 2 = sair"))