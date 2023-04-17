
#ok

from abc import ABC, abstractmethod

class AbstractTipoChamado(ABC):

	@abstractmethod
	def __init__(self):
		pass

	@property
	@abstractmethod
	def codigo(self) -> int:
		pass

	@property
	@abstractmethod
	def descricao(self) -> str:
		pass

	@property
	@abstractmethod
	def nome(self) -> str:
		pass