from pessoa import Pessoa
from materia import Materia


class Professor(Pessoa):
    def __init__(self, nome, endereco, salario, materias):
        super().__init__(nome, endereco)

        self.materias = materias

        if not isinstance(salario, (int, float)):
            raise TypeError('Salario deve ser numérico')

        if salario <= 0:
            raise ValueError('Salario deve ser maior que zero')

        self.__salario = salario

    def adicionar_materia(self, materia):
        self.materias.append(materia)

    def aumentar_salario(self, valor_por_materia):
        self.__salario += valor_por_materia
        print(f'Novo salario: {self.__salario:.2f}')

    def lancar_nota(self, aluno, materia, *nota):

        if materia.nome not in [m.nome for m in self.materias]:
            raise ValueError('Professor não ensina essa matéria')

        aluno.adicionar_nota(materia, *nota)

    def mostrar_materias(self):
        ordem = ['manha', 'tarde', 'noite']
        ordenadas = sorted(self.materias, key=lambda m: ordem.index(m.periodo))
        for materia in ordenadas:
            print(f'{materia.nome} - {materia.periodo}')

    def mostrar_salario(self):
        print(f'Salario: R$ {self.__salario:.2f}')

    def dados(self):
        print(f'Professor: {self.nome}')
        print(f'Endereço: {self.endereco}')


if __name__ == '__main__':

    materia_1 = Materia('matematica', 'manha')
    materia_2 = Materia('geografia', 'tarde')

    p1 = Professor('alex', 'rua b', 3500, [materia_1])
    p1.adicionar_materia((materia_2))
    p1.mostrar_materias()
    p1.mudar_endereco('rua antonia boschett')
    p1.dados()
    p1.mostrar_salario()

    materia_3 = Materia('sociologia', 'noite')
    p2 = Professor('marcelo', 'rua A', 3000, [materia_2])
    p2.mostrar_materias()
    p2.mudar_endereco('rua C')
    p2.dados()
    p2.mostrar_salario()
