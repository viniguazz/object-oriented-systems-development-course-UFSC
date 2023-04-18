from AbstractCarta import *
from Personagem import *


class Carta(AbstractCarta):

    def __init__(self, personagem: Personagem):
        if isinstance(personagem, Personagem):
            self.__personagem = personagem

    '''
    Soma e retorna todos os valores dos atributos do personagem da Carta
    @return Retorna o somatorio de todos os atributos do personagem da Carta
    '''
    def valor_total_carta(self) -> int:
        personagem = self.__personagem
        sum = (
            personagem.energia +
            personagem.habilidade +
            personagem.velocidade +
            personagem.resistencia)
        return sum

    @property
    def personagem(self) -> Personagem:
        return self.__personagem
