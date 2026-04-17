# Sistema de calculadora desenvolvido em Python
# Contém operações matemáticas básicas, média, fatorial,
# sequência de Fibonacci, tabuada e equação do 2º grau
# Desenvolvido para fins acadêmicos


# Importa a biblioteca math para usar a raiz quadrada
import math

# Função para exibir títulos padronizados
def titulo(texto):
    print("\n" + "=" * 30)
    print(f"{texto.center(30)}")
    print("=" * 30)

# Função para pausar o programa
def pausar():
    input("\nPressione ENTER para continuar...")

# Função para ler dois números com validação
def ler_numeros():
    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            return num1, num2
        except ValueError:
            print("Erro: digite apenas números válidos.")


# Loop principal do sistema que mantém o programa em execução
# até o usuário escolher a opção de sair
while True:
    titulo("MENU PRINCIPAL")
    print("1 - Soma")
    print("2 - Subtração")
    print("3 - Multiplicação")
    print("4 - Divisão")
    print("5 - Média")
    print("6 - Fatorial")
    print("7 - Fibonacci")
    print("8 - Tabuada")
    print("9 - Equação do 2º grau")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    # Soma
    if opcao == "1":
        titulo("SOMA")
        num1, num2 = ler_numeros()
        print("Resultado:", num1 + num2)
        pausar()

    # Subtração
    elif opcao == "2":
        titulo("SUBTRAÇÃO")
        num1, num2 = ler_numeros()
        print("Resultado:", num1 - num2)
        pausar()

    # Multiplicação
    elif opcao == "3":
        titulo("MULTIPLICAÇÃO")
        num1, num2 = ler_numeros()
        print("Resultado:", num1 * num2)
        pausar()

    # Divisão
    elif opcao == "4":
        titulo("DIVISÃO")
        num1, num2 = ler_numeros()

        if num2 == 0:
            print("Erro: divisão por zero não é permitida.")
        else:
            print("Resultado:", num1 / num2)

        pausar()

    # Média
    elif opcao == "5":
        titulo("MÉDIA")

        # Trata possíveis erros de entrada do usuário
        try:
            quantidade = int(input("Quantos números deseja calcular a média? "))

            if quantidade <= 0:
                print("Quantidade inválida.")
            else:
                soma = 0

                for i in range(quantidade):
                    while True:
                        try:
                            numero = float(input(f"Digite o {i+1}º número: "))
                            soma += numero
                            break
                        except ValueError:
                            print("Erro: digite um número válido.")

                media = soma / quantidade
                print("Média:", media)

        except ValueError:
            print("Erro: digite um número inteiro válido.")

        pausar()

    # Fatorial
    elif opcao == "6":
        titulo("FATORIAL")

        try:
            numero = int(input("Digite um número inteiro: "))

            if numero < 0:
                print("Erro: não existe fatorial de número negativo.")
            else:
                # Inicializa o valor do fatorial
                fatorial = 1

                for i in range(1, numero + 1):
                    fatorial *= i

                print(f"Fatorial de {numero} é {fatorial}")

        except ValueError:
            print("Erro: digite um número inteiro válido.")

        pausar()

    # Fibonacci
    elif opcao == "7":
        titulo("FIBONACCI")

        try:
            n = int(input("Quantos termos deseja ver? "))

            if n <= 0:
                print("Digite um número maior que zero.")
            else:
                # Inicializa os dois primeiros termos da sequência
                a, b = 0, 1

                print("Sequência de Fibonacci:")

                for i in range(n):
                    print(a, end=" ")
                    a, b = b, a + b

                print()

        except ValueError:
            print("Erro: digite um número inteiro válido.")

        pausar()

    # Tabuada
    elif opcao == "8":
        titulo("TABUADA")

        try:
            numero = int(input("Digite o número da tabuada: "))
            limite = int(input("Até qual número deseja calcular? "))

            if limite <= 0:
                print("O limite deve ser maior que zero.")
            else:
                print(f"\nTabuada do {numero}:\n")

                for i in range(1, limite + 1):
                    print(f"{numero} x {i} = {numero * i}")

        except ValueError:
            print("Erro: digite números inteiros válidos.")

        pausar()

    # Equação do 2º grau
    elif opcao == "9":
        titulo("EQUAÇÃO DO 2º GRAU")

        try:
            a = float(input("Digite o valor de a: "))
            b = float(input("Digite o valor de b: "))
            c = float(input("Digite o valor de c: "))

            if a == 0:
                print("Isso não é uma equação do 2º grau.")
            else:
                # Calcula o delta da equação (b² - 4ac)
                delta = b**2 - 4*a*c

                if delta < 0:
                    print("Não existem raízes reais.")

                elif delta == 0:
                    x = -b / (2*a)
                    print("Existe apenas uma raiz:", x)

                else:
                    x1 = (-b + math.sqrt(delta)) / (2*a)
                    x2 = (-b - math.sqrt(delta)) / (2*a)

                    print("Duas raízes:")
                    print("x1 =", x1)
                    print("x2 =", x2)

        except ValueError:
            print("Erro: digite valores numéricos válidos.")

        pausar()

    # Sair
    elif opcao == "0":
        titulo("ENCERRANDO")
        print("Saindo do programa...")
        break

    # Opção inválida
    else:
        print("Opção inválida. Tente novamente.")