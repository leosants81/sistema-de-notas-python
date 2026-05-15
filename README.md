# Sistema de Gestão de Notas 📚

Sistema escolar desenvolvido em Python com Programação Orientada a Objetos,
permitindo cadastrar professores,
alunos e matérias, lançar notas e gerar boletins.

## Estrutura do Projeto


sistema_de_notas/
├── pessoa.py       # Classe base
├── professor.py    # Gerencia matérias e notas
├── aluno.py        # Armazena notas por matéria
├── materia.py      # Nome e período da matéria
├── boletim.py      # Calcula média e situação
└── main.py         # Arquivo principal


## Como Rodar

bash
python main.py


## Exemplo de Saída


Boletim do aluno: Leo
Matéria: Matematica
Notas: [8, 7, 9]
Média: 8.00
Situação: aprovado


## Tecnologias
- Python 3.x
- Herança, encapsulamento e validações