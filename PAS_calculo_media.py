quantidade_alunos:int
i:int
j:int
media:float
media_turma:float
soma:float
posicao:int
maior:float
menor:float

quantidade_alunos = int(input("Digite a quantidade de alunos (minimo 2/maximo 7): "))

while (quantidade_alunos < 2) or (quantidade_alunos > 7):
    quantidade_alunos = int (input("Digite a quantidade correta de alunos: "))


mat_notas1: [[float]] = [[0 for x in range(quantidade_alunos)]for x in range (1)]
mat_notas2: [[float]] = [[0 for x in range(quantidade_alunos)]for x in range (1)]
mat_alunos: [[str]] = [[0 for x in range(quantidade_alunos)]for x in range (1)]
mat_media: [[float]] = [[0 for x in range(quantidade_alunos)]for x in range (1)]

for i in range (0,1):
    for j in range (0,quantidade_alunos):
        mat_alunos[i][j] = str(input(f"Digite o nome do(a) {j+1}º aluno(a): "))
        mat_notas1[i][j] = float (input(f"Digite a primeira nota do(a) aluno(a) {mat_alunos [i][j]}: "))
        while (mat_notas1[i][j] < 0) or (mat_notas1[i][j] > 10):
            mat_notas1[i][j] = float(input("Digite a nota correta: "))
        mat_notas2[i][j] = float(input(f"Digite a segunda nota do(a) aluno(a) {mat_alunos [i][j]}: "))
        while (mat_notas2[i][j] < 0) or (mat_notas2[i][j] > 10):
            mat_notas2[i][j] = float(input("Digite a nota correta: "))
        media = (mat_notas1[i][j] + mat_notas2[i][j])/2
        mat_media[i][j] = media
        print()

for i in range (0,1):
    for j in range (0,quantidade_alunos):
        print (f"Aluno: {mat_alunos[i][j]}")
        print(f"Nota 1: {mat_notas1[i][j]:.1f}")
        print(f"Nota 2: {mat_notas2[i][j]:.1f}")
        print(f"Media: {mat_media[i][j]:.1f}")
        print()

soma = 0
for i in range (0,1):
    for j in range (0,quantidade_alunos):
        soma = soma + mat_media[i][j]
media_turma = soma/quantidade_alunos
print (f"MEDIA DA TURMA = {media_turma:.2f}")
print (f"A TURMA TEM {quantidade_alunos} ALUNOS")

posicao = 0
maior = mat_media[0][0]
for i in range (0,1):
    for j in range (0,quantidade_alunos):
        if mat_media[i][j] > maior:
            maior = mat_media[i][j]
            posicao = j
print(f"O(a) ALUNO(a) QUE OBTEVE A MAIOR MEDIA FOI {mat_alunos[i][posicao]} COM {maior:.2f} PONTOS")

posicao = 0
menor = mat_media[0][0]
for i in range (0,1):
    for j in range (0,quantidade_alunos):
        if mat_media[i][j] < menor:
            menor = mat_media[i][j]
            posicao = j
print(f"O(a) ALUNO(a) QUE OBTEVE A MENOR MEDIA FOI {mat_alunos[i][posicao]} COM {menor:.2f} PONTOS")




