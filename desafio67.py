cont = 0
soma = 0
while True:
    n = int(input('Digite um número para somar, quando quiser parar digite 999. '))
    if n == 999:
        break
    soma = soma + n
    cont = cont + 1
print(f'Você digitou {cont} número(s) e o valor da soma entre eles foi de {soma}.')