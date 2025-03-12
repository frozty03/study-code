user = input('Digite seu usuário: ')
senha_user = input('Digite sua senha: ')

userog = 'frozty'
senha = 'd0301'

if senha_user == senha and user == userog:
    print('Acesso permitido!')
else:
    print('Acesso negado!')
