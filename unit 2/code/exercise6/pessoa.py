
#ok

from abc import ABC, abstractmethod
from abstractPessoa import AbstractPessoa


class Pessoa(AbstractPessoa, ABC):
    def __init__(self, codigo: int, nome: str):
        if isinstance(nome, str):
            self.__nome = nome
        if isinstance(codigo, int):
            self.__codigo = codigo
    
    @property
    def nome(self):
        return self.__nome
    @property
    def codigo(self):
        return self.__codigo
    
    @nome.setter
    def nome(self, nome):
        if isinstance(nome, str):
            self.__nome = nome
    @codigo.setter
    def codigo(self, codigo):
        if isinstance(codigo, int):
            self.__codigo = codigo
    