nome= input('qual seu nome: ').lower() .strip()
if nome == 'gustavo':
    a = 'nome bonito!'
elif nome == 'pedro' or nome == 'maria' or nome == 'paulo':
    a = 'nome bem comum no brasil!'
elif nome in ' ana claudia jessica juliana':
    a = 'belo nome feminino!'
else:
    a = 'nome comum!'
print('{}\n tenha um bom dia! {}'.format(a,nome))
print(len(nome))
