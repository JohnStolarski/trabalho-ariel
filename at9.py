def main():
    salario = float(input("Digite o salário do trabalhador: "))
    prestacao = float(input("Digite o valor da prestação do empréstimo: "))

    limite_prestacao = salario * 0.2

    if prestacao > limite_prestacao:
        print("Empréstimo não concedido")
    else:
        print("Empréstimo concedido")

if __name__ == "__main__":
    main()