from figura_geometrica import FiguraGeometrica
from math import pi as PI


class Circulo(FiguraGeometrica):
    def __init__(self, raio):
        self.raio = raio

    def area(self):
        return PI * self.radio * self.raio

    def perimetro(self):
        return PI * self.raio * 2
