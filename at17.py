def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Impossível dividir por zero."

def main():
    print("Selecione a operação desejada:")
    print("1. Somar")
    print("2. Subtrair")
    print("3. Multiplicar")
    print("4. Dividir")

    escolha = input("Digite o número da operação desejada: ")

    if escolha in ('1', '2', '3', '4'):
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))

        if escolha == '1':
            print("Resultado da soma:", somar(num1, num2))
        elif escolha == '2':
            print("Resultado da subtração:", subtrair(num1, num2))
        elif escolha == '3':
            print("Resultado da multiplicação:", multiplicar(num1, num2))
        elif escolha == '4':
            print("Resultado da divisão:", dividir(num1, num2))
    else:
        print("Opção inválida.")

if __name__ == "__main__":
    main()