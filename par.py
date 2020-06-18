num = int(input('digite um numero inteiro: '))
modulo = num % 2
if  modulo == 0 :
    a= 'é um numero par'
else:
    a = 'é um numero impar'
print('o numero {} {}'.format(num, a))
