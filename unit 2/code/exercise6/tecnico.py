
#ok

from pessoa import Pessoa


class Tecnico(Pessoa):
    def __init__(self, codigo: int, nome: str):
        super().__init__(nome, codigo)