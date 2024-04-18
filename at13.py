def calcular_media(nota_lab, nota_semestral, nota_exame):
    # Calcula a média ponderada das notas com os respectivos pesos
    media = (nota_lab * 2 + nota_semestral * 3 + nota_exame * 5) / 10
    return media

def verificar_situacao_aluno(media):
    # Verifica a situação do aluno com base na média calculada
    if media < 3.0:
        return "Reprovado"
    elif 3.0 <= media < 5.0:
        return "Recuperação"
    else:
        return "Aprovado"

def main():
    # Solicita as notas ao usuário
    nota_lab = float(input("Digite a nota do trabalho de laboratório (0 a 10): "))
    nota_semestral = float(input("Digite a nota da avaliação semestral (0 a 10): "))
    nota_exame = float(input("Digite a nota do exame final (0 a 10): "))

    # Calcula a média ponderada
    media = calcular_media(nota_lab, nota_semestral, nota_exame)

    # Verifica a situação do aluno
    situacao = verificar_situacao_aluno(media)

    # Imprime o resultado
    print("Média do aluno:", media)
    print("Situação do aluno:", situacao)

if __name__ == "__main__":
    main()