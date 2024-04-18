def verificar_aposentadoria(idade, tempo_de_servico):
    if idade >= 65 or tempo_de_servico >= 30 or (idade >= 60 and tempo_de_servico >= 25):
        return True
    else:
        return False

def main():
    idade = int(input("Digite a idade do trabalhador: "))
    tempo_de_servico = int(input("Digite o tempo de serviço do trabalhador: "))

    if verificar_aposentadoria(idade, tempo_de_servico):
        print("O trabalhador pode se aposentar.")
    else:
        print("O trabalhador não pode se aposentar.")

if __name__ == "__main__":
    main()