se = str(input('Digite seu sexo [F/M] ')).upper().strip()[0]
while se != 'F' and  se != 'M':
    se = str(input('Por favor digite seu sexo com [F/M]. ')).upper().strip()[0]
print('Voce digitou {}'.format(se))
print('Fim')
