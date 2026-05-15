from pessoa import Pessoa
from materia import Materia


class Aluno(Pessoa):
    def __init__(self, nome, endereco):
        super().__init__(nome, endereco)
        self.notas = {}

    def adicionar_nota(self, materia, *notas):

        if not notas:
            raise ValueError('informe ao menos uma nota')

        if materia.nome not in self.notas:
            self.notas[materia.nome] = []

        for nota in notas:

            if nota < 0 or nota > 10:
                raise ValueError('Nota deve ser entre 0 e 10')

            self.notas[materia.nome].append(nota)


if __name__ == '__main__':

    materia_1 = Materia('Matematica', 'manha')

    a1 = Aluno('leo', 'rua antonia')

    a1.mudar_endereco('rua luiz stamatis')

    a1.adicionar_nota(materia_1, 10, 8, 9, 5)

    print(a1.nome)
    print(a1.notas)
    print(a1.endereco)
