from time import sleep
lista = []
a = {}
while True:
    a["nome"] = str(input('Nome: ').capitalize())
    a["media"] = float(input(f'Média de {a["nome"]}: ')) 
    lista.append(a.copy())
    a.clear()
    esc = str(input('Quer continuar? [S/N] ')).upper()[0]
    while esc != 'N' and esc != 'S':
        esc = str(input('Por favor digite S ou N ')).upper()[0]
    if esc =='N':
        break
print(lista)
for c in range(0, len(lista)):
    print('-'*30)
    print(f'O nome do aluno(a): {lista[c]["nome"]}')
    print(f'Sua média foi: {lista[c]["media"]}')
    if lista[c]["media"] >= 7:
        print('Sua situação é: aprovada(o).')
    else:
        print('Sua situação é: reprovado(a).')
    print('-'*30)
    sleep(2)
print('-'*30)
print('Finalizando programa.')
print('-'*30)
sleep(1)
print('Fim')