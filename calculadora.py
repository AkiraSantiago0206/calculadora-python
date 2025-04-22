def calculadora():
    print("Bem-vindo à Calculadora Simples!")
    print("Escolha uma operação:")
    print("1. Soma")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")

    while True:
        try:
            escolha = int(input("Digite o número da operação (1-4): "))
            if escolha in [1, 2, 3, 4]:
                break
            else:
                print("Escolha inválida! Digite um número entre 1 e 4.")
        except ValueError:
            print("Entrada inválida! Digite um número.")

    while True:
        try:
            num1 = float(input("Digite o primeiro número: "))
            num2 = float(input("Digite o segundo número: "))
            break
        except ValueError:
            print("Entrada inválida! Digite números válidos.")

    if escolha == 1:
        resultado = num1 + num2
        print(f"{num1} + {num2} = {resultado}")
    elif escolha == 2:
        resultado = num1 - num2
        print(f"{num1} - {num2} = {resultado}")
    elif escolha == 3:
        resultado = num1 * num2
        print(f"{num1} * {num2} = {resultado}")
    elif escolha == 4:
        if num2 != 0:
            resultado = num1 / num2
            print(f"{num1} / {num2} = {resultado}")
        else:
            print("Erro: Divisão por zero não é permitida!")

if __name__ == "__main__":
    calculadora()