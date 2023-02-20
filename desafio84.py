lista = []
conta = 0
contf = 0
exp = str(input('Digite uma expressão com parenteses '))
lista = list(exp)
for c in range(0,len(lista)):
    if lista[c] == '(':
        conta = conta + 1
    if lista[c] == ')':
        contf = contf + 1
if conta == contf:
    print('Sua expressão é valida.')
if conta != contf:
    print('Sua expressão está errada.')
