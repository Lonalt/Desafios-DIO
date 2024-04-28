"""DESAFIO Sistema de Caixa Eletrônico"""

from os import system
from time import sleep

MENU = """

[1] Depositar
[2] Sacar
[3] Extrato
[0] Sair

=> """

SALDO = 0
LIMITE = 500
EXTRATO = ""
NUMERO_SAQUES = 0
LIMITE_SAQUES = 3

while True:

    opcao = input(MENU)

    if opcao == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            SALDO += valor
            EXTRATO += f"Depósito: R$ {valor:.2f}\n"

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "2":
        valor = float(input("Informe o valor do saque: "))

        EXCEDEU_SALDO = valor > SALDO

        EXCEDEU_LIMITE = valor > LIMITE

        EXCEDEU_SAQUES = NUMERO_SAQUES >= LIMITE_SAQUES

        if EXCEDEU_SALDO:
            print("Operação falhou! Você não tem saldo suficiente.")

        elif EXCEDEU_LIMITE:
            print("Operação falhou! O valor do saque excede o limite.")

        elif EXCEDEU_SAQUES:
            print("Operação falhou! Número máximo de saques excedido.")

        elif valor > 0:
            SALDO -= valor
            EXTRATO += f"Saque: R$ {valor:.2f}\n"
            NUMERO_SAQUES += 1

        else:
            print("Operação falhou! O valor informado é inválido.")

    elif opcao == "3":
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not EXTRATO else EXTRATO)
        print(f"\nSaldo: R$ {SALDO:.2f}")
        print("==========================================")

    elif opcao == "0":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
        sleep(5)
    sleep(2)
    system("clear")
