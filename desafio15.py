tc= float(input('Qual a temperatura de onde você está em graus celcius? '))
tf= (tc*1.8)+32
tk= tc+273
print('A temperatura de {}°C equivale a {:.2}°F e à {:.2} K'.format(tc,tf,tk))