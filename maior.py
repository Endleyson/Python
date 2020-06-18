num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('digite o segundo numero: '))
if num1<num2:
    a = num2
else:
    a = num1
print('voce digitou {} e {}, e entre eles o maior numero é o {}'.format(num1, num2, a))
