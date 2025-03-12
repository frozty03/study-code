msg = 'engenheiro de software'
print(msg[0]) #INDEX
print(msg[0:3]) #SLICING
print(msg[0:3:2]) #SLICING COM STEP
print(msg[0:]) #SLICING SEM LIMITES
print(msg[0:4:3])
print(msg[-1]) #INDEX NEGATIVO
print(msg[-3:]) #SLICING NEGATIVO
print('\n........................................')
msg2 = '  engenheiro de software  '
print(msg2.upper()) #UPPER
print(msg2.lower()) #LOWER
print(msg2.strip()) #STRIP(tirar espaços)
print(msg2.replace('engenheiro', 'cientista')) #REPLACE
print(msg2.split()) #SPLIT
print(msg2.find('de')) #FIND
print('\n........................................')
nome = 'davi'
idade = 18
print('Meu nome é', nome, 'e tenho', idade, 'anos') 
print(f'Meu nome é {nome} e tenho {idade} anos') #F STRING
print('Meu nome é {} e tenho {} anos'.format(nome, idade)) #FORMAT
print('\n........................................')
print('Separação de \nlinhas') #QUEBRA DE LINHA
print('\nTabulação \tde \tespaços') #TABULAÇÃO
print('Barra invertida \\') #BARRA INVERTIDA(duas resulta em uma)
print('colocar \'python\' entre aspas') #COLOCAR ALGO ENTRE ASPAS SEM INTERFERIR
#EXEMPLO DE USO DE TABULAÇÃO
print('\nNome:\tDavi\nIdade:\t18\nPais:\tBrasil')
print('\n........................................')
print('Coração: \u2764') #UNICODE(pesquisar tabela)
print('Coração: \U0001F496') #UNICODE
print('\n........................................')
nome2 = input('Digite seu nome: ') #INPUT(entrada de dados)
idade2 = input('Digite sua idade: ')
pais = input('Digite seu país: ')
print(f'Meu nome é {nome2}, tenho {idade2} anos e moro no {pais}')
print('\nNome:\t', nome2, '\nIdade:\t', idade2, '\nPais:\t', pais)
print('\n........................................')
valor = float(input('Digite um valor: '))
acr = valor + (0.1 * valor)
print(f'O valor final é {acr: .2f}')#2f para duas casas decimais
print('\n........................................')
dados = input('Digite seu nome, idade e altura: ').split() #DAVI 18 176
nome3 = dados[0]
idade3 = dados[1]
altura = dados[2]
print(f'Meu nome é {nome3.upper()}, tenho {idade3} anos e {altura} de altura')
