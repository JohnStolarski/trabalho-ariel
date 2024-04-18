import math

def main():
    numero = int(input("Digite um número inteiro: "))

    if numero < 0:
        print("Número inválido.")
    else:
        logaritmo = math.log(numero)
        print("O logaritmo do número é:", logaritmo)

if __name__ == "__main__":
    main()