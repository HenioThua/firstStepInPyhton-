nota_total = 0
alunos = int(input("Digite o número de alunos: "))
for i in range(1, alunos + 1):
    nota = float(input("digite a sua nota: "))
    nota_total += nota
media = nota_total / alunos
print("a media final da turma é {:.2f}".format(media))
