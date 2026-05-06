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




aluno = Aluno("Léo")
print(f'Aluno: {aluno.nome}')

try:
    aluno.adicionar_nota(8)
    aluno.adicionar_nota(7.8)
    aluno.adicionar_nota(10) 

except ValueError as e:
    print(f'Erro capturado: {e}')


print(f'Notas: {aluno.notas}')
print(f'Média: {aluno.calcular_media():.2f}')
print(f'Situação: {aluno.situacao()}')