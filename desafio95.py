lista = list()
listmu = list()
listme = list()
a = {}
cont = 0
soma = 0
while True:
  a["nome"] = str(input('Nome: ')).capitalize()
  a["sexo"] = str(input('Sexo [F/M]: ')).upper()[0]
  while a["sexo"] != 'M' and a["sexo"] != 'F':
    a["sexo"] = str(input('Por favor digite F ou M ')).upper()[0]
  a["idade"] = float(input('Idade: '))
  lista.append(a.copy())
  a.clear()
  cont = cont +1
  esc = str(input('Deseja cadastrar mais uma pessoa? [S/N] ')).upper()[0]
  while esc != 'N' and esc != 'S':
    esc = str(input('Por favor digite S para sim e N para não. ')).upper()[0]
  if esc == 'N':
    break
print('-'*40)
print(f'O numero de pessoas cadastradas foi {cont}')
print('-'*60)
for b in range(0, len(lista)):
  soma = soma + lista[b]["idade"]
  media = soma/cont
  if lista[b]["sexo"] == 'F':
    listmu.append(lista[b]["nome"])

print(f'A média das idades das pessoas cadastradas foram: {media:.2f}')
print('-'*60)
if len(listmu) > 0:
    print(f'As mulheres cadastradas foram: {listmu}')
else:
    print('Nenhuma mulher foi cadastrada.')
print('-'*60)
for c in range(0, len(lista)):
    if lista[c]["idade"] > media:
        print(f'{lista[c]["nome"]} {lista[c]["sexo"]} tem idade acima da média, pois tem {lista[c]["idade"]}')
print('-'*60)