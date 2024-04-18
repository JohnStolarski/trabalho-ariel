def classificar_atleta(idade):
    if idade >= 5 and idade <= 7:
        return "Infantil A"
    elif idade >= 8 and idade <= 10:
        return "Infantil B"
    elif idade >= 11 and idade <= 13:
        return "Juvenil A"
    elif idade >= 14 and idade <= 17:
        return "Juvenil B"
    else:
        return "Sênior"

def main():
    idade = int(input("Digite a idade do atleta: "))

    categoria = classificar_atleta(idade)
    print("O atleta está na categoria:", categoria)

if __name__ == "__main__":
    main()