matriz = [list(), list(), list()]
soma1 = 0
soma2 = 0
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
    if matriz[0][a] % 2==0:
        soma1 = soma1 +  matriz[0][a]
print('')
for b in range(0,len(matriz[1])):
    print(f'[ {matriz[1][b]:^5} ] ',end='')
    if matriz[1][b] % 2==0:
        soma1 = soma1 +  matriz[1][b]
print('')
for c in range(0,len(matriz[2])):
    print(f'[ {matriz[2][c]:^5} ] ',end='')
    if matriz[2][c] % 2==0:
        soma1 = soma1 +  matriz[2][c]
soma2 = soma2 + matriz[0][2]+ matriz[1][2]+ matriz[2][2]
print('')
print('-'*40)
print(f'A soma dos números pares é: {soma1}.')
print(f'A soma dos números da terceira coluna é: {soma2}')
print(f'O maior valor da segunda linha foi: {max(matriz[1])}')
