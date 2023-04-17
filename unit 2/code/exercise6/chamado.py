
#ok

from abstractChamado import AbstractChamado
from tipoChamado import TipoChamado
from datetime import date as Date
from cliente import Cliente
from tecnico import Tecnico


class Chamado(AbstractChamado):
    def __init__(
            self,
            data: Date,
            cliente: Cliente,
            tecnico: Tecnico,
            titulo: str,
            descricao: str,
            prioridade: int,
            tipo: TipoChamado):

        if isinstance(data, Date):
            self.__data = data
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
        if isinstance(tecnico, Tecnico):
            self.__tecnico = tecnico
        if isinstance(titulo, str):
            self.__titulo = titulo
        if isinstance(descricao, str):
            self.__descricao = descricao
        if isinstance(prioridade, int):
            self.__prioridade = prioridade
        if isinstance(tipo, TipoChamado):
            self.__tipo = tipo
        
    @property
    def data(self):
        return self.__data
    @property
    def cliente(self):
        return self.__cliente
    @property
    def tecnico(self):
        return self.__tecnico
    @property
    def titulo(self):
        return self.__titulo
    @property
    def descricao(self):
        return self.__descricao
    @property
    def prioridade(self):
        return self.__prioridade
    @property
    def tipo(self):
        return self.__tipo

    @data.setter
    def data(self, data):
        if isinstance(data, Date):
            self.__data = data
    @cliente.setter
    def cliente(self, cliente):
        if isinstance(cliente, Cliente):
            self.__cliente = cliente
    @tecnico.setter
    def tecnico(self, tecnico):
        if isinstance(tecnico, Tecnico):
            self.__tecnico = tecnico
    @titulo.setter
    def titulo(self, titulo):
        if isinstance(titulo, str):
            self.__titulo = titulo
    @descricao.setter
    def descricao(self, descricao):
        if isinstance(descricao, str):
            self.__descricao = descricao
    @prioridade.setter
    def prioridade(self, prioridade):
        if isinstance(prioridade, int):
            self.__prioridade = prioridade
    @tipo.setter
    def tipo(self, tipo):
        if isinstance(tipo, TipoChamado):
            self.__tipo = tipo

