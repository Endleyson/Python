id = int(input('digite a sua idade:'))
if id < 18:
    a = 'você é menor de idade'
else:
    a = 'você é maior de idade'
print('sua idaded é de {} anos e {}'.format(id,a))