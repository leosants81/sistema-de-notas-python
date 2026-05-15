class Pessoa():
    def __init__(self, nome, endereco):
        self.nome = nome
        self.endereco = endereco

    def mudar_endereco(self, novo_endereco):
        if novo_endereco == '':
            print('endereço inválido')
            return

        self.endereco = novo_endereco

if __name__ =='__main__':
    p1 = Pessoa('leo', 'rua antonia boschett')

    print(p1.nome, p1.endereco)

    p1.mudar_endereco('rua luiz stamatis')

    print(f'Novo endereço {p1.endereco}')