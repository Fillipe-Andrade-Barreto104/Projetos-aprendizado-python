def area(l,c):
    a = l * c
    print(f'A área do terreno informado é {a:.2f} m².')

while True:
    L = float(input('Por favor digite a lagura (em m) da área que deseja calcular: '))
    C = float(input('Por favor digite o comprimento (em m) da área que deseja calcular: '))
    area(l = L, c = C)
    esc = str(input('Você deseja calcular mais alguma área [S/N] ')).upper()[0]
    while esc != 'S' and esc != 'N':
        esc = str(input('Por favor digite S para sim e N para não. ')).upper()[0]
    if esc == 'N':
        break
print('FIM')
