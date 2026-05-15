class Materia():
    PERIODOS = ['manha', 'tarde', 'noite']

    def __init__(self, nome, periodo):
        if periodo not in self.PERIODOS:
            raise ValueError(f'periodo deve ser: {self.PERIODOS}')
        self.nome = nome 
        self.periodo = periodo
        