n =[]
mxv = 0
mnv = 0
pmxv = []
pmnv = []

for c in range(0,5):
    n.append(int(input('Digite um número ')))
print(f'A lista composta por {n} tem como')
mxv = max(n)
mnv = min(n)
for p,v in enumerate(n):
    if v == mxv:
        pmxv.append(p+1)
    if v == mnv:
        pmnv.append(p+1)
if len(pmxv) > 1:
    print(f'O maior valor {mxv} e ele apareceu nas ', end='')
else:
    print(f'O maior valor {mxv} e ele apareceu na ', end='')
for c in range(0, len(pmxv)):
    if c+1 < len(pmxv):
        print(f'{pmxv[c]}ª ', end = '')
    if c+1 == len(pmxv):
        if len(pmxv) > 1:
            print(f'e {pmxv[c]}ª posições')
        else:
            print(f'{pmxv[c]}ª posição')
if len(pmnv) > 1:
    print(f'E o menor valor {mnv} e ele apareceu nas ', end='')
else:
    print(f'E o menor valor {mnv} e ele apareceu na ', end='')
for c in range(0, len(pmnv)):
    if c+1 < len(pmnv):
        print(f'{pmnv[c]}ª ', end = '')
    if c+1 == len(pmnv):
        if len(pmnv) > 1:
            print(f'e {pmnv[c]}ª posições')
        else:
            print(f'{pmnv[c]}ª posição')
