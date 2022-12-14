#Felipe Paimilla , Nicolas ramires
class Figura:
    def __init__(self, lados, area, perimetro):
        self.lados = lados
        self.area = area
        self.perimetro = perimetro

    def imprimir(self):
        print("Lados: ", self.lados)
        print("Area: ", self.area)
        print("Perimetro: ", self.perimetro)

class Circulo(Figura):
    def __init__(self, radio):
        self.radio = radio
        self.area = 3.1416 * (radio ** 2)
        self.perimetro = 2 * 3.1416 * radio
        super().__init__(1, self.area, self.perimetro)

    def imprimir(self):
        print("--------------Circulo--------------")
        super().imprimir()
        print("Radio: ", self.radio)

class Triangulo(Figura):
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
        self.area = (lado1 * lado2) / 2
        self.perimetro = lado1 + lado2 + lado3
        super().__init__(3, self.area, self.perimetro)

    def imprimir(self):
        print("--------------Triangulo--------------")
        super().imprimir()
        print("Lado 1: ", self.lado1)
        print("Lado 2: ", self.lado2)
        print("Lado 3: ", self.lado3)
        if self.lado1 == self.lado2 and self.lado2 == self.lado3:
            print("Es un triangulo equilatero")
        elif self.lado1 == self.lado2 or self.lado1 == self.lado3 or self.lado2 == self.lado3:
            print("Es un triangulo isosceles")
        else:
            print("Es un triangulo escaleno")

class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado
        self.area = lado ** 2
        self.perimetro = lado * 4
        super().__init__(4, self.area, self.perimetro)

    def imprimir(self):
        print("--------------Cuadrado--------------")
        super().imprimir()
        print("Lado: ", self.lado)

class Rectangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        self.area = base * altura
        self.perimetro = (base * 2) + (altura * 2)
        super().__init__(4, self.area, self.perimetro)

    def imprimir(self):
        print("--------------Rectangulo--------------")
        super().imprimir()
        print("Base: ", self.base)
        print("Altura: ", self.altura)

def main():
    n = int(input("Ingrese un numero: "))
    circulo = Circulo(n)
    circulo.imprimir()

    triangulo = Triangulo(n, n, n)
    triangulo.imprimir()

    cuadrado = Cuadrado(n)
    cuadrado.imprimir()

    rectangulo = Rectangulo(n, n*2)
    rectangulo.imprimir()


if __name__ == '__main__':
    main()