
#ok

from abstractControladorPessoas import AbstractControladorPessoas
from cliente import Cliente
from tecnico import Tecnico


class ControladorPessoas(AbstractControladorPessoas):
    def __init__(self):
        self.__clientes = []
        self.__tecnicos = []
    
    @property
    def clientes(self):
        return self.__clientes
    @property
    def tecnicos(self):
        return self.__tecnicos

    def inclui_cliente(self, codigo, nome):
        novo_cliente = Cliente(codigo, nome)
        for _ in self.__clientes:
            if _.codigo == novo_cliente.codigo:
                return
        self.__clientes.append(novo_cliente)
        return novo_cliente
    
    def inclui_tecnico(self, nome, codigo):
        novo_tecnico = Tecnico(codigo, nome)
        for _ in self.__tecnicos:
            if _.codigo == novo_tecnico.codigo:
                return        
        self.__tecnicos.append(novo_tecnico)
        return novo_tecnico