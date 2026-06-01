turma = [
    ['Alice', 8.0, 7.5, 9.0],
    ['Bruno', 6.5, 7.0, 8.0],
    ['Carla', 9.5, 9.0, 9.5],
    ['Diego', 5.0, 6.0, 5.5],
    ['Elena', 7.0, 8.5, 7.5],
]

lista_medias = []

for aluno in turma:
    nome = aluno[0]
    nota1 = aluno[1]
    nota2 = aluno[2]
    nota3 = aluno[3]
    media = (nota1 + nota2 + nota3) / 3
    print(nome)
    print(media)
    lista_medias.append([nome, media])

maior_media = 0
melhor_aluno = ""
for item in lista_medias:
    if item[1] > maior_media:
        maior_media = item[1]
        melhor_aluno = item[0]
print(melhor_aluno)

for item in lista_medias:
    if item[1] >= 6.0:
        print("Aprovado:", item[0])
    else:
        print("Reprovado:", item[0])

soma_total = 0
for item in lista_medias:
    soma_total = soma_total + item[1]
media_geral = soma_total / len(lista_medias)
print(media_geral)

turma.append(['Felipe', 8.0, 7.5, 8.5])
