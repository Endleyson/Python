from time import sleep
casa = float(input('Qual o valor da casa?\nR$: '))
salario = float(input('Quanto vc ganha?\nR$: '))
meses = int(input('pretende pagar em quantos meses?\n'))
valor_mensal = casa/meses
a = ''
porcentagem = salario*.3
if valor_mensal > porcentagem:
    a = 'Credito \033[31mNEGADO\033[m!'
else:
    a= 'Credito APROVADO!'
print("""O valor da casa escolhida foi de R${:.2f}, você tem um salario de R${:.2f}
e pretende pagar em {}x""".format(casa, salario, meses))
print('Analisando crédito..')
sleep(3)
print('Devido ao valor da casa de, salario e parcelas você teve o {}'.format(a))
