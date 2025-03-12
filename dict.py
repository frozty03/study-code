#armazenar + de 1 info em uma var
'''
variável = {
    'chave': 'valor',
    'chave': 'valor',
    'chave': 'valor'
    ...
}
'''
pessoa = {
    'nome': 'davi',
    'idade': 18,
    'peso': 68.8
}
print(pessoa['nome'])
print(pessoa['idade'])
print(pessoa['peso'])
print('\n........................................')
#exemplo de uso de dicionário
player = {
    'user': 'caio',
    'hp': 100,
    'level': 1,
    'exp': 0,
    'dano': 5.
} 
#DICIONARIO EM UMA LISTA          
npcs = [
    {'nome': 'goblin', 'hp': 50, 'dano': 3},
    {'nome': 'orc', 'hp': 100, 'dano': 10},
    {'nome': 'dragão', 'hp': 200, 'dano': 20}
]
print(npcs[0])
print(npcs[1]['hp'])

