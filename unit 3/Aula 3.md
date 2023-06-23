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

