notas = [7.5, 8.0, 6.0, 9.5, 5.5, 8.5, 7.0, 9.0, 6.5, 8.0]

soma = sum(notas)
quantidade = len(notas)
media = soma / quantidade
print(media)

maior = max(notas)
menor = min(notas)
print(maior)
print(menor)

contagem_acima = 0
for n in notas:
    if n > media:
        contagem_acima = contagem_acima + 1
print(contagem_acima)

nomes = ['Carlos', 'Ana', 'Bruno', 'Ana', 'Diego', 'Ana', 'Bruno']
print(nomes.count('Ana'))
print(nomes.index('Bruno'))

unicos = []
for nome in nomes:
    if nome not in unicos:
        unicos.append(nome)
print(unicos)
