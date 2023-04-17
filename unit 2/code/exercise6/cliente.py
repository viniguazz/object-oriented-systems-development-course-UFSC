
#ok

from pessoa import Pessoa


class Cliente(Pessoa):
    def __init__(self, codigo: int, nome: str):
        super().__init__(codigo, nome)

