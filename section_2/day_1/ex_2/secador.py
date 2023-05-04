from eletrodomestico import Eletrodomestico


class Secador(Eletrodomestico):
    pass


secador = Secador("preto", 200, 220, 130)

print(f"A cor do secador é: {secador.cor}")
