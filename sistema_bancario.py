menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

"""

Saldo = 0
Valor_Limite_Saque = 500
Extrato = ""
Numero_saques = 0
Numero_depositos = 0
Limite_saques = 3
Opcao = 0

while True:

    Opcao = int(input(menu))
    
    if Opcao == 1:
        Deposito = float(input("Digite o valor desejado para deposito:"))

        if Deposito > 0:
            Saldo += Deposito
            Numero_depositos += 1
        else:
            print("Valor informado não é válido, por favor, tente novamente!")

    elif Opcao == 2:

        Saque = float(input("Digite o valor desejado para saque:"))

        if Numero_saques == Limite_saques:
            print("Operação falhou! Número máximo de saques excedido.")
       
        elif (Saque < Saldo) and (Saque < Valor_Limite_Saque) and (Numero_saques < Limite_saques):
            Saldo -= Saque
            Numero_saques += 1
        
        elif Saque > Saldo:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif Saque > Valor_Limite_Saque:
            print("Operação falhou! O valor do saque excede o limite.")
        

    elif Opcao == 3:
        print("Seu extrato está assim:")
        print(f"Seu saldo é de: R${Saldo:.2f}")

        if Numero_saques >= 1 and Numero_depositos >= 1 :
            print(f"Foram Realizados {Numero_saques} saques e {Numero_depositos} depositos hoje!")

        else:
            print("Não foram realizados movimentações hoje!")
        

    elif Opcao == 4:
        print("Até mais!")
        break

    else:
        print("Opção invalida, por favor selecione novamente a operação desejada.")