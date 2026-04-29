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

def inserir_notas():
    notas = []
    quantidade = int(input('digite a quantidade de notas: '))
    for i in range(quantidade):
        nota = float(input(f'Digite a {i+1}ª nota: '))
        notas.append(nota)
    return notas 
    
def calcular_media(notas):
    return sum(notas) / len(notas)


def verificar(media):
    if media >= 7:
        return 'o aluno esta aprovado'
    else:
        return 'o aluno esta reprovado'


def relatorio(notas, media, situacao):
    print('notas inseridas: ',notas)
    print('media do aluno: ', media)
    print('situação do aluno: ', situacao)


notas_do_aluno = inserir_notas()
media_do_aluno = calcular_media(notas_do_aluno)
verificar_media = verificar(media_do_aluno)
relatorio_do_aluno = relatorio(notas_do_aluno, media_do_aluno, verificar_media)


# Erro corrigido na primeira função return dentro do for linha 23 
# a função encerrava na primeira repetição 
# função verificar os return estava como print o relatorio aparecia None 