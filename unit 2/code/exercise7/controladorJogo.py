from AbstractControladorJogo import *
import random


class ControladorJogo(AbstractControladorJogo):
    def __init__(self):
        self.__personagems = []
        self.__baralho = []

    @property
    def baralho(self) -> list:
        return self.__baralho

    @property
    def personagems(self) -> list:
        return self.__personagems

    def inclui_personagem_na_lista(
        self,
        energia: int,
        habilidade: int,
        velocidade: int,
        resistencia: int,
        tipo: Tipo
    ) -> Personagem:
        personagem = Personagem(
            energia,
            habilidade,
            velocidade,
            resistencia,
            tipo
        )
        self.__personagems.append(personagem)
        return personagem

    def inclui_carta_no_baralho(self, personagem: Personagem) -> Carta:
        carta = Carta(personagem)
        self.__baralho.append(carta)
        return carta

    def jogada(self, mesa: Mesa) -> Jogador:

        jogador1 = mesa.jogador1
        jogador2 = mesa.jogador2
        carta_jogador1 = mesa.carta_jogador1
        carta_jogador2 = mesa.carta_jogador2

        if (
                carta_jogador1.valor_total_carta() >
                carta_jogador2.valor_total_carta()):

            jogador1.inclui_carta_na_mao(carta_jogador1)
            jogador1.inclui_carta_na_mao(carta_jogador2)
            return jogador1

        elif (
                carta_jogador1.valor_total_carta() <
                carta_jogador2.valor_total_carta()):

            jogador2.inclui_carta_na_mao(carta_jogador1)
            jogador2.inclui_carta_na_mao(carta_jogador2)
            return jogador2

        else:
            jogador1.inclui_carta_na_mao(carta_jogador1)
            jogador2.inclui_carta_na_mao(carta_jogador2)
            return None
