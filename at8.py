def calcular_media(nota1, nota2):
    return (nota1 + nota2) / 2

def main():
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))

    # Verifica se as notas são válidas
    if 0.0 <= nota1 <= 10.0 and 0.0 <= nota2 <= 10.0:
        media = calcular_media(nota1, nota2)
        print("A média das notas é:", media)
    else:
        print("Uma ou ambas as notas não são válidas. As notas devem estar entre 0.0 e 10.0.")

if __name__ == "__main__":
    main()