'''
#atribuir multiplos valores a uma variavel
lista_mercado = ['Arroz', 'Feijão', 'Carne'] #lista

print(lista_mercado)
print(lista_mercado[0]) #selecionar qual str será printada

lista_mercado.append('Macarrão') #acrescentar informação
print(lista_mercado)

lista_mercado[0] = 'Feijoada' #modificar informação
print(lista_mercado)
#function lists -> funções dentro de listas, para, por exemplo, organizar em ordem alfabética
'''
'''
#concatenar lista
lista_1 = ['a', 'b', 'c']
lista_2 = ['d', 'e', 'f']

nova_lista = lista_1 + lista_2
print(nova_lista)

lista_1.extend(lista_2)
print(lista_1)

item = [['item 1', 'item 2'], ['item 3', 'item 4']] #partições na lista

print(item[0])
print(item[1][0])
'''
'''
#extrair variável
linguagens = ['python', 'java', 'js', 'css']

L1, L2, L3, L4 = linguagens
print(L1)

L1, L2, L3, *other = linguagens #caso não tenha esse asterisco, não vai funcionar, porque, caso contrario, precisa incluir todos os itens da lista.
print(other)
'''
'''
#loop dentro de lista
nomes = ['Davi', 'Miguel', 'Pedro', 'Vitor']

for x in nomes:
    print(x)
'''
'''
#verificando itens em uma lista
cor_pedido = input('Cor desejada:')
cores = ['roxo', 'vermelho', 'verde', 'azul']

if cor_pedido.lower() in cores: #PARA NAO DAR ERRO, LETRA MAIUSCULA != MINUSCULA
    print('Cor disponível!')
else:
    print('Cor indisponível!')
'''