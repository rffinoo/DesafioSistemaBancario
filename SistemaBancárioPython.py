menu = """

[1] Depositar
[2] Sacar 
[3] Extrato
[0] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_de_saques = 0
LIMITE_SAQUES = 5

while True:

    opcao = input (menu)

    if opcao == "1":    
        valor = float(input("Informe o valor do depósito: "))
        
        if valor >0:
            saldo += valor
            extrato += f"Depósito:  R$ {valor:.2F}\n"

        else:
            print("Erro! Por favor entre com uma das opções validas!.")

    elif opcao == "2":
        valor = float(input("Informe o valor que deseja Sacar: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_de_saques >= LIMITE_SAQUES

        if excedeu_saldo:
            print("Erro! Voçe não tem saldo suficiente.")

        elif excedeu_limite:
            print("Erro! O valor de saque excedeu o limite.")

        elif excedeu_saques:
            print("Erro! Número máximo de saques excedido.")

        elif valor > 0:
            saldo -= valor
            extrato == f'Saque: R$ {valor:.2f}\n'
            numero_de_saques += 1

        else:
            print("Operação falhou o valor Informado é inválido.")


    
    elif opcao == "3":
        print("\n========== EXTRATO ===========")
        print("Não foram realizadas as movimentações." if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print('============================')
        
    elif opcao == "0":
        break   

    else: 
        print("Erro! Por favor entre com uma das opções validas!.")
