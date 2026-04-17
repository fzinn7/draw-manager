# Sistema de sorteio desenvolvido em Python
# Permite adicionar, listar, sortear e remover participantes
# Desenvolvido para fins acadêmicos

import random

def titulo(texto):
    print("\n" + "=" * 30)
    print(f"{texto.center(30)}")
    print("=" * 30)

def pausar():
    input("\nPressione ENTER para continuar...")

# Lista que armazena os nomes dos participantes
participantes = []

# Loop principal que mantém o programa em execução
while True:
    titulo("SORTEIO")

    print("1 - Adicionar participante")
   
    print("2 - Sortear")
    print("3 - Remover participante")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

# Adicionar
    if opcao == "1":
        nome = input("Digite o nome do participante: ").strip()

# Verifica se o nome é válido e evita duplicatas
        if nome == "":
            print("Nome inválido.")
        elif nome in participantes:
            print("Esse nome já está na lista.")
        else:
            participantes.append(nome)
            print(f"{nome} foi adicionado com sucesso!")

            print(f"\nTotal de participantes: {len(participantes)}")

            for i, nome in enumerate(participantes, 1):
                print(f"{i} - {nome}")

        pausar()


# Sortear
    elif opcao == "2":
        titulo("SORTEIO")

        if len(participantes) == 0:
            print("Não há participantes para sortear.") 
        else:
            # Realiza o sorteio aleatório de um participante
            sorteado = random.choice(participantes)
            print(f"O sorteado foi: {sorteado}")

            remover = input("Deseja remover o sorteado da lista? (s/n): " ).lower()

            if remover == "s":
                participantes.remove(sorteado)
                print(f"{sorteado} foi removido da lista.")

        pausar()

# Permite remover um participante da lista pelo índice
    elif opcao == "3":
        titulo("REMOVER PARTICIPANTE")

        if len(participantes) == 0:
            print("Nenhum participante cadastrado ainda.")
        else:
            for i, participante in enumerate(participantes, 1):
                print(f"{i} - {participante}")

            try:
                indice = int(input("Digite o número do participante para remover: "))
                if 1 <= indice <= len(participantes):
                    confirmar = input("Tem certeza que deseja remover? (s/n): ").lower()

                    if confirmar == "s":
                        removido = participantes.pop(indice - 1)
                        print(f"{removido} foi removido.")
                    else:
                        print("Remoção cancelada.")
                else:
                    print("Número inválido.")

            except ValueError:
                print("Digite um número válido")

        pausar()

    elif opcao == "0":
        titulo("ENCERRANDO")
        print("Saindo...")
        break

    else:
        print("Opção inválida.")