menu = """

[d] Depositar
[s] Sacar 
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES =3

while True:

    opcao = input (menu)

    if opcao == "d":    
        valor = float(input("Informe o valor do depósito: "))
        
        if valor >0:
            saldo += valor
            extrato += f"Depósito:  R$ {valor:.2F}\n"

        else:
            print("Operação Falhou! O valor Informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor que deseja Sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_de_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Operação Falhou! Voçe não tem saldo suficiente.")

        elif excedeu_limite:
            print("Operação Falhou! O valor de saque excedeu o limite.")

        elif excedeu_saques:
            print("Operação Falhou! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato == f'Saque: R$ {valor:.2f}\n'
            numero_de_saques += 1

        else:
            print("Operação falhou o valor Informado é inválido.")


    
    elif opcao == "e":
        print("\n========== EXTRATO ==========")
        print("Não foram realizadas as movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print('================================')
        
    elif opcao == "q":
        break   

    else: 
        print("Operação Inválida, por favor selecione novamente a operação desejada")
