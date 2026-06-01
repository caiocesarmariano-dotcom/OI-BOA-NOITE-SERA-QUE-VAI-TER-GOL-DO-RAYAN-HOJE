quadrados = []
for x in range(1, 11):
    quadrados.append(x * x)
print(quadrados)

numeros = list(range(1, 21))
pares = []
for n in numeros:
    if n % 2 == 0:
        pares.append(n)
print(pares)

palavras = ['python', 'lista', 'programação', 'código', 'loop', 'função']
tamanhos = []
for p in palavras:
    tamanhos.append(len(p))
print(tamanhos)

longas = []
for p in palavras:
    if len(p) > 5:
        longas.append(p.upper())
print(longas)
