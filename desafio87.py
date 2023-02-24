matriz = [list(), list(), list()]
for d in range(0,9):
    print('Digite um valor para ',end='')
    if d <= 2:
        n = int(input('[0,{}] '.format(d)))
        matriz[0].append(n) 
    if 2 < d <= 5:
        n = int(input('[1,{}] '.format(d-3)))
        matriz[1].append(n)
    if 5 < d <= 8:
        n = int(input('[2,{}] '.format(d-6)))
        matriz[2].append(n) 
for a in range(0,len(matriz[0])):
    print(f'[ {matriz[0][a]:^5} ] ',end='')
print('')
for b in range(0,len(matriz[1])):
    print(f'[ {matriz[1][b]:^5} ] ',end='')
print('')
for c in range(0,len(matriz[2])):
    print(f'[ {matriz[2][c]:^5} ] ',end='')
