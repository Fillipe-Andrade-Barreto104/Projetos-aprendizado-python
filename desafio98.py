def escreva(frase):
    print('~'*(len(frase)+4))
    print(f'  {frase}  ')
    print('~'*(len(frase)+4))

while True:
    f = str(input('Digite uma frase para ver ela "estilizada". ')).capitalize()
    escreva(frase = f)
    esc = str(input('Quer digitar mais? [S/N] ')).upper()[0]
    while esc != 'S' and esc != 'N':
        esc = str(input('Por favor digite S para sim e N para não. ')).upper()[0]
    if esc == 'N':
        break
print('FIM')
