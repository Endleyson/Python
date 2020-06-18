nota=int(input('Digite a sua Nota: '))
if nota>=90 and nota<=100:
    n = 'A'
elif nota>=70 and nota<=89:
    n = 'B'
elif nota>=50 and nota<=69:
    n = 'C'
else:
    n = 'D'
print(' sua nota foi {}, e seu conceito sera {}'.format(nota,n))