print("Olá. Bem-vindo a calculadora de vendas") 

seletor = 0
contador = 1
seletor = int(input("O que gostaria de fazer? 1 = Calculadora de vendas, 2 = sair"))

if seletor == 1:
 while True:
        preco_total = 0
 
        print("Digite as seguintes informações para o calculo:")

        preco_de_unidade = float(input(f"Qual o preço do produto {contador}:"))
        imposto = float(input(f"Imposto total do produto {contador}:"))
        frete = float(input(f"Frete do produto {contador}:"))
        desconto = float(input(f"Desconto do produto {contador}:")) 
        contador += 1
        def recibo():
            preco_total = preco_de_unidade + imposto + frete - desconto
            print (f"=== RECIBO ===") 
            print(f"Produto numero {contador} ")
            print(f"Preço total: R${preco_total}")
            print(f"Imposto: R${imposto}")
            print(f"Frete: R${frete}")
            print(f"Desconto R${desconto}")

            seletor2 = input("Gostaria de criar um recibo? sim (para criar) não (para não criar)")

            if seletor2 == "sim" or "Sim" or "s" or "S" or "yes" or "Yes" or "y" or "Y" or "1":
                recibo1 = open(f"Recibo{contador}.txt", "w")
                recibo1.write("=== RECIBO ==="
                              f"Produto numero {contador} "
                              f"Preço total: R${preco_total}"
                              f"Imposto: R${imposto}"  
                              f"Frete: R${frete}"
                              f"Desconto R${desconto}") 
                recibo1.close()
            
            elif seletor2 == "não" or "Não" or "n" or "N" or "no" or "No":
              input("\n === Aperte ENTER para continuar ===")

            else:
                print("Comando invalido") 
                input("\n === Aperte ENTER para continuar ===") 
            

        recibo()
        input("\n === Aperte ENTER para continuar ===")

elif seletor == 2:
    input("\n === Aperte ENTER para sair ===")

else:
    print("Comando invalido")
    seletor = int(input("O que gostaria de fazer? 1 = Calculadora de vendas, 2 = sair"))