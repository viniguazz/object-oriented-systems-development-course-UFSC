
# Intro 

OOP is a method that aims to organize the code in a way that get closer to real world.

* Object: a computational representation of a certain entity, geared towards executing a certain task, with well defined limits. It's a collection of data (attributes) and operations (methods) that operate the data, representing a logic entity in the system.

* Abstraction: identify the important aspects of a phenomenon and ignore it's details.

* Class: the defition of a group comprised of objects that share common properties and behaviors. 

An object is an instatiation of a class.

Attributes are variables that describe an object. Methods are functions (for the imperative paradigm) that operate over an object.

### Declaring classes in Python

	class Car:

	def __init__(self, model: str, color: str, licensePlate: str):      # constructor method
		self.model = model
		self.color = color
		self.licensePlate = licensePlate
		self.speed = 0

	def honk(self):
		print('car', self.model, 'honked')

	def accelerate(self):
		self.speed += 10

	def brake(self):
		self.speed -= 10
		if self.speed < 0:
			self.speed = 0

The 'self' keyword is a reference to the object that will be instantiated. It's mandatory and must always be the first argument of any method.

The 'constructor' is a method that is automatically triggered whenever a class is instantiated.

### Instantiation

	def main():
		car1 = Car('Gol', 'red', 'LCC-555')

		car.honk()
		car.accelerate()

Attention: notice that SELF isn't passed whenever the methods of an instantiated object are called. Notice that we use dot notation.

### Pillars of abstraction

* Encapsulation
* Inheritance
* Composition
* Polymorphism

# Inheritance

It's a mechanism that allows reuse of implemented code. It defines a relationship between classes, in which we verify what's common.
Classes share their structure/behaviors. It's a specialization/generalization relationship.

Note: private attributes are preceded by two underscores in python.

Note2: decorators

	In Python syntax, the "@" symbol is used as a decorator in Object-Oriented Programming (OOP) to modify the behavior of a function or method.

	A decorator is a special type of function that takes another function as an argument and extends the behavior of the latter function without modifying its source code. Decorators are identified by the "@" symbol, which is followed by the name of the decorator function.

	Here's an example of how the "@" symbol is used in Python syntax to create a decorator:

		def my_decorator(func):
		    def wrapper():
		        print("Something is happening before the function is called.")
		        func()
		        print("Something is happening after the function is called.")
		    return wrapper

		@my_decorator
		def say_hello():
		    print("Hello!")

		say_hello()

	In the code above, we defined a decorator function called my_decorator that takes a function func as an argument and returns a new function called wrapper. The wrapper function is then used to wrap the original say_hello function by applying the @my_decorator decorator to it.

	When the say_hello function is called, it is actually the wrapper function that is executed, which adds some extra behavior before and after the original function call.

# Aula 2 (...)

# Aula 3

UML (unified modeling language) - há vários tipos de diagramas UML. Nós estudaremos somente os diagramas de classe.

## Acoplamento

É o nível de dependência entre classes. Queremos sempre o mínimo de acoplamento possível.

	Nível crescente de acoplamento:
	1 Dependência
	2 Associação
	3 Agregação
	4 Composição
	5 Generalização

## Relações

* Dependência: há uma dependência não permanente entre as classes. As classes não têm nenhum atributo que consista em um objeto da outra. É a relação mais fraca (menos acoplada): é uma necessidade de simples utilização. Pe: utilizo um objeto de outra classe como argumento para a execução de um método.

* Associação: uma classe TEM um atributo que é um objeto da outra (ou um array de objetos). Esse objeto desempenha um papel na classe que o contém (role). Ex.: classe professor que tem um objeto aluno como orientando (rolename = orientando --> é o nome que esse objeto tem, em virtude de sua função, para a classe professor).

* Agregação: é uma relação mais forte que a associação. É uma relação de todo/parte. Não faz sentido pensar em um time de futebol (todo) sem um jogador (parte). Uma classe é um todo e a outra é uma parte desse todo (time/jogadores; clube/membros). Quando um time acaba eles ainda existem e podem ser jogadores de outros times (os objetos são compartilhados) - esse detalhe diferencia a agregação da composição. Do mesmo modo, um jogador do Havaí também pode ser jogador da seleção brasileira (ele existe fora do clube original, como jogador).

