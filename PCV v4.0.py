import random

print("Olá. Bem-vindo a calculadora de vendas") #apresentacao

#seletor e contador
contador = 1
seletor = 0
seletor = int(input("O que gostaria de fazer? 1 = Calculadora de vendas, 2 = sair: "))

#if
if seletor == 1:
 while True: #Loop
        preco_total = 0
        aleatorio = random.randint(1, 99999)
 
        #informacoes para o calculo
        print("Digite as seguintes informações para o calculo:")

        preco_de_unidade = float(input(f"Qual o preço do produto {contador}: R$ "))
        imposto = float(input(f"Imposto total do produto {contador}:R$ "))
        frete = float(input(f"Frete do produto {contador}: R$ "))
        desconto = float(input(f"Desconto do produto {contador}: R$ ")) 
        cpf = str(input("Cpf (Se não (não)): "))
        
        preco_total = preco_de_unidade + imposto + frete - desconto
        print (f"=== RECIBO{contador} ===   ") 
        print(f"Produto numero {contador}   ")
        print(f"Preço total: R${preco_total}    ")
        print(f"Imposto: R${imposto}    ")
        print(f"Frete: R${frete}    ")
        print(f"Desconto R${desconto}   ")

            #criar arquvo do recibo
        seletor2 = input("Gostaria de criar um recibo? sim (para criar) não (para não criar)")

        if seletor2 == "sim" or "Sim" or "s" or "S" or "yes" or "Yes" or "y" or "Y" or "1":
            recibo1 = open(f"Recibo{contador} {aleatorio} Cpf {cpf}.txt", "w")
            recibo1.write(f"=== RECIBO{contador} ===     "
                            f"|Produto numero {contador}|     "
                            f"|Preço total: R${preco_total}|     "
                            f"|Imposto: R${imposto}|     "  
                            f"|Frete: R${frete}|     "
                            f"|Desconto R${desconto}|     "
                            f"|Cpf: {cpf}|     ")
            
            print(f"Recibo numero {contador} criado. Id: {aleatorio}") 
            
            recibo1.close()
            contador += 1
            
        elif seletor2 == "não" or "Não" or "n" or "N" or "no" or "No" or "2":
            input("\n === Aperte ENTER para continuar ===")

        else:
            print("Comando invalido") 
            input("\n === Aperte ENTER para continuar ===") 
            
        input("\n === Aperte ENTER para continuar ===")

else:
    exit
