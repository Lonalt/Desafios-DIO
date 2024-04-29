"""DESAFIO SISTEMA BANCARIO MUDULARIZADO"""

from os import system
from time import sleep
import time
from random import randint
from random import seed

def cria_conta(contas = None):
    """Cria uma conta bancária."""
    seed(time.time())
    numero_conta = randint(1, 9999)
    agencia = randint(1, 999)
    nome = input("Informe o nome do titular: ")
    endereco = input("Informe o endereço do titular: ")
    cpf = input("Informe o CPF do titular: ")
    saldo = 0
    conta = {
        "nome": nome,
        "endereco": endereco,
        "cpf": cpf,
        "saldo": saldo,
        "numero_conta": f"{numero_conta:04}",
        "agencia": f"{agencia:03}"
    }
    contas.append(conta)
    return conta["numero_conta"]

def depositar(contas = None):
    """Realiza um depósito na conta."""
    numero_conta = input("Informe o número da conta: ")
    valor = float(input("Informe o valor do depósito: "))
    for conta in contas:
        if conta["numero_conta"] == numero_conta:
            conta["saldo"] += valor
            print("Depósito realizado com sucesso.")
            break
    else:
        print("Conta não encontrada.")

def sacar(contas = None):
    """Realiza um saque na conta."""
    numero_conta = input("Informe o número da conta: ")
    valor = float(input("Informe o valor do saque: "))
    for conta in contas:
        if conta["numero_conta"] == numero_conta:
            if valor > conta["saldo"]:
                print("Operação falhou! Você não tem saldo suficiente.")
            else:
                conta["saldo"] -= valor
            print("Saque realizado com sucesso.")
            break
    else:
        print("Conta não encontrada.")

def extrato(contas):
    """Retorna o extrato da conta."""
    numero_conta = input("Informe o número da conta: ")
    for conta in contas:
        if conta["numero_conta"] == numero_conta:
            return f"Extrato da conta {conta['numero_conta']}:\n{conta['saldo']:.2f}"
    return "Conta não encontrada."

def menu():
    """Exibe o menu."""
    print("""SISTEMA BANCÁRIO""")
    print("""
          [1] Criar conta
          [2] Depositar
          [3] Sacar
          [4] Extrato
          [0] Sair
        """)
    return input("=> ")

def main():
    """Função principal."""
    contas = []
    while True:
        opcao = menu()
        if opcao == "1":
            conta = cria_conta(contas)
            print(f"Conta criada: {conta}")
            sleep(5)
        elif opcao == "2":
            depositar(contas)
            sleep(2)
        elif opcao == "3":
            sacar(contas)
            sleep(2)
        elif opcao == "4":
            print(extrato(contas))
            sleep(2)
        elif opcao == "0":
            break
        else:
            print("Opção inválida.")
        system("clear")

if __name__ == "__main__":
    main()
