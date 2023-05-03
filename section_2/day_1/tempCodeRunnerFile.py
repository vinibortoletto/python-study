class Ventilador:
  def __init__(self, cor, potencia, tensao, preco):
    self.preco = preco
    self.cor = cor
    self._potencia = potencia
    self.tensao = tensao
    self.__ligado = False
    self.__velocidade = 0
    self.__velocidade_maxima = 3
    self.__corrente_atual_no_motor = 0

  def ligar (self):
    self.__ligado = True

  def desligar (self):
    self.__ligado = False