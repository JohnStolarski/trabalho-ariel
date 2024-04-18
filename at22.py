def calcular_preco_final(valor, estado):
    impostos = {'MG': 0.07, 'SP': 0.12, 'RJ': 0.15, 'MS': 0.08}

    if estado in impostos:
        taxa_imposto = impostos[estado]
        preco_final = valor * (1 + taxa_imposto)
        return preco_final
    else:
        return "Erro: Estado inválido."

def main():
    valor = float(input("Digite o valor do produto: "))
    estado = input("Digite a sigla do estado destino (MG, SP, RJ, MS): ").upper()

    preco_final = calcular_preco_final(valor, estado)
    print("O preço final do produto no estado", estado, "é:", preco_final)

if __name__ == "__main__":
    main()