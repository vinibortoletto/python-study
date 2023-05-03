from ventilador import Ventilador


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.ventilador = None

    def comprar_ventilador(self, ventilador):
        self.ventilador = ventilador

    def __str__(self):
        return f"{self.nome} possui um ventilador."


ventilador = Ventilador(cor="branco", potencia=250, tensao=220, preco=100)
pessoa = Pessoa(nome="Vinicius", idade=29)
pessoa.comprar_ventilador(ventilador=ventilador)
print(pessoa)