* Composição: também é uma relação de parte/todo, só que mais intensa. A parte é totalmente dependente e só existe no contexto do todo. Uma determinada página X só pertence a um único livro Y! Se ateio fogo em um livro, as páginas também queimam. A partes são criadas e destruídas a partir do todo.

* Generalização: herança (de atributos e métodos). Serve para que evitemos a replicação de código. Animal é uma superclasse, cão e gato são subclasses; logo animal é uma generalização de cão e gato.

Note que agregação e composição são especializações de uma **associação**.

Uma das razões pelas quais criamos classes é justamente para evitar problemas quando da operação do software pelo usuário. O sistema dos postos de saúde, por exemplo, permitia que os nomes das vacinas fossem digitados - ou seja, utilizavam-se quaisquer entradas em string. Os nomes das vacinas foram escritos dos modos mais criativos possíveis, o que, obviamente, gerou uma série de problemas. Nessas circunstâncias, o ideal seria cria uma classe para a vacina pfizer, por exemplo, e somente instanciá-la, fazendo com que o usuário fique adstrito a clicar no tipo de vacina (gerando um objeto). O mesmo vale para outros campos.

Outro critério interessante para criar classes é saber quais buscas serão geralmente efetivadas pelo sistemas. Ajuda a separar as classes.

	OBS: quando o nome de um atributo está no plural, teremos um array.

	OBS2: em orientação a objetos, a referência a um objeto de outra classe nunca é feito por ID (como, por exemplo, em bancos de dados). Fazemos isso apontando para o próprio objeto, usando um atributo que contenha a sua referência na memória (ex.: um array).

Em Python, quando atribuo um objeto a uma variável (ou atributo), ela recebe uma REFERÊNCIA ao endereço de memória desse objeto.

	OBS: usar a checagem isinstance(obj,class) daqui pra frente. Haverá um decréscimo na nota caso não haja verificação de tipo.

Quando tenho indicadores de multiplicidade ("*", 0..*, 1..*, 0..1, 1, 2..4 ...) em que o primeiro dígito não seja nulo ou * - como, por exemplo, 1..* ou 1 - o construtor tem de, obrigatoriamente, passar um objeto.


	class Pessoa():
		def __init__(self, nome : str, rua : str, numero : str, cep : str):
			self.__nome = nome
			self.__enderecos = [Endereco(rua, numero, cep)]
		@property
		def nome(self):
			return self.__nome
		@property
		def enderecos(self):
			return self.__enderecos
		def add_endereco(endereco):
			if isinstanceof(endereco, Endereco):
				self.__enderecos.append(endereco)

	class Endereco():
		def __init__(self, rua : str, numero : str, cep : str):
			self.__rua = rua
			self.__numero = numero
			self.__cep = cep
			@property
			def rua(self):
				return self.__rua
			@rua.setter
			def rua(self, rua):
				self.rua = rua
			@property
			def numero(self):
				return self.numero
			@numero.setter
			def numero(self, numero):
				self.__numero = numero
			@property
			def __cep(self):
				return self.__cep
			@__cep.setter
			def __cep(self, __cep):
				self.__cep = __cep

	class Aluno(Pessoa):
		def __init__(self, nome, rua, numero, cep):
			super().__init__(self, nome, rua, numero, cep)

	class Professor(Pessoa):
		def __init__(self, nome, rua, numero, cep, orientando):
			if isistanceof(orientando, Aluno):
				self.__orientando = orientando
			super().__init__(self, nome, rua, numero, cep)
		@property
		def orientando(self):
			return self.__orientando
		@orientando.setter
		def orientando(self, orientando):
			if isinstanceof(orientando, Aluno):
				self.__orientando = orientando
			else:
				raise Exception("Atributo orientando aceita somente objetos da classe Aluno")


