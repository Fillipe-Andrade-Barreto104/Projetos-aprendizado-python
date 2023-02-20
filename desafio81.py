numeros = []
for c in range(0,5):
    n = int(input('Digite um valor '))
    if c == 0 and n > 5:
        print('Número adicionado ao final da lista')
        numeros.append(n)
    if c == 0 and n <= 5:
        print('Número adicionado ao inicio da lista')
        numeros.append(n)
    if c == 1 and n > numeros[0]:
        print('Número adicionado ao final da lista')
        numeros.insert(1,n)
    if c == 1 and n < numeros[0]:
        print('Número adicionado ao inicio da lista')
        numeros.insert(0,n)
    if  c == 2 and n > numeros[0] and n < numeros[-1]:
        print('Número adicionado na posição 1')
        numeros.insert(1,n)
    if c == 2 and n < numeros[0]:
        print('Número adicionado ao inicio da lista')
        numeros.insert(0,n)
    if c == 2 and n > numeros[-1]:
        print('Número adicionado ao final da lista')
        numeros.append(n)
    if c == 3 and n < numeros[0]:    
        print('Número adicionado ao inicio da lista')
        numeros.insert(0,n)
    if c == 3 and numeros[0] < n < numeros[1]:    
        print('Número adicionado na posição 1')
        numeros.insert(1,n)
    if c == 3 and numeros[1] < n < numeros[-1]:    
        print('Número adicionado na posição 2')
        numeros.insert(2,n)
    if c == 3 and n > numeros[-1]:    
        print('Número adicionado na posição no final da lista')
        numeros.insert(3,n)
    if c == 4 and n < numeros[0]:    
        print('Número adicionado ao inicio da lista')
        numeros.insert(0,n)
    if c == 4 and numeros[0] < n < numeros[1]:    
        print('Número adicionado na posição 1')
        numeros.insert(1,n)
    if c == 4 and numeros[1] < n < numeros[2]:    
        print('Número adicionado na posição 2')
        numeros.insert(2,n)
    if c == 4 and numeros[2] < n < numeros[3]:    
        print('Número adicionado na posição 3')
        numeros.insert(3,n)
    if c == 4 and n > numeros[-1]:    
        print('Número adicionado no final da lista')
        numeros.append(n)
print(f'Os valores digitadtos foram: {numeros}')
