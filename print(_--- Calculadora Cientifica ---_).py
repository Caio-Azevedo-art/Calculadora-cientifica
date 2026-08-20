print("--- Calculadora Cientifica ---")
print("1. Soma (+)")
print("2. Subtração (-)")
print("3. Multiplicação (*)")
print("4. Divisão (/)")

opcao = input("Escolha a opção (1/2/3/4): ")

num1 = float(input("Digite o primeiro numero: "))
num2 = float(input("Digite o segundo numero: "))

if opcao == '1':
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")
elif opcao == '2':
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")
elif opcao == '3':
    resultado = num1 * num2
    print(f"Resultado: {num1} * {num2} = {resultado}")
elif opcao == '4':
    if num2 != 0:
        resultado = num1 / num2
        print(f"Resultado: {num1} / {num2} = {resultado}")
    else:
        print("Erro: Divisão por zero não permitida!")
else:
    print("Opção Inválida!")