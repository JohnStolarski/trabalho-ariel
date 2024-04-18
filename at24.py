import math

def calcular_preco(chegada, partida):
    hora_chegada, minuto_chegada = chegada
    hora_partida, minuto_partida = partida

    minutos_chegada = hora_chegada * 60 + minuto_chegada
    minutos_partida = hora_partida * 60 + minuto_partida

    total_minutos = minutos_partida - minutos_chegada
    total_horas = math.ceil(total_minutos / 60)

    if total_horas <= 2:
        preco = total_horas * 1.00
    elif total_horas <= 4:
        preco = 2 * 1.00 + (total_horas - 2) * 1.40
    else:
        preco = 2 * 1.00 + 2 * 1.40 + (total_horas - 4) * 2.00

    return preco

def main():
    chegada = tuple(map(int, input("Digite o momento de chegada (hora minuto): ").split()))
    partida = tuple(map(int, input("Digite o momento de partida (hora minuto): ").split()))

    preco = calcular_preco(chegada, partida)
    print("O preço cobrado pelo estacionamento é R$ {:.2f}".format(preco))

if __name__ == "__main__":
    main()