Quando faço uma composição, eu crio/instancio o objeto da classe parte dentro da minha própria classe todo. Se o objeto-parte é obrigatório para o objeto-todo (e é), o construtor tem que prever a criação do atributo que receba esse objeto-parte.
Esse objeto-parte seria parte integrante e exclusiva do objeto-todo.

Henraça simples: a subclasse herda somente de uma classe.

Herança múltipla: a subclasse herda de mais de uma classe.

	OBS:Classe gênero e autor no trabalho 2 -> há um milhão de modos de modelar um problemas, criando infinitas classes. Mas é interessante entender que as opções devem ser orientadas tendo em mente o que vai ser feito com o sistema, como ele será utilizado pelo usuário final.

# Aula 4

Classe associativa: é uma forma de resolver uma relação many-to-many ou one-to-many. A própria associação entre duas classes é tão complexa que exige ou ao menos sugere a criação de uma classe que represente essa associação. Essa classes associativa terá objetos de ambas as classes que ela associa (ex.: objetos de cliente e conta - e a classe associativa é AssocClienteConta).

Associação qualificada: é um modo de representar um atributo que tem um dicionário, onde, no exemplo abaixo, o produto é a chave de um dicionário que contém objetos da classe ITEMPEDIDO.
________
PEDIDO  | produto --------------- > ITEMPEDIDO
---------

O produto é a chave e o ITEMPEDIDO é o valor..

Associações reflexivas: uma classe está associada a ela mesma. É uma relação entre objetos da mesma classe.uma classe tem objetos de si própria.

OBS: Quando tenho composição, significa que eu o objeto não virá pronto para a classe: ele será instanciado dentro dela. Temos que criar uma função, dentro da classe principal, que receba os argumentos necessários para instanciar e inserir dentro dela os objetos dependentes.

# Aula 5

### Classes abstratas (para garantir que não conseguiremos instanciar um objeto)

Classe abstrata: É uma classe que não terá objetos instanciados! A classe pode estar completinha, mas não poderá ser instanciada.
Ela oferece uma base abstrata para a hierarquia de classes. Interessante para o uso de polimorfismo.

No UML, indico que é uma classes abstrata tanto por {abstract} ou pelo uso de itálico. 

A classe abstrata funciona como uma interface! Eu digo o que eu preciso mas eu não implemento.

Na classe abstrata é muito comum só a previsão de um método e deixar a implementação para as classes filhas, que precisarão implementar cada uma a seu modo (para suprir as suas necessidades).

Nos métodos abstratos, colocaremos um pass dentro do corpo da função. Isso torna obrigatória a implementação do método nas classes filhas!


No Python:


from abc import ABC, abstractmethod

class Figura(ABC):

	@abstractmethod
	def __init__(self):
		pass

	@abstractmethid
	def desenhe(self):
		pass


class Circulo(Figura):

	def __init__(self, raio):
		super().__init__()
		self.__raio = raio

	@property
	def raio(self):
		return self.__raio

	@raio.setter
	def raio
	...

	def desenhe(self):  +========> a implementação dessa aqui é obrigatória em função da utilização de @abstractmethod lá em cima


Por que fica uma interface? Porque as classes filhas precisam implementar o método com a mesma ASSINATURA DE MÉTODO (mesmo nome do método/função e os mesmos parâmetros).

LEMBRE: assinatura de método ===>    NOME DA FUNÇÃO + PARÂMETROS


O nome disso é polimorfismo. A possibilidade de que algo assuma diversas formas.

BAIXAR E ANALISAR A IMPLEMENTAÇÃO DE MOSTRA_DADOS EM DEPENDENTES! 


OBS: é possível implementar parte ao menos de um método abstrato -> e aí eu chamo essa implementação nas filhas usando super()
OBS: é possível também implementar totalmente a classe original (e aí o @abstractmethod serve como um jeito de forças as classes a implementar --- lembrando que eu teria que chamar a funcionalidade colocando um super() dentro do método da classe filha)

Dica do exercício: retornar pedaços da string para as classes concretas (castatinha) - não usaremos pass, iremos implementar algumas funcionalidades que vão se incrementando e se somando ao longo das passagens para as funções de baixo. Um monte de return, formatar a string e printar.

