# Ordene os alunos pelas seguintes regras:
# maior nota primeiro;
# em caso de empate, nome em ordem alfabética.

alunos = [
    ("Arthur", 8.5),
    ("Lucas", 7.0),
    ("Ana", 8.5),
    ("Bruno", 9.0),
    ("Carla", 7.0)
]

alunos.sort(key=lambda aluno: (-aluno[1], aluno[0]))
print(alunos)