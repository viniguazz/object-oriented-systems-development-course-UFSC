from aluno_posgraduacao import AlunoPosGraduacao
from administrativo import Administrativo
from professor import Professor


aluno1 = AlunoPosGraduacao(50, 20, 22200520)
print(aluno1.dias_de_emprestimo)
print(aluno1.cpf)
print(aluno1.matricula)
print(aluno1.elaborando_tese)
print(aluno1.emprestar('o nome da rosa'))
print(aluno1.devolver('o nome da rosa'))

professor1 = Professor('INE', 3030)
print(professor1.dias_de_emprestimo)
print(professor1.cpf)
print(professor1.departamento)
print(professor1.emprestar('o nome da rosa'))
print(professor1.devolver('o nome da rosa'))

administrativo1 = Administrativo('CCE', 220)
print(administrativo1.dias_de_emprestimo)
print(administrativo1.cpf)
print(administrativo1.departamento)
print(administrativo1.emprestar('o nome da rosa'))
print(administrativo1.devolver('o nome da rosa'))