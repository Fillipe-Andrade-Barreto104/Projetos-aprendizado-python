def voto(ano):
    from datetime import datetime
    ani = datetime.now().year - ano
    if ani < 16:
        return f'Você não vota, pois tem somente {ani} anos.'
    elif 16 <= ani < 18:
        return f'Seu voto é opcional, pois tem {ani} anos.' 
    elif 18 <= ani < 65:
        return f'Seu voto é obrigatório, pois tem {ani} anos.'
    else:
        return f'Seu voto é opcional, pois tem {ani} anos.'

n = int(input('Digite seu ano de nascimento '))
print(f'{voto(n)}')
