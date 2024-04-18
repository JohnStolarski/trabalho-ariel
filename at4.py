import math

def main():
    numero = float(input("Digite um número: "))

    if numero > 0:
        quadrado = numero ** 2
        raiz_quadrada = math.sqrt(numero)
        print("O número ao quadrado é:", quadrado)
        print("A raiz quadrada do número é:", raiz_quadrada)
    else:
        print("O número não é positivo.")

if __name__ == "__main__":
    main()