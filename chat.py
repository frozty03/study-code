import os
mensagem = []
nome = input('Nome:')


while True:
    os.system('cls')

    if len(mensagem) > 0: #se a lista mensagem tiver mais de 0 elementos
        for m in mensagem:
            print(m['nome'],'-', m['texto']) 
    print("__________________")      

    texto = input('Mensagem:') #obtendo texto e adicionado na lista
    if texto == 'fim':
        break
    mensagem.append({
        'nome': nome,
        'texto': texto
    })





