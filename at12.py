def calcular_media_ponderada(nota1, nota2):
    # Calcula a média ponderada
    media_ponderada = (nota1 * 1 + nota2 * 2) / 3
    return media_ponderada

def verificar_aprovacao(media):
    # Verifica se a média é maior ou igual a 70
    if media >= 70:
        return "Aprovado"
    else:
        return "Reprovado"

def main():
    # Solicita as notas das provas
    nota1 = float(input("Digite a nota da primeira prova: "))
    nota2 = float(input("Digite a nota da segunda prova: "))

    # Calcula a média ponderada
    media = calcular_media_ponderada(nota1, nota2)

    # Verifica se o aluno foi aprovado ou reprovado
    resultado = verificar_aprovacao(media)

    # Imprime o resultado
    print("A média do aluno é:", media)
    print("Situação do aluno:", resultado)

if __name__ == "__main__":
    main()