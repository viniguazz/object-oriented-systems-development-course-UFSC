from abc import ABC, abstractmethod


class UsuarioBU(ABC):

    @abstractmethod
    def __init__(self, cpf: int, dias_de_emprestimo: int):
        if isinstance(cpf, int):
            self.__cpf = cpf
        if isinstance(dias_de_emprestimo, int):
            self.__dias_de_emprestimo = dias_de_emprestimo

    @property
    def cpf(self):
        return self.__cpf
    @property
    def dias_de_emprestimo(self):
        return self.__dias_de_emprestimo

    @cpf.setter
    def cpf(self, cpf):
        if isinstance(cpf, int):
            self.__cpf = cpf
    @dias_de_emprestimo.setter
    def dias_de_emprestimo(self, dias_de_emprestimo):
        if isinstance(dias_de_emprestimo, int):
            self.__dias_de_emprestimo = dias_de_emprestimo
    
    @abstractmethod
    def emprestar(self, titulo_livro):
        if isinstance(titulo_livro, str):
            return f"pegou emprestado o livro: {titulo_livro} com {self.__dias_de_emprestimo} dias de prazo"
    
    @abstractmethod
    def devolver(self, titulo_livro):
        if isinstance(titulo_livro, str):
            return f"devolveu o livro: {titulo_livro}"


        
