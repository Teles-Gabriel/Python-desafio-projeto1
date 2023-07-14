import math

menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>"""
saldo = 50
limite = 500
extrato = ""
numero_saques = 0
limite_saque = 3
extrato_saques = []

while True:
    
    opcao = input(menu)

    if opcao == "d":
        print("Deposito")
        valor = float(input("Insira o valor que você quer depositar:"))
        deposito = math.sqrt((valor)**2)
        saldo += deposito
        print(f"Seu novo saldo é de R$ {saldo:,.2f}")

    elif opcao == "s":
        if numero_saques <= limite_saque:
            print("Saque")
            saque = float(input("Insira o valor que você quer sacar:"))
            if saldo >= saque and saque >= saldo and saque <= 500:
                saldo -= saque
                print(f"Seu saldo é de R$ {saldo:,.2f}")
                print("Espere que o valor esteja disponivel na boca do caixa.")
                numero_saques += 1
                extrato_saques.append(saque)

            else:
                print("Valor insuficiente ou ultrapassa o limite de 500 reais por saque.")
        else:
            print("O número máximo de saques por dia foi atingido, tente novamente amanhã ou dirija-se a uma agência.")

    elif opcao == "e":
        print("Extrato")
        print(f"Seu saldo é de R$ {saldo:,.2f}.")
        if len(extrato_saques) > 0:
            print(f"Saques realizados: {extrato_saques:,.2f}")
        elif len(extrato_saques) == 0:
            print("Não foram realizadas movimentações")
          
    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")