from time import sleep
lista = []
a = {}
cont = 1
while True:
  soma = 0
  a["gols"] = []
  a["nome"] = str(input('Nome do jogador: ')).capitalize()
  a["part"] = int(input(f'Quantas partidas {a["nome"]} jogou? '))
  for b in range(0, a["part"]):
      g = int(input(f'Quantos gols na partida {cont}? '))
      soma = soma + g
      a["gols"].append(g)
      cont = cont + 1
  a["soma"] = soma
  lista.append(a.copy())
  a.clear()
  cont = 1
  esc = str(input('Você quer adicionar mais um jogador? [S/N] ')).upper()[0]
  while esc != 'S' and esc != 'N':
    esc = str(input('Por favor use S para sim e N para não ')).upper()[0]
  if esc == 'N':
    break
cont = 1
print('-'*60)
print('cod'.ljust(5), end = '') 
print('nome'.ljust(5),end = '')
print('gols'.rjust(25), end = '')
print(' '*15, end = '')
print('total', end = '')
print()
print('-'*60)
for c in range(0, len(lista)):
    print(f'{c}'.ljust(5), end = '')
    print(f'{lista[c]["nome"]}'.ljust(5),end = '')
    print(f'{lista[c]["gols"]}'.rjust(35-(len(lista[c]["nome"])+5)), end = '')
    print(' '*15, end = '')
    print(f'{lista[c]["soma"]}', end = '')
    print()
print('-'*60)
while True:
    cont = 1
    num = int(input('Mostrar dados de qual jogador? (999 interrompe) '))
    if num == 999:
        break
    while num >= len(lista):
        num = int(input(f'ERRO. Não existe jogador número {num}. Tente novamente '))
        print('-'*60)
    print(f'Levantando dados do jogador {lista[num]["nome"]}.')
    sleep(1)
    for d in range(0, len(lista[num]["gols"])):
        print(f'Na partida {cont}, fez {lista[num]["gols"][d]} gols.')
        cont = cont +1
    print('-'*60)
print('-'*60)
print('FIM')
