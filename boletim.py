class Boletim:

    def calcular_media(self, notas):
        if len(notas) == 0:
            return 0
        return sum(notas) / len(notas)

    def situacao(self, media):
        if media >= 7:
            return 'aprovado'
        elif media >= 5:
            return 'recuperação'
        else:
            return 'reprovado'

    def mostrar_boletim(self, aluno):
        print(f'\nBoletim do aluno: {aluno.nome}')

        for materia, notas in aluno.notas.items():
            media = self.calcular_media(notas)
            situacao = self.situacao(media)

            print(f'\nMatéria: {materia}')
            print(f'Notas: {notas}')
            print(f'Média: {media:.2f}')
            print(f'Situação: {situacao}')
