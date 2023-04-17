
#ok

from abstractControladorChamados import AbstractControladorChamados
from tipoChamado import TipoChamado
from chamado import Chamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico
from collections import defaultdict


class ControladorChamados(AbstractControladorChamados):
    
    def __init__(self):
        self.__chamados = []
        self.__tipos_de_chamados = []
    
    
    def total_chamados_por_tipo(self, tipo : TipoChamado):
        counter = 0
        for _ in self.__chamados:
            if _.tipo.codigo == tipo.codigo:
                counter += 1
        return counter

    def inclui_chamado(self, data : Date, cliente : Cliente, tecnico : Tecnico, titulo : str, descricao : str, prioridade : int, tipo : TipoChamado):
        novo_chamado = Chamado(data, cliente, tecnico, titulo, descricao, prioridade, tipo)
        if (len(vars(novo_chamado)) == 7):
            for _ in self.__chamados:
                if (_.data == novo_chamado.data and _.cliente == novo_chamado.cliente and _.tecnico == novo_chamado.tecnico and _.tipo == novo_chamado.tipo):
                    return
            self.__chamados.append(novo_chamado)
            return novo_chamado
        return
    
    def inclui_tipochamado(self, codigo, nome, descricao):
        tipo = TipoChamado(codigo, nome, descricao)
        for _ in self.__tipos_de_chamados:
            if _.codigo == tipo.codigo:
                return
        self.__tipos_de_chamados.append(tipo)
        return tipo
    
    @property
    def tipos_chamados(self):
        return self.__tipos_de_chamados