import datetime
an = int(input('Digite o ano que você nasceu '))
a = datetime.date.today()
av = int(a.strftime("%Y"))
dif = (av - an)

if dif < 18:
    al1 = 18 - dif
    print('Você ainda vai ter que se alistar, ainda falta {} ano(s).'.format(al1))
elif dif == 18:
    print('Já está na hora de você se alistar! Vá o quanto antes!')
elif dif > 18:
    al2 = dif - 18
    print('Você está atrasado rapaz! Já se passou {} ano(s) de o senhor se alistar. Vá o quanto antes!'.format(al2))
