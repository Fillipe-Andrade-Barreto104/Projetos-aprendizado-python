def fatorial(n=1,s=False):
    """
    -> Calcula o fatorial de um número.
        :param n: Número a ser calculado
        :param s: (Opcional) Mostra ou não a conta
        :return n: O valor do fatorial do número n
        :return s: A conta para alcançar o resultado
    """
    fat = 1
    li = list()
    for a in range(n,0,-1):
        li.append(a)
        fat *= a
    if s == True:
            return '{} = {}'.format( ' * '.join(str(x) for x in li), fat)
    else:
         return f'{fat}'
 

print(fatorial(7, True))
help(fatorial)
