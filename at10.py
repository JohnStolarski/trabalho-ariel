def soma_algarismos(numero):
    soma = 0
    while numero > 0:
        digito = numero % 10
        soma += digito
        numero //= 10
    return soma

def main():
    numero = int(input("Digite um número inteiro maior que zero: "))

    if numero <= 0:
        print("Número inválido.")
    else:
        resultado = soma_algarismos(numero)
        print("A soma dos algarismos do número é:", resultado)

if __name__ == "__main__":
    main()