def verificar_triangulo(a, b, c):
    if a < b + c and b < a + c and c < a + b:
        if a == b == c:
            return "equilátero"
        elif a == b or a == c or b == c:
            return "isósceles"
        else:
            return "escaleno"
    else:
        return "não é um triângulo"

def main():
    a = float(input("Digite o comprimento do primeiro lado do triângulo: "))
    b = float(input("Digite o comprimento do segundo lado do triângulo: "))
    c = float(input("Digite o comprimento do terceiro lado do triângulo: "))

    tipo_triangulo = verificar_triangulo(a, b, c)
    print("O triângulo é:", tipo_triangulo)

if __name__ == "__main__":
    main()