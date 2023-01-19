frase= str(input('Digite uma frase '))
f= frase.upper()
f1= f.strip()
f2= f1.count('A')
f3= f1.find('A')+1
f4= f1.rfind('A')+1
print("A letra 'A' aparece {} vezes na frase escrita, sendo sua primeira aparição no caracter {} e sua aparição ultima é no {}.".format(f2,f3,f4))

