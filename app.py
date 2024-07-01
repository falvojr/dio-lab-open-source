
print("City of Bank Lights")

menu = """
[D] Depositar
[S] Sacar
[E] Extrato
[Q] Sair
"""
print(menu.upper())

saldo = 0
limite_saque_diario = 3
limite_saque_total = 500
num_saques = 0
extrato = ""

while True:
    opcao = input("Digite a operação desejada (D, S, E, Q): ").upper()

    if opcao == "D":
        valor_deposito = float(input("Digite o valor para realizar o depósito: "))
        if valor_deposito > 0:
            saldo += valor_deposito
            extrato += f"Depósito de R${valor_deposito:.2f}\n"
            print(f"Depósito de R${valor_deposito:.2f} realizado com sucesso. Seu saldo atual é R$ {saldo:.2f}")
        else:
            print("Valor de depósito inválido. O valor deve ser maior que zero.")

    elif opcao == "S":
        if num_saques < limite_saque_diario and saldo > 0:
            valor_saque = float(input("Digite o valor para realizar o saque: "))
            if valor_saque > 0 and valor_saque <= saldo and (num_saques + 1) <= limite_saque_total:
                saldo -= valor_saque
                num_saques += 1
                extrato += f"Saque de R${valor_saque:.2f}\n"
                print(f"Saque de R${valor_saque:.2f} realizado com sucesso. Seu saldo atual é R$ {saldo:.2f}")
            elif valor_saque <= 0:
                print("Valor de saque inválido. O valor deve ser maior que zero.")
            elif valor_saque > saldo:
                print("Saldo insuficiente.")
            elif (num_saques + 1) > limite_saque_total:
                print("Limite total de saques atingido.")
        else:
            print("Limite diário de saques atingido ou saldo insuficiente.")

    elif opcao == "E":
        print("Seu extrato:")
        print(extrato)

    elif opcao == "Q":
        print("Saindo do programa.")
        break

    else:
        print("Opção inválida, selecione novamente.")

