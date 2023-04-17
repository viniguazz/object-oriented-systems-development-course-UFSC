from abc import ABC, abstractmethod
from usuario_bu import UsuarioBU

class Funcionario(UsuarioBU):
    
    @abstractmethod
    def __init__(self, departamento : str, cpf : int , dias_de_emprestimo : int):
        super().__init__(cpf, dias_de_emprestimo)
        if isinstance(departamento, str):
            self.__departamento = departamento
        
    @property
    def departamento(self):
        return self.__departamento
    @departamento.setter
    def departamento(self, departamento):
        if isinstance(departamento, str):
            self.__departamento = departamento

    def emprestar(self, titulo_livro):
        if isinstance(titulo_livro, str):
            return f"do departamento \"{self.departamento}\" {super().emprestar(titulo_livro)}"

    def devolver(self, titulo_livro):
        if isinstance(titulo_livro, str):
            return f'do departamento \"{self.departamento}\" {super().devolver(titulo_livro)}'