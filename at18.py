def verificar_divisibilidade(numero):
    if numero % 3 == 0 and numero % 5 == 0:
        return False
    elif numero % 3 == 0 or numero % 5 == 0:
        return True
    else:
        return False

def main():
    numero = int(input("Digite um número inteiro: "))

    if verificar_divisibilidade(numero):
        print("O número é divisível por 3 ou por 5, mas não simultaneamente pelos dois.")
    else:
        print("O número não é divisível por 3 ou por 5, ou é divisível simultaneamente pelos dois.")

if __name__ == "__main__":
    main()