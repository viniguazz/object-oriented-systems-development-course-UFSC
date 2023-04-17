from controladorChamados import ControladorChamados
from controladorPessoas import ControladorPessoas
from datetime import date as Date

# instancia os controladores
conChamados = ControladorChamados()
conPessoas = ControladorPessoas()

# testa a criação de clientes e técnicos
print('tentativa 1', conPessoas.inclui_cliente(1, 'vinicius'))
print('tentativa 2', conPessoas.inclui_cliente(1, 'Paulo Garrido'))
print('tentativa 3', conPessoas.inclui_cliente(2, 'Lucas'))

print('tentativa 1', conPessoas.inclui_tecnico(1, 'Adilson'))
print('tentativa 2', conPessoas.inclui_tecnico(1, 'Jorge'))
print('tentativa3', conPessoas.inclui_tecnico(1, 'Jamanta'))

print(f'clientes: {conPessoas.clientes}')
print(f'tecnicos: {conPessoas.tecnicos}')
print(f'clientes vars: {vars(conPessoas.clientes[0])}')

for _ in conPessoas.clientes:
    print(_.codigo)
    print(_.nome)

for _ in conPessoas.tecnicos:
    print(_.codigo)
    print(_.nome)

# testa a criação de tipos de chamado
print('tentativa 1', conChamados.inclui_tipochamado(1, 'Instalação elétrica', 'Instalação de equipamentos elétricos em geral'))
print('tentativa 2', conChamados.inclui_tipochamado(1, 'Encanamento', 'Reparo de sistemas hídricos'))
print('tentativa 3', conChamados.inclui_tipochamado(2, 'Gato', 'Instalação de unidade de fornecimento de energia gratuita'))

# teste do método tipo_chamados
print(f'tipos de chamados: {conChamados.tipos_chamados}')

for _ in conChamados.tipos_chamados:
    print(_.codigo)
    print(_.nome)
    print(_.descricao)

# testa a criação de chamados
date_obj = Date(2023, 4, 17)
print('tentativa 1', conChamados.inclui_chamado(date_obj, conPessoas.clientes[0], conPessoas.tecnicos[0], 'Energia cortada', 'O cliente busca uma solução para a energia cortada', 3, conChamados.tipos_chamados[1]))
print('tentativa 2', conChamados.inclui_chamado(date_obj, conPessoas.clientes[1], conPessoas.tecnicos[0], 'Resistência de chuveiro', 'Socorro', 2, conChamados.tipos_chamados[0]))
print('tentativa 3', conChamados.inclui_chamado(date_obj, conPessoas.clientes[0], conPessoas.tecnicos[0], 'Energia cortada', 'O cliente busca uma solução para a energia cortada', 3, conChamados.tipos_chamados[1]))
print('tentativa 4', conChamados.inclui_chamado(date_obj, conPessoas.clientes[1], conPessoas.clientes[1], 'Energia cortada', 'O cliente busca uma solução para a energia cortada', 3, conChamados.tipos_chamados[1]))


print(f'lista de chamados: {conChamados._ControladorChamados__chamados}')
print(f'lista de tipos: {conChamados._ControladorChamados__tipos_de_chamados}')
print(f'lista de chamados do tipo 1: {conChamados.total_chamados_por_tipo(conChamados.tipos_chamados[0])}')
print(f'lista de chamados do tipo 2: {conChamados.total_chamados_por_tipo(conChamados.tipos_chamados[1])}')

