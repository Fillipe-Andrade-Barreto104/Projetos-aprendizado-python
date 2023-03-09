def notas(*n, s = False):
    '''
    -> Mostrar total de notas cadastrados
    -> Mostrar a maior e a menor nota
    -> Mostrar a média
    -> Mostrar a situação da turma
    :param n: recebe as notas
    :param s: valor opcional para mostrar ou não a situação da turma
    :return: retorna total de notas, maior e menor nota, a média e a situação da turma
    '''
    print('-'*75)
    dic= {}
    dic["total"] = len(n)
    dic["maior"] = 0
    dic["menor"] = 0
    dic["media"] = 0 
    for b in range(0, len(n)):
        if b == 0:
            dic["maior"] = n[0]
        if dic["maior"] < n[b]:
            dic["maior"] = n[b]    
        if b == 0:
            dic["menor"] = n[0]
        if dic["menor"] > n[b]:
            dic["menor"] = n[b]
        dic["media"] += n[b]
    dic["media"] = dic["media"]/len(n)
    if s == True:
        if dic["media"] >= 7:
            dic["situação"] = 'BOA' 
        elif 6 <= dic["media"] < 7: 
            dic["situação"] = 'RASOÁVEL'
        else:
            dic["situação"] = 'RUIM'
    return dic



no = notas(5.6, 7, 5, 5,s=True)
print(f'{no}')
help(notas)