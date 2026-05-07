# ATIVIDADE PROPOSTA:
# Você foi contratado para desenvolver um sistema simples de gestão de notas de alunos. O sistema
# deve permitir que o usuário adicione notas, calcule a média das notas, determine a situação do
# aluno (aprovado ou reprovado), e exiba um relatório final. Utilize estruturas condicionais, de
# repetição e funções.
# Cadastro de Notas:
# • O sistema deve permitir que o usuário insira as notas dos alunos.
# • As notas devem ser armazenadas em uma lista.
# Cálculo da Média:
# • O sistema deve calcular a média das notas inseridas.
# Determinação da Situação:
# • Se a média for maior ou igual a 7, o aluno está aprovado.
# • Se a média for menor que 7, o aluno está reprovado.
# Relatório Final:
# Exibir as notas inseridas, a média e a situação do aluno.

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.notas = []

    def adicionar_nota(self, nota):
        if nota < 0 or nota > 10:
            raise ValueError('Nota deve ser entre 0 e 10')
        self.notas.append(nota)

    def calcular_media(self):
        if not self.notas:
            return 0
        return sum(self.notas) / len(self.notas)

    def situacao(self):
        media = self.calcular_media()
        if media >= 7:
            return "o aluno esta aprovado"
        else:
            return "o aluno esta reprovado"

    def relatorio(self):
        print(f'Aluno: {self.nome}')
        print()
        print(f'Notas: {self.notas}')
        print()
        print(f'Média: {self.calcular_media():.2f}')
        print()
        print(f'Situação: {self.situacao()}')


nome = input('digite seu nome:')
aluno = Aluno(nome)


while True:
    try:
        quantidade = int(input('digite a quantidade de notas: '))
        if quantidade <= 0:
            print('A quantidade deve ser maior que zero')
            continue
        break
    except ValueError:
        print('valor invalido digite numeros inteiros')

for i in range(quantidade):
    while True:
        try:
            nota = float(input(f"Digite a {i+1}ª nota: "))

            aluno.adicionar_nota(nota)

            break

        except ValueError as erro:
            print(f"Erro: {erro}")

aluno.relatorio()
