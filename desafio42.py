nom = str(input('Insira o nome do atleta '))
ida = int(input('Insira a idade do atleta '))
n1 = nom.strip()
n2 = n1.capitalize()
if ida <= 9:
    print('O atleta {} de idade de {} anos deve competir na categoria mirin.'.format(n2,ida))
elif 9 < ida <= 14:
    print('O atleta {} de idade de {} anos deve competir na categoria infantil.'.format(n2,ida))
elif 14 < ida <= 19:
    print('O atleta {} de idade de {} anos deve competir na categoria junior'.format(n2,ida))
elif ida ==20:
    print('O atleta {} de idade de {} anos deve competir na categoria senior.'.format(n2,ida))
elif ida > 20:
    print('O atleta {} de idade de {} anos deve competir na categoria master'.format(n2,ida))



