notas_turma = []
media = 0
cont = 0
for i in range (1,21):
    notas = int(input("digite a sua nota: "))
    notas_turma.append(notas)
    media = sum(notas_turma) / 20
    if notas >= media:
        cont +=1
print(media, cont)
