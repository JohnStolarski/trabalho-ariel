def encontrar_maior_numero(numero1, numero2):
    if numero1 > numero2:
        return numero1
    elif numero2 > numero1:
        return numero2
    else:
        return "Números iguais"

def main():
    numero1 = float(input("Digite o primeiro número: "))
    numero2 = float(input("Digite o segundo número: "))

    maior_numero = encontrar_maior_numero(numero1, numero2)
    print("O maior número é:", maior_numero)

if __name__ == "__main__":
    main()