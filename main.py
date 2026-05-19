import os
from pessoa import Pessoa
from materia import Materia
from professor import Professor
from aluno import Aluno
from boletim import Boletim


alunos = []
professores = []
materias = []
boletim = Boletim()


def limpar():
    os.system('cls')


def menu():
    limpar()
    print('\n    SISTEMA DE NOTAS      ')
    print('1 - Cadastrar materia')
    print('2 - Cadastrar aluno')
    print('3 - Cadastrar professor')
    print('4 - Lançar nota')
    print('5 - Ver boletim')
    print('6 - Aumentar salario')
    print('7 - Listar alunos')
    print('8 - Listar professores')
    print('9 - Dados do professor')
    print('0 - Sair')
    return input('\n Escolha uma opção: ')


def cadastrar_materia():
    limpar()
    nome = input('Nome da materia: ')
    print('Periodos: manha, tarde, noite')
    periodo = input('Periodo: ')
    try:
        m = Materia(nome, periodo)
        materias.append(m)
        print(f'Materia {nome} cadastrada')
    except ValueError as e:
        print(f'Erro: {e}')
    input('\nPrecione Enter para continuar')


def cadastrar_aluno():
    limpar()
    nome = input('Nome do aluno: ')
    endereco = input('Endereço: ')
    a = Aluno(nome, endereco)
    alunos.append(a)
    print(f'Aluno {nome} cadastrado')
    input('\nPrecione Enter para continuar')


def cadastrar_professor():
    limpar()
    nome = input('Nome do professor: ')
    endereco = input('Endereço: ')
    try:
        salario = float(input('Salario: '))
        if not materias:
            print('cadastre uma materia primeiro')
            return
        for i, m in enumerate(materias):
            print(f'{i} - {m.nome}')
        idx = int(input('Escolha a materia: '))
        p = Professor(nome, endereco, salario, [materias[idx]])
        professores.append(p)
        print(f'Professor {nome} cadastrado ')
    except (ValueError, TypeError, IndexError) as e:
        print(f'Erro: {e}')
    input('\nPrecione Enter para continuar')


def aumentar_salario():
    limpar()
    if not professores:
        print('Nenhum professor cadastrado')
        return
    for i, p in enumerate(professores):
        print(f'{i} - {p.nome}')
    idx = int(input('Escolha o professor: '))
    try:
        valor = float(input('Valor do aumento: '))
        professores[idx].aumentar_salario(valor)
    except (ValueError, IndexError) as e:
        print(f'Erro: {e}')
    input('\nPrecione Enter para continuar')


def escolher(lista, tipo):
    if not lista:
        print(f'Nenhuma(a) {tipo} cadastrado')
        return None
    for i, item in enumerate(lista):
        print(f'{i} - {item.nome}')
    try:
        idx = int(input(f'Escolha o {tipo}: '))
        if idx < 0 or idx >= len(lista):
            print('Opção invalida')
            return None
        return lista[idx]
    except ValueError:
        print('Digite apenas numeros')
        return None


def listar_alunos():
    limpar()
    if not alunos:
        print('Nenhum aluno cadastrado')
        input('\nPrecione Enter para continuar')
        return
    print('\nAlunos')
    for a in sorted(alunos, key=lambda a: a.nome):
        print(f'- {a.nome}')
    input('\nPrecione Enter para continuar')


def listar_professores():
    limpar()
    if not professores:
        print('Nenhum professor cadastrado')
        input('\nPrecione Enter para continuar')
        return
    print('\nProfessores')
    for p in sorted(professores, key=lambda p: p.nome):
        print(f'- {p.nome}')
    input('\nPrecione Enter para continuar')

def ver_dados_professor():
    limpar()
    professor = escolher(professores, 'professor')
    if professor is None:
        return 
    limpar()
    print('\nDados do professor')
    print(f'Nome: {professor.nome}')
    print(f'Endereço: {professor.endereco}')
    professor.mostrar_salario()
    print(f'\nMaterias: ')
    professor.mostrar_materias()
    input('\nPrecione Enter para continuar')

def lancar_nota():
    limpar()
    aluno = escolher(alunos, 'aluno')
    if aluno is None:
        return
    professor = escolher(professores, 'professor')
    if professor is None:
        return
    materia = escolher(professor.materias, 'materia')
    if materia is None:
        return
    try:
        entrada = input('Notas separadas por espaço: ')
        notas = [float(n) for n in entrada.split()]
        professor.lancar_nota(aluno, materia, *notas)
        print('Notas lançadas')
    except ValueError as e:
        print(f'Erro: {e}')
    input('\nPrecione Enter para continuar')


def ver_boletim():
    if not alunos:
        print('Nenhum aluno cadastrado')
        return
    for i, a in enumerate(alunos):
        print(f'{i} - {a.nome}')
    idx = int(input('Escola o aluno: '))
    boletim.mostrar_boletim(alunos[idx])
    input('\nPrecione Enter para continuar')


while True:
    opcao = menu()
    if opcao == '1':
        cadastrar_materia()
    elif opcao == '2':
        cadastrar_aluno()
    elif opcao == '3':
        cadastrar_professor()
    elif opcao == '4':
        lancar_nota()
    elif opcao == '5':
        ver_boletim()
    elif opcao == '6':
        aumentar_salario()
    elif opcao == '7':
        listar_alunos()
    elif opcao == '8':
        listar_professores()
    elif opcao == '9':
        ver_dados_professor()
    elif opcao == '0':
        print('Saindo')
        break
    else:
        print('Opção invalida')
