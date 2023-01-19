from math import sin, cos, tan, radians
g= int(input('Digite um ângulo '))
gr= radians(g)
print('O ângulo {} tem como seno {:.2f},\ncomo cosseno {:.2f} \ne como tangente {:.2f}'.format(g,sin(gr), cos(gr), tan(gr)))
