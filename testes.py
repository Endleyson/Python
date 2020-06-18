print('hello Word!')
num = int(input('digite um numero: '))
if num > 0:
    a = 'é positivo'
elif num< 0:
    a = 'é negativo'
else:
    a = 'é o zero'
print('o numero {} {}'.format(num, a))
