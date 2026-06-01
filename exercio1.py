frutas = ['maçã', 'banana', 'laranja', 'uva', 'melancia']
numeros = [5, 12, 18, 25, 30, 8, 42, 15, 3, 21]

print(frutas[0])
print(frutas[4])
print(frutas[0])
print(frutas[-1])

frutas.append('morango')
frutas.insert(2, 'kiwi')

frutas.remove('banana')

for n in numeros:
    if n > 15:
        print(n)

numeros.sort()
print(numeros)

numeros.sort(reverse=True)
print(numeros)
