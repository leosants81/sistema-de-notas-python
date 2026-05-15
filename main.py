from pessoa import Pessoa
from materia import Materia
from professor import Professor
from aluno import Aluno
from boletim import Boletim


if __name__ == '__main__':

    # materias
    matematica_manha = Materia('Matematica', 'manha')
    matematica_tarde = Materia('Matematica', 'tarde')
    matematica_noite = Materia('Matematica', 'noite')
    geografia_manha = Materia('Geografia', 'manha')
    geografia_tarde = Materia('Geografia', 'tarde')
    geografia_noite = Materia('Geografia', 'noite')
    ciencias_manha = Materia('Ciências', 'manha')
    ciencias_tarde = Materia('Ciências', 'tarde')
    sociologia_noite = Materia('Sociologia', 'noite')
    historia_noite = Materia('História', 'noite')
    artes_manha = Materia('Artes', 'manha')

    # professores

    prof_alex = Professor('Alex', 'Rua B', 7000, [
                          matematica_manha, ciencias_tarde])
    prof_marcelo = Professor('Marcelo', 'Rua A', 7000, [
                             geografia_manha, sociologia_noite])
    prof_cristina = Professor('Cristina', 'Rua C', 3500, [historia_noite])

    prof_cristina.adicionar_materia(artes_manha)

    print('=====Professores======')
    prof_cristina.dados()
    prof_cristina.mostrar_materias()
    prof_cristina.mostrar_salario()
    prof_cristina.aumentar_salario(3500.50)

    print()

    prof_alex.dados()
    prof_alex.mostrar_materias()
    prof_alex.mostrar_salario()

    # Alunos 
    aluno_1 = Aluno('Maria', 'Rua Antonia')
    aluno_2 = Aluno('Leo', 'Rua C')
    aluno_3 = Aluno('Lais', 'Rua C')

    # lançar notas 
    prof_alex.lancar_nota(aluno_1, matematica_manha, 8, 7, 8, 5)
    prof_cristina.lancar_nota(aluno_2, historia_noite, 8, 6, 7, 7)
    prof_marcelo.lancar_nota(aluno_3, sociologia_noite, 5, 6, 7, 5)

    # Boletim 
    boletim = Boletim()
    boletim.mostrar_boletim(aluno_1)
    boletim.mostrar_boletim(aluno_2)
    boletim.mostrar_boletim(aluno_3)
