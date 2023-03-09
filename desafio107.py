def sistema(txt = ''):
    from time import sleep
    
    h = None
    while True:
        print('\033[1;;42m~'*27)
        print('  SISTEMA DE AJUDA PyHELP  ''\033[1;;42m \033[m')
        print('\033[1;;42m~\033[m'*27)
        txt = input('Função ou Biblioteca> ').lower()
        if txt == 'fim':
            break
        print('\033[1;;46m~'*(24+len(txt)))
        print(f'  Acessando manual do {txt}  ''\033[1;;46m \033[m',flush=True)
        print('\033[1;;46m~\033[m'*(24+len(txt)))
        sleep(0.5)
        h = help(txt)
    if h == None:
        print('\033[1;;41m~\033[m'*12)
        print("\033[1;;41m  ATÉ LOGO  ")
        return('\033[1;;41m~\033[m'*12)
    if h != None:
        print('\033[7;30m ',end = '')
        help(txt)
        print('\033[m')

duv = sistema()
print(duv)
