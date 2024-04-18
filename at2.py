import math

def calcular_raiz_quadrada(numero):
    if numero >= 0:
        return math.sqrt(numero)
    else:
        return "Número inválido. Não é possível calcular a raiz quadrada de um número negativo."

def main():
    numero = float(input("Digite um número: "))

    resultado = calcular_raiz_quadrada(numero)
    print(resultado)

if __name__ == "__main__":
    main()