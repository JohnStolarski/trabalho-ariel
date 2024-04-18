def encontrar_maior_e_diferenca(numero1, numero2):
    maior_numero = max(numero1, numero2)
    menor_numero = min(numero1, numero2)
    diferenca = maior_numero - menor_numero
    return maior_numero, diferenca

def main():
    numero1 = int(input("Digite o primeiro número inteiro: "))
    numero2 = int(input("Digite o segundo número inteiro: "))

    maior_numero, diferenca = encontrar_maior_e_diferenca(numero1, numero2)

    print("O maior número é:", maior_numero)
    print("A diferença entre os números é:", diferenca)

if __name__ == "__main__":
    main()