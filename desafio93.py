import datetime
data = datetime.datetime.now()
ano = data.year
a = {}
a["nome"] = str(input('Nome: ')).capitalize()
a["idade"] = ano - int(input('Ano de nascimento: '))
a["ctps"] = int(input('Número da carteira de trabalho: (0 caso não tenha) '))
if a["ctps"] != 0:
    a["ano"] = int(input('Ano de contratação: '))
    a["salario"] = float(input('Valor do salário: '))
    a["apo"] = (35 - (ano - a["ano"])) + a["idade"]
print('-'*50)
print(f'O nome da(o) usuária(o) é: {a["nome"]}')
print(f'Sua idade é de: {a["idade"]}')
print(f'O ctps é de: {a["ctps"]}')
if a["ctps"] != 0:
    print(f'O ano de contratação é de {a["ano"]}')
    print(f'O salário é de: {a["salario"]:.2f}')
    print(f'{a["nome"]} vai se aposentar com {a["apo"]}')
print('-'*50)
